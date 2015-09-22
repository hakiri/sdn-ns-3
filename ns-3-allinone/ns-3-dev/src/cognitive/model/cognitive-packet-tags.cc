/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2005,2006,2007 INRIA
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
 * Author: Abdulla Al-Ali <al-ali.a@husky.neu.edu>
 */

#include "cognitive-packet-tags.h"

namespace ns3 {

PacketTypePacketTag::PacketTypePacketTag (PacketType t) :
  m_type (t)
{
}

TypeId
PacketTypePacketTag::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PacketTypePacketTag")
    .SetParent<Tag> ()
    .AddConstructor<PacketTypePacketTag> ()
  ;
  return tid;
}
TypeId
PacketTypePacketTag::GetInstanceTypeId (void) const
{
  return GetTypeId ();
}

uint32_t
PacketTypePacketTag::GetSerializedSize (void) const
{
  return 1;
}
void
PacketTypePacketTag::Serialize (TagBuffer i) const
{
  i.WriteU8 (m_type);
}
void
PacketTypePacketTag::Deserialize (TagBuffer i)
{
  m_type = (PacketType) i.ReadU8 ();
}

void
PacketTypePacketTag::Print (std::ostream &os) const
{
  switch (m_type)
    {
    case CTRL_PACKET:
      {
        os << "ctrl_packet";
        break;
      }
    case DATA_PACKET:
      {
        os << "data_packet";
        break;
      }
    default:
      os << "UNKNOWN_TYPE";
      break;
    }
}

PacketChannelPacketTag::PacketChannelPacketTag (uint16_t t) :
  m_channel (t)
{
}

TypeId
PacketChannelPacketTag::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PacketChannelPacketTag")
    .SetParent<Tag> ()
    .AddConstructor<PacketChannelPacketTag> ()
  ;
  return tid;
}
TypeId
PacketChannelPacketTag::GetInstanceTypeId (void) const
{
  return GetTypeId ();
}

uint32_t
PacketChannelPacketTag::GetSerializedSize (void) const
{
  return 2;
}
void
PacketChannelPacketTag::Serialize (TagBuffer i) const
{
  i.WriteU16 (m_channel);
}
void
PacketChannelPacketTag::Deserialize (TagBuffer i)
{
  m_channel = i.ReadU16 ();
}

void
PacketChannelPacketTag::Print (std::ostream &os) const
{
  os << "packet channel: " << m_channel;
}

}
