from ryu.base               import app_manager
from ryu.controller         import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto            import ofproto_v1_3, ether, inet
from ryu.lib.packet         import packet, ethernet

class TrafCon(app_manager.RyuApp):
  # Tell Ryu to only accept OpenFlow 1.3
  OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

  # Internal constants for ports, priority, etc
  MAGIC_COOKIE                 = bytearray(b"xyzzy")
  MAGIC_COOKIEB                = bytearray(b"abbba")
  (PORT_H1, PORT_H2)           = (1,2)
  (PRI_LOW, PRI_MID, PRI_HIGH) = (20, 30, 40)

  # Minimal __init__
  def __init__(self, *args, **kwargs):
    super(TrafCon, self).__init__(*args, **kwargs)

  # Helper to prepare format flow add messages
  def add_flow(self, dp, priority, match, actions):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser

    inst = []
    if actions:
      inst = [parser.OFPInstructionActions(
                            ofp.OFPIT_APPLY_ACTIONS,
                            actions)]

    mod = parser.OFPFlowMod(datapath=dp, table_id=0,
                                priority=priority,
                                match=match, instructions=inst)
    dp.set_xid(mod)         # Preallocate transaction ID
    dp.send_msg(mod)    

  # Helper to delete all flows (ie, reset to default)
  # (No filtering on delete, so deletes everything in table 0)
  def del_flows(self, dp):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser

    wildcard_match = parser.OFPMatch()
    instructions   = []

    mod = parser.OFPFlowMod(datapath=dp, table_id=0,
                             command=ofp.OFPFC_DELETE,
                             out_port=ofp.OFPP_ANY,
                             out_group=ofp.OFPP_ANY,
                             match=wildcard_match,
                             instructions=instructions)

    dp.send_msg(mod)

  # Add flow to flood all arp packets, so ARP works
  def flood_all_arp(self, dp):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser

    self.logger.info("Permitting ARP, by flooding")
    match   = parser.OFPMatch(eth_type = ether.ETH_TYPE_ARP)
    actions = [parser.OFPActionOutput(ofp.OFPP_FLOOD, 
                                      ofp.OFPCML_NO_BUFFER)]
    self.add_flow(dp, TrafCon.PRI_MID,
                  match, actions)
 
  # Add override (high priority) to flood traffic from MAC
  def permit_traffic_from_mac(self, dp, src_mac):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser

    self.logger.info("Permitting traffic from %s" % src_mac)
    match   = parser.OFPMatch(eth_src = src_mac)
    actions = [parser.OFPActionOutput(ofp.OFPP_FLOOD, 
                                      ofp.OFPCML_NO_BUFFER)]
    self.add_flow(dp, TrafCon.PRI_HIGH,
                  match, actions)

  # Add (low priority) defaults that block traffic)
  def block_traffic_by_default(self, dp):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser

    self.logger.info("Clearing existing flows")
    self.del_flows(dp)

    self.logger.info("Blocking traffic from h1 port by default")
    match   = parser.OFPMatch(in_port = TrafCon.PORT_H1)
    actions = None
    self.add_flow(dp, TrafCon.PRI_LOW,
                  match, actions)

    self.logger.info("Allowing traffic from h2 port by default")
    match   = parser.OFPMatch(in_port = TrafCon.PORT_H2)
    actions = [parser.OFPActionOutput(ofp.OFPP_FLOOD, 
                                      ofp.OFPCML_NO_BUFFER)]
    self.add_flow(dp, TrafCon.PRI_LOW,
                  match, actions)

  # Ask switch to send us UDP packets from host 1
  def add_notify_on_udp_from_host_1(self, dp):
    ofp    = dp.ofproto
    parser = dp.ofproto_parser
    
    self.logger.info("Request notify on UDP from h1")
    match   = parser.OFPMatch(in_port  = TrafCon.PORT_H1,
                              eth_type = ether.ETH_TYPE_IP,
                              ip_proto = inet.IPPROTO_UDP)
    actions = [parser.OFPActionOutput(ofp.OFPP_CONTROLLER, 
                                      ofp.OFPCML_NO_BUFFER)]
    self.add_flow(dp, TrafCon.PRI_MID,
                  match, actions)
    
  @set_ev_cls(ofp_event.EventOFPStateChange, 
              MAIN_DISPATCHER)
  def new_connection(self, ev):
    dp = ev.datapath
    self.logger.info("Switch connected (id=%s)" % dp.id)
    self.block_traffic_by_default(dp)
    self.flood_all_arp(dp)
    self.add_notify_on_udp_from_host_1(dp)

  @set_ev_cls(ofp_event.EventOFPPacketIn, 
              MAIN_DISPATCHER)
  def handle_packet(self, ev):
     pkt = packet.Packet(ev.msg.data) 
     eth = pkt.get_protocol(ethernet.ethernet)     
     self.logger.info("UDP received from %s" % eth.src)
     if ev.msg.data.find(TrafCon.MAGIC_COOKIE) >= 0:
       self.logger.info("Magic cookie found from %s" % eth.src)
       self.permit_traffic_from_mac(ev.msg.datapath, eth.src)
     if ev.msg.data.find(TrafCon.MAGIC_COOKIEB) >= 0:
       self.logger.info("Communnication a ete bloquee pour : %s" % eth.src)
       self.block_traffic_by_default(ev.msg.datapath)
       self.flood_all_arp(ev.msg.datapath)
       self.add_notify_on_udp_from_host_1(ev.msg.datapath)

