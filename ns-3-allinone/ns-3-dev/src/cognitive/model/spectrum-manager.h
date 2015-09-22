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

/*
 * Implementation of the spectrum management activities performed by CRs
 * Includes:
 * 1. Spectrum sensing:      PU detection through Carrier Sensing Detection
 * 2. Spectrum decision:     Decision of the next-channel to be used in case of PU detection
 * 3. Spectrum mobility:     Handoff Managment    
 * 4. Spectrum data loader:  Loader of spectrum information
 * 5. Spectrum timers:       Timers for spectrum management (handoff/sensing/transmitting/...) 
 */

#ifndef SPECTRUM_MANAGER_H
#define SPECTRUM_MANAGER_H

#include "spectrum-sensing.h"
#include "spectrum-decision.h"
#include "spectrum-data.h"

#include "pu-model.h"
#include "repository.h"
#include "ns3/regular-wifi-mac.h"
#include "ns3/nstime.h"

// Spectrum Manager modules
// Enable/Disable channel allocation performed at MAC Layer, by the SpectrumDecision Module
// Comment this line if channel allocation is performed by the routing agent 
#define CHANNEL_DECISION_MAC_LAYER

// Enable/Disable Notifications MAC->NET layers, in case of PU detection on the current channel
#define ENABLE_SPECTRUM_HANDOFF_NOTIFICATION


namespace ns3 {

// Other classes
class SpectrumSensing;
class SpectrumDecision;
class SpectrumMobility;
class HandoffTimer;
class SenseTimer;
class TransmitTimer;
class RegularWifiMac;

/**
 * \brief APIs for Cognitive Radio extension
 *
 * This class can helps put together all cognitive
 * radio exposed functions (APIs) in one class.
 * A researcher must instantiate this class in the run script
 * and use a reference to it whenever it wants to call any of the
 * cognitive radio functions from any given network layer.
 */
class SpectrumManager  {

	friend class SenseTimer;
	friend class TransmitTimer;

public:

  /**
   * \param mac the mac of the RX interface. This will be used for the cognitive cycle
   * \param id the node id
   *
   * Spectrum Manager initializer
   */
	SpectrumManager(Ptr<RegularWifiMac> mac, int id);

	/**
	 * \param mac the mac of the RX interface. This will be used for the cognitive cycle
	 * \param phy the PHY of the RX interface. This will be used for the cognitive cycle
	 * \param id the node id (integer)
	 * \param sense_time the duration of the sensing time
	 * \param transmit_time the duration of the transmission time
	 *
	 * Spectrum Manager initializer
	 */
	SpectrumManager(Ptr<RegularWifiMac> mac, Ptr<WifiPhy> phy,
	    int id, Time sense_time, Time transmit_time);

	virtual ~SpectrumManager ();


	/**
	 * Start the sensing/handoff/transmission cycle on the RX iface.
	 */
	void Start();

	/**
	 * \returns true if CR is not sensing or performing hand off.
	 */
	bool IsChannelAvailable();

	/**
	 * \returns true if PU is active while receiving the packet, on the current listening channel.
	 */
	bool IsPuInterfering(Time txDuration);

	/**
	 * Callback for when sensing is finished by the PHY layer
	 */
	void SenseEnded();

	/**
	 * Callback for when handoff is finished by the PHY layer
	 */
	void HandoffEnded();

	/**
	 * Callback for when the transmission period has ended.
	 * Now we usually start sensing
	 */
	void TransmitEnded();

	/**
	 * \param prob Probability of mis-detecting the PU. Set to zero for 100% reliability
	 * \param p a reference to the PUModel
	 *
	 * Sets the PU model and probability of misdetection in the spectrum manager
	 */
	void SetPuModel(double prob, Ptr<PUModel> p);

	/**
	 * \param rep a reference to the global repository
	 *
	 * Sets the reference the global repository that is shared among all nodes
	 */
	void SetRepository(Ptr<Repository> rep);

private:

	// Spectrum Cycle Timers and Variables
	// Sensing interval
	Time m_senseTime;
	// Transmitting interval
	Time m_transmitTime;

	// State Variables
	// pu_on_ is true wheter PU activity is detected in the current sensing cycle
	bool m_isPuOn;
	// sensing_ is true wheter a CR is performing sensing
	bool m_isSensing;
	// switching
	bool m_isSwitching;


	// MAC References and address
	Ptr<RegularWifiMac> m_wifiMac;
	int m_nodeId;
  // WifiPhy reference
  Ptr<WifiPhy> m_wifiPhy;

	// Modules
	// Cross-layer repository for information sharing about the current channel
	Ptr<Repository> m_repository;

	// Spectrum Sensing Module
	SpectrumSensing  *m_sensingMod;
	// Spectrum Decision Module
	SpectrumDecision *m_decisionMod;

};
}
#endif


