/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2005 INRIA
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Mathieu Lacage <mathieu.lacage@sophia.inria.fr>
 */

#include "ns3/assert.h"
#include "ns3/packet.h"
#include "ns3/log.h"
#include "ns3/simulator.h"
#include "ns3/node.h"
#include "ns3/uinteger.h"
#include "ns3/pointer.h"
#include "dca-txop.h"
#include "dcf-manager.h"
#include "mac-low.h"
#include "wifi-mac-queue.h"
#include "mac-tx-middle.h"
#include "wifi-mac-trailer.h"
#include "wifi-mac.h"
#include "random-stream.h"
#include "yans-wifi-phy.h"

#undef NS_LOG_APPEND_CONTEXT
#define NS_LOG_APPEND_CONTEXT if (m_low != 0) { std::clog << "[mac=" << m_low->GetAddress () << "] "; }

namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("DcaTxop");

DcaTxop::ActiveChannels::ActiveChannels(uint16_t channel, Time lastActive)
  : channel (channel),
    lastActive (lastActive)
{
}

class DcaTxop::Dcf : public DcfState
{
public:
  Dcf (DcaTxop * txop)
    : m_txop (txop)
  {
  }

private:
  virtual void DoNotifyAccessGranted (void)
  {
    m_txop->NotifyAccessGranted ();
  }
  virtual void DoNotifyInternalCollision (void)
  {
    m_txop->NotifyInternalCollision ();
  }
  virtual void DoNotifyCollision (void)
  {
    m_txop->NotifyCollision ();
  }
  virtual void DoNotifyChannelSwitching (void)
  {
    m_txop->NotifyChannelSwitching ();
  }

/*
  virtual void DoNotifyChannelSwitching (Time duration, uint16_t toChannel)
  {
      m_txop->NotifyChannelSwitching (duration, toChannel);
  }
  virtual void DoNotifyChannelSensing (void)
  {
      m_txop->NotifyChannelSensing ();
  }
  
  */
  
  virtual void DoNotifySleep (void)
  {
    m_txop->NotifySleep ();
  }
  virtual void DoNotifyWakeUp (void)
  {
    m_txop->NotifyWakeUp ();
  }

  DcaTxop *m_txop;
};


/**
 * Listener for MacLow events. Forwards to DcaTxop.
 */
class DcaTxop::TransmissionListener : public MacLowTransmissionListener
{
public:
  /**
   * Create a TransmissionListener for the given DcaTxop.
   *
   * \param txop
   */
  TransmissionListener (DcaTxop * txop)
    : MacLowTransmissionListener (),
      m_txop (txop)
  {
  }

  virtual ~TransmissionListener ()
  {
  }

  virtual void GotCts (double snr, WifiMode txMode)
  {
    m_txop->GotCts (snr, txMode);
  }
  virtual void MissedCts (void)
  {
    m_txop->MissedCts ();
  }
  virtual void GotAck (double snr, WifiMode txMode)
  {
    m_txop->GotAck (snr, txMode);
  }
  virtual void MissedAck (void)
  {
    m_txop->MissedAck ();
  }
  virtual void StartNext (void)
  {
    m_txop->StartNext ();
  }
  virtual void Cancel (void)
  {
    m_txop->Cancel ();
  }
  virtual void EndTxNoAck (void)
  {
    m_txop->EndTxNoAck ();
  }

private:
  DcaTxop *m_txop;
};

NS_OBJECT_ENSURE_REGISTERED (DcaTxop);

TypeId
DcaTxop::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::DcaTxop")
    .SetParent<ns3::Dcf> ()
    .SetGroupName ("Wifi")
    .AddConstructor<DcaTxop> ()
    .AddAttribute ("Queue", "The WifiMacQueue object",
                   PointerValue (),
                   MakePointerAccessor (&DcaTxop::GetQueue),
                   MakePointerChecker<WifiMacQueue> ())
    .AddAttribute ("ChannelActiveTimeout",
                  "After how long should a channel be considered inactive if not used",
                   TimeValue (Seconds (2)),
                   MakeTimeAccessor (&DcaTxop::m_activeChannelTimeout),
                   MakeTimeChecker ())
    .AddAttribute ("QueueUtilizationInterval",
                  "How long should we transmit on a queue for a specific channel",
                   TimeValue (MilliSeconds (150)),
                   MakeTimeAccessor (&DcaTxop::m_queueUtilizationTime),
                   MakeTimeChecker ())
  ;
  return tid;
}

