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

#include "spectrum-decision.h"
#include "ns3/random-variable-stream.h"

namespace ns3 {

// Spectrum Decision initializer
SpectrumDecision::SpectrumDecision(SpectrumManager *sm) {

	m_decisionPolicy=DECISION_POLICY_ALWAYS_SWITCH;
	//decision_policy_=DECISION_POLICY_NEVER_SWITCH;

	m_spectrumPolicy=ROUND_ROBIN_SWITCH;

	m_specManager=sm;

}




// DecideSwitch: decide wether to stay or leave the current channel, when a PU is detected
bool
SpectrumDecision::DecideSwitch() {

	double randomValue;
	bool switch_decision;

	Ptr<UniformRandomVariable> uv = CreateObject<UniformRandomVariable>();
	switch(m_decisionPolicy) {

	// Switch with probability equal to THRESHOLD_SWITCH, stay otherwise
	case DECISION_POLICY_PROBABILISTIC_SWITCH:

		randomValue = uv->GetValue();

		if (randomValue < THRESHOLD_SWITCH)
			switch_decision=true;
		else
			switch_decision=false;
		break;

		// Switch to a new channel in anycase
	case DECISION_POLICY_ALWAYS_SWITCH:

		switch_decision=true;
		break;

		// Never make a switch
	case DECISION_POLICY_NEVER_SWITCH:

		switch_decision=false;
		break;

	default:

		switch_decision=true;
		break;
	}

	return switch_decision;
}





// DecideSpectrum: get the next spectrum to be used, based on the allocation policy
int
SpectrumDecision::DecideSpectrum(int current_channel) {

	int next_channel;

	Ptr<UniformRandomVariable> uv1 = CreateObject<UniformRandomVariable>();

	switch(m_spectrumPolicy) {

	// Policy RANDOM_SWITCH: next_channel -> random(1..MAX_CHANNELS)
	case RANDOM_SWITCH:
		uv1->SetAttribute ("Min", DoubleValue (2));
		uv1->SetAttribute ("Max", DoubleValue (MAX_CHANNELS));
		next_channel=uv1->GetInteger();

		if (next_channel >= MAX_CHANNELS)
			next_channel = MAX_CHANNELS-1;
		break;

		// Policy ROUND_ROBIN_SWITCH: next channel -> ( next_channel + 1 ) % MAX_CHANNELS
	case ROUND_ROBIN_SWITCH:

		next_channel=(current_channel+1) % MAX_CHANNELS;
		if (next_channel==0) next_channel += 2;
		if (next_channel ==1)
			next_channel++;
		break;

	}

	return next_channel;

}

}

