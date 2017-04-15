#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import NSLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

import ns.core
import ns.network
import ns.point_to_point

class MyNSLink(NSLink):
    def __init__(self, **opts, interface0, interface1):
		NSLink.__init__(self, **opts, interface0, interface1)
		#
		# We are interacting with the outside, real, world.  This means we have to 
		# interact in real-time and therefore we have to use the real-time simulator
		# and take the time to calculate checksums.
		#
		ns.core.GlobalValue.Bind("SimulatorImplementationType", ns.core.StringValue("ns3::RealtimeSimulatorImpl"))
		ns.core.GlobalValue.Bind("ChecksumEnabled", ns.core.BooleanValue("true"))

		#
		# Create two ghost nodes.  The first will represent the interface
		# on the left side of the link; and the second will represent the interface on 
		# the right side.
		#
		nodes = ns.network.NodeContainer()
		nodes.Create (2);

		#
		# We're going to use 802.11 A so set up a wifi helper to reflect that.
		#
		wifi = ns.wifi.WifiHelper.Default()
		wifi.SetStandard (ns.wifi.WIFI_PHY_STANDARD_80211a);
		wifi.SetRemoteStationManager ("ns3::ConstantRateWifiManager", "DataMode", ns.core.StringValue ("OfdmRate54Mbps"));

		#
		# We'll use an ad-hoc network.
		#
		wifiMac = ns.wifi.NqosWifiMacHelper.Default()
		wifiMac.SetType ("ns3::AdhocWifiMac");

		#
		# Configure the physicial layer.
		#
		wifiChannel = ns.wifi.YansWifiChannelHelper.Default()
		wifiPhy = ns.wifi.YansWifiPhyHelper.Default()
		wifiPhy.SetChannel(wifiChannel.Create())

		#
		# Install the wireless devices onto our ghost nodes.
		#
		devices = wifi.Install(wifiPhy, wifiMac, nodes)

		#
		# We need location information since we are talking about wifi, so add a
		# constant position to the ghost nodes.
		#
		mobility = ns.mobility.MobilityHelper()
		positionAlloc = ns.mobility.ListPositionAllocator()
		positionAlloc.Add(ns.core.Vector(0.0, 0.0, 0.0))
		positionAlloc.Add(ns.core.Vector(5.0, 0.0, 0.0))
		mobility.SetPositionAllocator(positionAlloc)
		mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel")
		mobility.Install(nodes)

		#
		# Use the TapBridgeHelper to connect to the pre-configured tap devices for 
		# the left side. 

		tapBridge = ns.tap_bridge.TapBridgeHelper()
		tapBridge.SetAttribute ("Mode", ns.core.StringValue ("UseLocal"));
		tapBridge.SetAttribute ("DeviceName", interface0);
		tapBridge.Install (nodes.Get (0), devices.Get (0));

		#
		# Connect the right side tap to the right side wifi device on the right-side
		# ghost node.
		#
		tapBridge.SetAttribute ("DeviceName", interface1);
		tapBridge.Install (nodes.Get (1), devices.Get (1));


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n=2, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n):
			host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch, MyNSLink())

def Test():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo=topo, link=NSLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    Test()