DcaTxop::DcaTxop ()
  : m_manager (0),
    m_currentPacket (0)
{
  NS_LOG_FUNCTION (this);
  m_transmissionListener = new DcaTxop::TransmissionListener (this);
  m_dcf = new DcaTxop::Dcf (this);
  m_queue = CreateObject<WifiMacQueue> ();
  m_rng = new RealRandomStream ();
}

DcaTxop::~DcaTxop ()
{
  NS_LOG_FUNCTION (this);
  m_switchQueueTimer.Cancel();
}

void
DcaTxop::DoDispose (void)
{
  NS_LOG_FUNCTION (this);
  m_queue = 0;
  m_low = 0;
  m_stationManager = 0;
  delete m_transmissionListener;
  delete m_dcf;
  delete m_rng;
  m_transmissionListener = 0;
  m_dcf = 0;
  m_rng = 0;
  m_txMiddle = 0;
}

void
DcaTxop::SetManager (DcfManager *manager)
{
  NS_LOG_FUNCTION (this << manager);
  m_manager = manager;
  m_manager->Add (m_dcf);
}

void DcaTxop::SetTxMiddle (MacTxMiddle *txMiddle)
{
  m_txMiddle = txMiddle;
}

void
DcaTxop::SetLow (Ptr<MacLow> low)
{
  NS_LOG_FUNCTION (this << low);
  m_low = low;
}

void
DcaTxop::SetWifiRemoteStationManager (Ptr<WifiRemoteStationManager> remoteManager)
{
  NS_LOG_FUNCTION (this << remoteManager);
  m_stationManager = remoteManager;
}

void
DcaTxop::SetTxOkCallback (TxOk callback)
{
  NS_LOG_FUNCTION (this << &callback);
  m_txOkCallback = callback;
}

void
DcaTxop::SetTxFailedCallback (TxFailed callback)
{
  NS_LOG_FUNCTION (this << &callback);
  m_txFailedCallback = callback;
}

Ptr<WifiMacQueue >
DcaTxop::GetQueue () const
{
  NS_LOG_FUNCTION (this);
  return m_queue;
}

void
DcaTxop::SetMinCw (uint32_t minCw)
{
  NS_LOG_FUNCTION (this << minCw);
  m_dcf->SetCwMin (minCw);
}

void
DcaTxop::SetMaxCw (uint32_t maxCw)
{
  NS_LOG_FUNCTION (this << maxCw);
  m_dcf->SetCwMax (maxCw);
}

void
DcaTxop::SetAifsn (uint32_t aifsn)
{
  NS_LOG_FUNCTION (this << aifsn);
  m_dcf->SetAifsn (aifsn);
}

uint32_t
DcaTxop::GetMinCw (void) const
{
  NS_LOG_FUNCTION (this);
  return m_dcf->GetCwMin ();
}

uint32_t
DcaTxop::GetMaxCw (void) const
{
  NS_LOG_FUNCTION (this);
  return m_dcf->GetCwMax ();
}

uint32_t
DcaTxop::GetAifsn (void) const
{
  NS_LOG_FUNCTION (this);
  return m_dcf->GetAifsn ();
}

void
DcaTxop::Queue (Ptr<const Packet> packet, const WifiMacHeader &hdr)
{
  NS_LOG_FUNCTION (this << packet << &hdr);
  WifiMacTrailer fcs;
  uint32_t fullPacketSize = hdr.GetSerializedSize () + packet->GetSize () + fcs.GetSerializedSize ();
  m_stationManager->PrepareForQueue (hdr.GetAddr1 (), &hdr,
                                     packet, fullPacketSize);
  PacketChannelPacketTag pcpt;
  bool found = packet->PeekPacketTag(pcpt);
  NS_LOG_LOGIC ("Enqueue packet to channel : " << pcpt.GetChannel() <<
        " current channel: " << m_low->GetPhy()->GetChannelNumber());
    if (m_low && found)
      {
        if (m_low->IsTxRadio() && m_low->GetPhy()->GetChannelNumber() == 1) //first packet
          {
            NS_LOG_LOGIC ("Switch PHY to channel: " << pcpt.GetChannel());
            m_low->GetPhy()->SetChannelNumber(pcpt.GetChannel());
          }
      }
  m_queue->Enqueue (packet, hdr);

  if (pcpt.GetChannel()!=1 && pcpt.GetChannel()!=0 &&
        m_low->IsTxRadio())
      UpdateActiveChannels(pcpt.GetChannel());
    //start the switching queue timer
    if (!m_switchQueueTimer.IsRunning() && m_low->IsTxRadio ())
        {
          m_switchQueueTimer = Simulator::Schedule(m_queueUtilizationTime,
              &DcaTxop::SwitchQueueHandler, this);
        }
  StartAccessIfNeeded ();
}

