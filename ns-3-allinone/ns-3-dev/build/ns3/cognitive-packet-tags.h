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
 * Author:
 *  Abdulla Al-Ali <al-ali.a@husky.neu.edu>
 */

#ifndef COGNITIVE_PACKET_TAGS_H_
#define COGNITIVE_PACKET_TAGS_H_

#include "ns3/tag.h"

namespace ns3 {

enum PacketType
{
  CTRL_PACKET  = 1,   //for packets destined to ctrl interface
  DATA_PACKET  = 2   //for packets destined to tx interface
};

class PacketTypePacketTag : public Tag
{
public:

  PacketTypePacketTag (PacketType t = CTRL_PACKET);
  static TypeId GetTypeId (void);
  virtual TypeId GetInstanceTypeId (void) const;
  virtual uint32_t GetSerializedSize (void) const;
  virtual void Serialize (TagBuffer i) const;
  virtual void Deserialize (TagBuffer i);

  void Print (std::ostream &os) const;
  void Set (PacketType m_type);
  PacketType Get () const { return m_type; }

private:
  PacketType m_type;
};

class PacketChannelPacketTag : public Tag
{
public:

  PacketChannelPacketTag (uint16_t t = 0);
  static TypeId GetTypeId (void);
  virtual TypeId GetInstanceTypeId (void) const;
  virtual uint32_t GetSerializedSize (void) const;
  virtual void Serialize (TagBuffer i) const;
  virtual void Deserialize (TagBuffer i);

  void Print (std::ostream &os) const;
  uint16_t GetChannel () const { return m_channel; }

private:
  uint16_t m_channel;
};

}
#endif /* COGNITIVE_PACKET_TAGS_H_ */
