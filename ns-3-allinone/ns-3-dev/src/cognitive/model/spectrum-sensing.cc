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

#include "spectrum-sensing.h"
#include "ns3/mobility-model.h"

NS_LOG_COMPONENT_DEFINE ("CogSpectrumSensing");

namespace ns3 {
// SpectrumSensing initialization: PU model off
SpectrumSensing::SpectrumSensing(SpectrumManager *sm) {
 	
	m_specManager=sm;
}




// SpectrumSensing initialization: PU model on
SpectrumSensing::SpectrumSensing(SpectrumManager *sm, double prob_misdetect, Ptr<PUModel> p) {
	
	m_puModel=p;

	m_probMisdetect=prob_misdetect;

}               




// sense: return true if PU activity is detected in the time interval [current_time:current_time + sense_time]
bool
SpectrumSensing::GetSenseResultsFuture(int id, Time sense_time, Time transmit_time, int channel) {
	
	NodeContainer const & n = NodeContainer::GetGlobal ();
	Ptr<Node> node = n.Get(id);
	Ptr<MobilityModel> mm = node->GetObject<MobilityModel>();
  double x = mm->GetPosition().x;
	double y = mm->GetPosition().y;
	bool cr_on=false;
	NS_LOG_DEBUG ("POSITIONS: x:" << x << " and y:" << y);

	if (m_puModel) {

		Ptr<UniformRandomVariable> uv = CreateObject<UniformRandomVariable>();
		double randomValue = uv->GetValue(); //by default, min 0 and max 1
		// Ask the PUmodel if a PU is active  in the time interval [current_time:current_time + sense_time]
		cr_on=m_puModel->IsPuActive(Simulator::Now(),sense_time,x,y, channel);
		// Apply the probability of false negative detection
		if ((randomValue < m_probMisdetect) and cr_on)
			cr_on=false;

	}
//#ifdef SENSING_VERBOSE_MODE
//	printf("[SENSING-DBG] Node %d sensed pu activity on channel %d at time %f\n", id, channel, Scheduler::instance().clock());
//#endif
	return cr_on;	
		
}

}


		