void
DcaTxop::UpdateActiveChannels(uint16_t channel)
{
  NS_LOG_FUNCTION (this << channel);
  bool found = false;
  if (m_activeChannels.empty())
    {
      m_activeChannels.push_back(DcaTxop::ActiveChannels(channel, Simulator::Now()));
      return;
    }
  else
    {
      ListActiveChannelsI it;
      for (it = m_activeChannels.begin (); it != m_activeChannels.end (); ++it)
      {
        uint16_t chan = it->channel;
        if (channel == chan)
        {
          //update current entry
          it->lastActive = Simulator::Now();
          found = true;
          break;
        }
      }
    }
  if (!found)
    {
      m_activeChannels.push_back(DcaTxop::ActiveChannels(channel, Simulator::Now()));
    }
}

uint16_t
DcaTxop::GetNextActiveChannel (void)
{
  //Only traverse if we're not empty and not size = 1
  if (!m_activeChannels.empty() && m_activeChannels.size()!=1)
  {
    ListActiveChannelsI it;
    ListActiveChannelsI startIterator;
    bool startLooking = false;
    bool keepRunning = true;
    while (keepRunning) {
      keepRunning = false;
      it = m_activeChannels.begin();
      long unsigned int count = 0;
      while (it != startIterator)
      {
        count++;
        if (it->channel == m_currentChannel && !startLooking)
        {
          NS_LOG_LOGIC ("rotate STARTS: " << count);
          startLooking = true;
          startIterator = it;
        }
        if (startLooking)
        {
          if (Simulator::Now() - it->lastActive > m_activeChannelTimeout
              && it->channel != m_currentChannel)
          {
            //record is too old. let's not use this channel anymore
            NS_LOG_LOGIC ("Disabling channel " << it->channel << " usage in TX radio");
            m_activeChannels.erase(it);
            if (m_activeChannels.size() == 1) return m_currentChannel;
            keepRunning = true;
            break;
          }
          else if ( it->channel != m_currentChannel )
          {
            //record is good! let's switch
            NS_LOG_LOGIC ("Found next active channel " << it->channel);
            return it->channel;
          }
        }

        //rotate
        if (count == m_activeChannels.size()) {
          it = m_activeChannels.begin();
        }
        else ++it;

      }
    }
  }

  NS_LOG_LOGIC ("No next active channel found");
  return m_currentChannel;
}




int64_t
DcaTxop::AssignStreams (int64_t stream)
{
  NS_LOG_FUNCTION (this << stream);
  m_rng->AssignStreams (stream);
  return 1;
}

void
DcaTxop::RestartAccessIfNeeded (void)
{
  NS_LOG_FUNCTION (this);
  if ((m_currentPacket != 0
       //|| !m_queue->IsEmpty ())
      || !m_queue->IsEmpty (m_currentChannel))
      && !m_dcf->IsAccessRequested ())
    {
      m_manager->RequestAccess (m_dcf);
    }
}

void
DcaTxop::StartAccessIfNeeded (void)
{
  NS_LOG_FUNCTION (this);
  if (m_currentPacket == 0
      //&& !m_queue->IsEmpty () //  FIX ME: Changed to support cognitive channel scanning
      && !m_queue->IsEmpty (m_currentChannel)
      && !m_dcf->IsAccessRequested ())
    {
      m_manager->RequestAccess (m_dcf);
    }
}

Ptr<MacLow>
DcaTxop::Low (void)
{
  NS_LOG_FUNCTION (this);
  return m_low;
}

