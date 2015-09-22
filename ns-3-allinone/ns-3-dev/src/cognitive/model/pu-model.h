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

// A model for PU activity and CR channel sensing

#ifndef NS_PU_MODEL_H
#define NS_PU_MODEL_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "common-cognitive-header.h"
#include "ns3/object.h"
#include "ns3/nstime.h"
#include "ns3/log.h"


// Constant value for the PU Mapping file
// Max number of PUs 
#define MAX_PU_USERS 		60
// Max number of PU-data entry
#define MAX_PU_DATA_ENTRY  	700
// Debug variable: enable verbose mode
#define IO_DEBUG		1

namespace ns3 {

//PU information
struct PuActivity {
	// channel used for tx
	int main_channel;
	// number of arrival/departure entries
	int number_data;
	// current location
	double x_loc;
	double y_loc;
	// arrival/departure time
	Time arrival_time[MAX_PU_DATA_ENTRY];
	Time departure_time[MAX_PU_DATA_ENTRY];
	bool detected[MAX_PU_DATA_ENTRY];
	// PU receiver location
	double x_loc_receiver;	
	double y_loc_receiver;	
	// PU <alpha-beta> activity description
	double alpha;
	double beta;
	// PU transmitting range
	double radius;
	// Avg. interference caused by CR on the PU receiver
	double interference;
};

class PUModel : public Object {

public:
	static TypeId GetTypeId (void);
	// PUmodel creator
	PUModel();
	// Return true if a PU is transmitting in the same spectrum of the CR
	bool IsPuActive(Time timeNow, Time ts, double x, double y, int channel);
	//Check if PU is active at that time
	bool CheckActive(Time timeNow, Time ts);
	//Get next PU off time
	Time GetNextOffTime(Time timeNow);
	//Set PU map file
	void SetPuMapFile(char * file);

private:

	// Number of PUs in the current scenario
	int m_numberPus_;
	// Data structures with information of PUs
	PuActivity m_puData[MAX_PU_USERS];
	// Method to read data from PU file and save them in the pu_activity data structure
	void ReadData(char * dir);
	// Method to get the distance from the PU transmitter
	double Distance(double x, double y, int channel);
	// Method to get the distance from the PU receiver
	double DistanceFromReceiver(double x, double y, int channel);
	// Method tc check if a PU is transmitting on a given spectrum at a given time
	bool CheckActive(Time timeNow, Time ts, int channel);

};
}
#endif
