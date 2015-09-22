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

#ifndef SPECTRUM_SENSING_H
#define SPECTRUM_SENSING_H

//#include <mobilenode.h>

#include "pu-model.h"
#include "spectrum-manager.h"
#include "ns3/node-container.h"
#include "ns3/log.h"

namespace ns3 {
class SpectrumManager;

// Implementation of the Spectrum Sensing activity performed by CRs
class SpectrumSensing {
	
	public:
		
		// Initialitation method: PUmodel off
		SpectrumSensing(SpectrumManager *sm);

		// Initialization method: PUmodel on
		SpectrumSensing(SpectrumManager *sm, double prob, Ptr<PUModel> p);
	
		// Perform sensing and return true if PU activity is detected on the current channel
		bool GetSenseResultsFuture(int id, Time sense_time, Time transmit_time, int channel);

	
	private:
		
		// Primary User Map and Model
		Ptr<PUModel> m_puModel;
		
		// Spectrum Manager reference
		SpectrumManager *m_specManager;

		// Probability to have false negative detection of PUs.
		double m_probMisdetect;
};

}
#endif