bool
DcaTxop::NeedRts (Ptr<const Packet> packet, const WifiMacHeader *header)
{
  NS_LOG_FUNCTION (this << packet << header);
  return m_stationManager->NeedRts (header->GetAddr1 (), header,
                                    packet);
}

void
DcaTxop::DoInitialize ()
{
  NS_LOG_FUNCTION (this);
  m_dcf->ResetCw ();
  m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
  m_currentChannel = m_low->GetPhy()->GetChannelNumber();
  ns3::Dcf::DoInitialize ();
}

bool
DcaTxop::NeedRtsRetransmission (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->NeedRtsRetransmission (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                                  m_currentPacket);
}

bool
DcaTxop::NeedDataRetransmission (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->NeedDataRetransmission (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                                   m_currentPacket);
}

bool
DcaTxop::NeedFragmentation (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->NeedFragmentation (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                              m_currentPacket);
}

void
DcaTxop::NextFragment (void)
{
  NS_LOG_FUNCTION (this);
  m_fragmentNumber++;
}

uint32_t
DcaTxop::GetFragmentSize (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->GetFragmentSize (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                            m_currentPacket, m_fragmentNumber);
}

bool
DcaTxop::IsLastFragment (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->IsLastFragment (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                           m_currentPacket, m_fragmentNumber);
}

uint32_t
DcaTxop::GetNextFragmentSize (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->GetFragmentSize (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                            m_currentPacket, m_fragmentNumber + 1);
}

uint32_t
DcaTxop::GetFragmentOffset (void)
{
  NS_LOG_FUNCTION (this);
  return m_stationManager->GetFragmentOffset (m_currentHdr.GetAddr1 (), &m_currentHdr,
                                              m_currentPacket, m_fragmentNumber);
}

Ptr<Packet>
DcaTxop::GetFragmentPacket (WifiMacHeader *hdr)
{
  NS_LOG_FUNCTION (this << hdr);
  *hdr = m_currentHdr;
  hdr->SetFragmentNumber (m_fragmentNumber);
  uint32_t startOffset = GetFragmentOffset ();
  Ptr<Packet> fragment;
  if (IsLastFragment ())
    {
      hdr->SetNoMoreFragments ();
    }
  else
    {
      hdr->SetMoreFragments ();
    }
  fragment = m_currentPacket->CreateFragment (startOffset,
                                              GetFragmentSize ());
  return fragment;
}

bool
DcaTxop::NeedsAccess (void) const
{
  NS_LOG_FUNCTION (this);
  //return !m_queue->IsEmpty () || m_currentPacket != 0;  // FIX ME: added below to support channel scanning
    return !m_queue->IsEmpty (m_currentChannel) || m_currentPacket != 0;
}
void
DcaTxop::NotifyAccessGranted (void)
{
  NS_LOG_FUNCTION (this);
  if (m_currentPacket == 0)
    {
     // if (m_queue->IsEmpty ()) // Modified below
      if (m_queue->IsEmpty (m_currentChannel))
        {
          NS_LOG_DEBUG ("queue empty");
          return;
        }
      // m_currentPacket = m_queue->Dequeue (&m_currentHdr); // Modified Below
      m_currentPacket = m_queue->DequeueForChannel (&m_currentHdr, m_currentChannel);

      NS_ASSERT (m_currentPacket != 0);
      uint16_t sequence = m_txMiddle->GetNextSequenceNumberfor (&m_currentHdr);
      m_currentHdr.SetSequenceNumber (sequence);
      m_stationManager->UpdateFragmentationThreshold ();
      m_currentHdr.SetFragmentNumber (0);
      m_currentHdr.SetNoMoreFragments ();
      m_currentHdr.SetNoRetry ();
      m_fragmentNumber = 0;
      NS_LOG_DEBUG ("dequeued size=" << m_currentPacket->GetSize () <<
                    ", to=" << m_currentHdr.GetAddr1 () <<
                    ", seq=" << m_currentHdr.GetSequenceControl ());
    }
  MacLowTransmissionParameters params;
  params.DisableOverrideDurationId ();
  if (m_currentHdr.GetAddr1 ().IsGroup ())
    {
      params.DisableRts ();
      params.DisableAck ();
      params.DisableNextData ();
      Low ()->StartTransmission (m_currentPacket,
                                 &m_currentHdr,
                                 params,
                                 m_transmissionListener);
      NS_LOG_DEBUG ("tx broadcast");
    }
  else
    {
      params.EnableAck ();

      if (NeedFragmentation ())
        {
          WifiMacHeader hdr;
          Ptr<Packet> fragment = GetFragmentPacket (&hdr);
          if (NeedRts (fragment, &hdr))
            {
              params.EnableRts ();
            }
          else
            {
              params.DisableRts ();
            }
          if (IsLastFragment ())
            {
              NS_LOG_DEBUG ("fragmenting last fragment size=" << fragment->GetSize ());
              params.DisableNextData ();
            }
          else
            {
              NS_LOG_DEBUG ("fragmenting size=" << fragment->GetSize ());
              params.EnableNextData (GetNextFragmentSize ());
            }
          Low ()->StartTransmission (fragment, &hdr, params,
                                     m_transmissionListener);
        }
      else
        {
          if (NeedRts (m_currentPacket, &m_currentHdr))
            {
              params.EnableRts ();
              NS_LOG_DEBUG ("tx unicast rts");
            }
          else
            {
              params.DisableRts ();
              NS_LOG_DEBUG ("tx unicast");
            }
          params.DisableNextData ();
          Low ()->StartTransmission (m_currentPacket, &m_currentHdr,
                                     params, m_transmissionListener);
        }
    }
}

