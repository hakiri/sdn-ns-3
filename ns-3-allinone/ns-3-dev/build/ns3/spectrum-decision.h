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

// Decision policy, when a PU is detected on the current channel
// Policy 0: Switch to a new channel as soon as a PU is detected
#define DECISION_POLICY_ALWAYS_SWITCH 0
// Policy 1: Switch to a new channel, with probability THRESHOLD_SWITCH
#define DECISION_POLICY_PROBABILISTIC_SWITCH 1
// Policy 2: Never switch!
#define DECISION_POLICY_NEVER_SWITCH 2

// Switching threshold, for policy 1
#define THRESHOLD_SWITCH 	0.8

// Next Spectrum Selection
// Policy 1: next channel -> ( next_channel + 1 ) % MAX_CHANNELS
#define ROUND_ROBIN_SWITCH  	0
// Policy 2: next_channel -> random(1..MAX_CHANNELS)
#define RANDOM_SWITCH		1

#ifndef SPECTRUM_DECISION_H
#define SPECTRUM_DECISION_H

#include "spectrum-manager.h"

namespace ns3 {
class SpectrumManager;

// Spectrum Decision module: decide the next channel when a PU is detected on the current one
class SpectrumDecision : public Object {

	public:

		// Spectrum Decision Initializer
		SpectrumDecision(SpectrumManager *sm);
	
		// Decide wheter to stay on the current channel or switch to a new channel
		bool DecideSwitch();		
		
		// Get the next channel to be used, based on the allocation policy	
		int DecideSpectrum(int current_channel);		
	
	private:
		
		// Decision policy: stay or leave the current channel
		int m_decisionPolicy;
		
		// Switching policy: decide the next channel to be used
		int m_spectrumPolicy;
		
		// Spectrum Manager reference
		SpectrumManager *m_specManager;
};

}
#endif
