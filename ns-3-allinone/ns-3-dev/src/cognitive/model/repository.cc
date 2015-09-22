/*
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
 * Author: Abdulla K. Al-Ali <abdulla.alali@qu.edu.qa>
 */

// Class Repository 
// Cross-Layer Repository to enable channel information sharing between MAC and routing protocols

#include "repository.h"

NS_LOG_COMPONENT_DEFINE ("CogRepository");

namespace ns3 {

TypeId
Repository::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::Repository")
    .SetParent<Object> ()
    .AddConstructor<Repository> ()
  ;
  return tid;
}


// Initializer
Repository::Repository() {

  NS_LOG_FUNCTION (this);
	// Set randomly the receiver channel for each node	
	for (int i=0; i<MAX_NODES; i++) {
		int channel=GetRandomChannel();
		m_repositoryTable[i].rxChannel= channel;
	}
	char mystring [50];
	for (int i=0; i<5; i++) {
	  sprintf(mystring, "node %i got channel %i",i, m_repositoryTable[i].rxChannel);
	  NS_LOG_DEBUG(mystring);
	}

	// Initialize each sending channel as NOT active for each node
	for (int node=0; node<MAX_NODES; node++) 
		for (int channel=0; channel< MAX_CHANNELS; channel++) 
			m_repositoryTableSender[node][channel].active=false;



}




//GetRxChannel: Return the receiving channel for a node
int 
Repository::GetRxChannel(int node) {
	if (node < MAX_NODES)
		return m_repositoryTable[node].rxChannel;
	else
		return -1;

}
		 

//SetRxChannel: Set the receiving channel for a node
void 
Repository::SetRxChannel(int node, int channel) {
	if (node < MAX_NODES)
		m_repositoryTable[node].rxChannel=channel;

}

		
// UpdateTxChannel: Set the sending channel as active, at the current time
void 
Repository::UpdateTxChannel(int node, int channel, double time) {

	if (node < MAX_NODES)  {
		
		m_repositoryTableSender[node][channel].active=true;
		m_repositoryTableSender[node][channel].time=time;
	
	 }

}

//GetRandomChannel: Return a random channel between 1 and MAX_CHANNELS
int 
Repository::GetRandomChannel() {
	Ptr<UniformRandomVariable> uv = CreateObject<UniformRandomVariable>();
	uv->SetAttribute ("Min", DoubleValue (1));
	uv->SetAttribute ("Max", DoubleValue (MAX_CHANNELS));
	int channel=uv->GetInteger();
	if (channel >= MAX_CHANNELS)
		channel = MAX_CHANNELS-1;
	return channel;
}

// Switchable Interface Implementation END


}