void
DcaTxop::NotifyInternalCollision (void)
{
  NS_LOG_FUNCTION (this);
  NotifyCollision ();
}

void
DcaTxop::NotifyCollision (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("collision");
  m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
  RestartAccessIfNeeded ();
}

void
DcaTxop::NotifyChannelSwitching (void)
{
  NS_LOG_FUNCTION (this);
  m_queue->Flush ();
  m_currentPacket = 0;
}


// FIX ME: To new added methods for cognitive radio
void
DcaTxop::NotifyChannelSwitching (Time duration, uint16_t toChannel)
{
  NS_LOG_FUNCTION (this);
  m_currentChannel = toChannel;
  m_currentPacket = 0;
}

void
DcaTxop::NotifyChannelSensing (void)
 {
   NS_LOG_FUNCTION (this);
   m_currentPacket = 0;
 }


void
DcaTxop::NotifySleep (void)
{
  NS_LOG_FUNCTION (this);
  if (m_currentPacket != 0)
    {
      m_queue->PushFront (m_currentPacket, m_currentHdr);
      m_currentPacket = 0;
    }
}

void
DcaTxop::NotifyWakeUp (void)
{
  NS_LOG_FUNCTION (this);
  RestartAccessIfNeeded ();
}

void
DcaTxop::GotCts (double snr, WifiMode txMode)
{
  NS_LOG_FUNCTION (this << snr << txMode);
  NS_LOG_DEBUG ("got cts");
}

void
DcaTxop::MissedCts (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("missed cts");
  if (!NeedRtsRetransmission ())
    {
      NS_LOG_DEBUG ("Cts Fail");
      m_stationManager->ReportFinalRtsFailed (m_currentHdr.GetAddr1 (), &m_currentHdr);
      if (!m_txFailedCallback.IsNull ())
        {
          m_txFailedCallback (m_currentHdr);
        }
      //to reset the dcf.
      m_currentPacket = 0;
      m_dcf->ResetCw ();
    }
  else
    {
      m_dcf->UpdateFailedCw ();
    }
  m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
  RestartAccessIfNeeded ();
}

void
DcaTxop::GotAck (double snr, WifiMode txMode)
{
  NS_LOG_FUNCTION (this << snr << txMode);
  if (!NeedFragmentation ()
      || IsLastFragment ())
    {
      NS_LOG_DEBUG ("got ack. tx done.");
      if (!m_txOkCallback.IsNull ())
        {
          m_txOkCallback (m_currentHdr);
        }

      /* we are not fragmenting or we are done fragmenting
       * so we can get rid of that packet now.
       */
      m_currentPacket = 0;
      m_dcf->ResetCw ();
      m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
      RestartAccessIfNeeded ();
    }
  else
    {
      NS_LOG_DEBUG ("got ack. tx not done, size=" << m_currentPacket->GetSize ());
    }
}

void
DcaTxop::MissedAck (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("missed ack");
  if (!NeedDataRetransmission ())
    {
      NS_LOG_DEBUG ("Ack Fail");
      m_stationManager->ReportFinalDataFailed (m_currentHdr.GetAddr1 (), &m_currentHdr);
      if (!m_txFailedCallback.IsNull ())
        {
          m_txFailedCallback (m_currentHdr);
        }
      //to reset the dcf.
      m_currentPacket = 0;
      m_dcf->ResetCw ();
    }
  else
    {
      NS_LOG_DEBUG ("Retransmit");
      m_currentHdr.SetRetry ();
      m_dcf->UpdateFailedCw ();
    }
  m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
  RestartAccessIfNeeded ();
}

void
DcaTxop::StartNext (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("start next packet fragment");
  /* this callback is used only for fragments. */
  NextFragment ();
  WifiMacHeader hdr;
  Ptr<Packet> fragment = GetFragmentPacket (&hdr);
  MacLowTransmissionParameters params;
  params.EnableAck ();
  params.DisableRts ();
  params.DisableOverrideDurationId ();
  if (IsLastFragment ())
    {
      params.DisableNextData ();
    }
  else
    {
      params.EnableNextData (GetNextFragmentSize ());
    }
  Low ()->StartTransmission (fragment, &hdr, params, m_transmissionListener);
}

void
DcaTxop::Cancel (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("transmission cancelled");
  /**
   * This happens in only one case: in an AP, you have two DcaTxop:
   *   - one is used exclusively for beacons and has a high priority.
   *   - the other is used for everything else and has a normal
   *     priority.
   *
   * If the normal queue tries to send a unicast data frame, but
   * if the tx fails (ack timeout), it starts a backoff. If the beacon
   * queue gets a tx oportunity during this backoff, it will trigger
   * a call to this Cancel function.
   *
   * Since we are already doing a backoff, we will get access to
   * the medium when we can, we have nothing to do here. We just
   * ignore the cancel event and wait until we are given again a
   * tx oportunity.
   *
   * Note that this is really non-trivial because each of these
   * frames is assigned a sequence number from the same sequence
   * counter (because this is a non-802.11e device) so, the scheme
   * described here fails to ensure in-order delivery of frames
   * at the receiving side. This, however, does not matter in
   * this case because we assume that the receiving side does not
   * update its <seq,ad> tupple for packets whose destination
   * address is a broadcast address.
   */
}

void
DcaTxop::EndTxNoAck (void)
{
  NS_LOG_FUNCTION (this);
  NS_LOG_DEBUG ("a transmission that did not require an ACK just finished");
  m_currentPacket = 0;
  m_dcf->ResetCw ();
  m_dcf->StartBackoffNow (m_rng->GetNext (0, m_dcf->GetCw ()));
  StartAccessIfNeeded ();
}

void
DcaTxop::SwitchQueueHandler (void)
{
  NS_LOG_FUNCTION (this);
  //we must see which channels are TX active, and switch if necessary
  uint16_t channel = GetNextActiveChannel();
  Time nextQueueSwitch = m_queueUtilizationTime;
  if (m_currentChannel != channel)
  {
    //we're switching
    NS_LOG_DEBUG ("Queue switching on TX radio from channel "
        << m_currentChannel << " to channel " << channel);

    m_low->GetPhy()->SetChannelNumber(channel);

    m_currentChannel = channel;

    nextQueueSwitch = nextQueueSwitch + m_low->GetPhy()->GetDelayUntilIdle();

    Ptr<YansWifiPhy> phy = DynamicCast<YansWifiPhy>(m_low->GetPhy());
    if (phy->GetDelayUntilIdle()<phy->GetSwitchingDelay())
      nextQueueSwitch = nextQueueSwitch + phy->GetSwitchingDelay();
    Simulator::Schedule( (nextQueueSwitch-m_queueUtilizationTime), &DcaTxop::RestartAccessIfNeeded, this);
  }

  //Call this function again
  m_switchQueueTimer = Simulator::Schedule (nextQueueSwitch,
      &DcaTxop::SwitchQueueHandler, this);
}



} //namespace ns3
