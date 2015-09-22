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

#include "pu-model.h"

NS_LOG_COMPONENT_DEFINE ("CogPUModel");

// PU model class
// Implementation of the model of PU activity for CRAHNs

namespace ns3 {

TypeId
PUModel::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PUModel")
    .SetParent<Object> ()
    .AddConstructor<PUModel> ()
  ;
  return tid;
}


// PUmodel Initializer
PUModel::PUModel() {
	m_numberPus_=0;
}

// ReadData: Read the content of the current pu map file and saves the information on the PU data structure
void
PUModel::ReadData(char* dir) {

	FILE* fd;	
	
	fd=fopen(dir,"rt");

	NS_LOG_DEBUG ("Reading PU Data from File: " << dir);
	

	if (fd==NULL) {
		NS_FATAL_ERROR("Can't open file " << dir);
	}
	
	// The first line contains the following entry:
	// <# number_of_PU>
	fscanf(fd,"%d",&m_numberPus_);

	if (ferror(fd)) {
		NS_FATAL_ERROR ("Can't read PU number Information from file " << dir);
	}


	if (IO_DEBUG)
		NS_LOG_DEBUG ("[READING MAP FILE] #PU users: " << m_numberPus_);

	
	if (m_numberPus_>	 MAX_PU_USERS)
	  NS_LOG_ERROR ("Too many PU in the file. Max allowed is " << MAX_PU_USERS);
	
	// The second section contains the following entry:
	// <PU_id, x_loc, y_loc, x_loc_receiver, y_loc_receiver, alpha, beta, tx_range>

	for (int i=0; i< m_numberPus_; i++) {
		int channel;
		float x,y,x2,y2;
		float alpha, beta;
		float range;		
	
		fscanf(fd,"%d %f %f %f %f %e %e %f",&channel,&x,&y,&x2,&y2,&alpha,&beta,&range);
		
		if (ferror(fd))
			NS_LOG_ERROR ("Can't read PU number Information from file " << dir);


		NS_LOG_DEBUG ("[READING MAP FILE] #PU Location: channel: " << channel << " x="
		    << x << " y=" << y << " #PU Receiver: x=" << x2 << " y=" << y2 << " ALPHA: "
		    << alpha << " BETA: " << beta << " TX RANGE: " << range );


		m_puData[i].main_channel=channel;
		m_puData[i].x_loc=x;
		m_puData[i].y_loc=y;
		m_puData[i].x_loc_receiver=x2;
		m_puData[i].y_loc_receiver=y2;
		m_puData[i].alpha=alpha;
		m_puData[i].beta=beta;
		m_puData[i].radius=range;
		m_puData[i].interference=0.0;
	}


	
	// The third section contains the following entry:
	// <arrival_PU_0, ..,arrival_PU_n>
	// <departure_PU_0, ..,departure_PU_n>
	
	for (int j=0; j< m_numberPus_; j++) {
		int arrivals=0;
		int departures=0;
		int number=0;
		
		fscanf(fd,"%d",&number);

		if (ferror(fd))
			NS_LOG_ERROR ("Can't read PU number DATA Information from file " << dir);

		NS_LOG_DEBUG ("[READING MAP FILE] #PU ON times: " << number);
	
		if (number>MAX_PU_DATA_ENTRY)
			NS_FATAL_ERROR("Too many PU DATA ON times in the file. Max allowed is " << MAX_PU_DATA_ENTRY << " " << number);
		
		m_puData[j].number_data=number;

		for (int i=0; i< (2*number); i++) {
			float time;
			fscanf(fd," %f ",&time);
			if (i%2==0) {		
				// Reading the arrival time			
				m_puData[j].arrival_time[arrivals]=Seconds(time);
				arrivals++;
				NS_LOG_DEBUG ("[READING MAP FILE] #PU arrival: " << j << " " << time);
			} else {
				// Reading the departure time
				m_puData[j].departure_time[departures]=Seconds(time);
				departures++;
				NS_LOG_DEBUG ("[READING MAP FILE] #PU departure: " << j << time);


			}			
	
			m_puData[j].detected[arrivals]=false;

		}
	}
}

// is_PU_active: Check if a PU is active in the time interval [timeNow, timeNow + ts]
bool
PUModel::IsPuActive(Time timeNow, Time ts, double x, double y, int channel) {

	bool active=false;

	for (int i=0; i< m_numberPus_; i++) {
		if ((m_puData[i].main_channel==channel) && (Distance(x,y,i) <=m_puData[i].radius))
			active=CheckActive(timeNow,ts,i);

		if (active) {
			return true;
		}
		
	}

	return false;

}





// check:active: Check if a PU is transmitting in the interval [timeNow, timeNow + ts]
bool
PUModel::CheckActive(Time timeNow, Time ts, int channel) {

	Time endTime=timeNow+ts;
	int number=m_puData[channel].number_data;
	double active=false;

	for (int i=0; i<number; i++) {

		// Check if there is an overlapping with the current PU activity	
		if( (m_puData[channel].arrival_time[i]>=timeNow && m_puData[channel].departure_time[i]>=endTime && m_puData[channel].arrival_time[i]<=endTime) || (m_puData[channel].arrival_time[i]<=timeNow && m_puData[channel].departure_time[i]>=endTime) ||
    (m_puData[channel].arrival_time[i]<=timeNow && m_puData[channel].departure_time[i]>=timeNow && m_puData[channel].departure_time[i]<=endTime)) {

			active=true;
			m_puData[channel].detected[i]=true;

	 	}

		// If there is on overlapping, then jump out from the cycle
		if (active || m_puData[channel].arrival_time[i]>endTime) 
        	              i=number; 
	}
	
	return(active);

}



/*
 * this function checks if PU is active in a time period. This is useful for our TFRC implementation
 * where we assume that the database returns only PUs that are affecting the chain
 */
bool
PUModel::CheckActive(Time timeNow, Time ts) {


	Time endTime=timeNow+ts;
	double active=false;

	for (int j=0; j<m_numberPus_; j++) {
		for (int i=0; i<m_puData[j].number_data; i++) {

			// Check if there is an overlapping with the current PU activity
			if( (m_puData[j].arrival_time[i]>=timeNow && m_puData[j].departure_time[i]>=endTime && m_puData[j].arrival_time[i]<=endTime) || (m_puData[j].arrival_time[i]<=timeNow && m_puData[j].departure_time[i]>=endTime) ||
					(m_puData[j].arrival_time[i]<=timeNow && m_puData[j].departure_time[i]>=timeNow && m_puData[j].departure_time[i]<=endTime)) {

				active=true;
				m_puData[j].detected[i]=true;

			}

			// If there is on overlapping, then jump out from the cycle
			if (active) {
				i=m_puData[j].number_data;
				j=m_numberPus_;
			}
			if (m_puData[j].arrival_time[i]>endTime) {
				i=m_puData[j].number_data;
			}
		}
	}

	return(active);

}

/*
 * Get the next time the PU goes off.
 * This is needed for our TFRC protocol so that it can start sending immediately at this time
 * returns -1 if there is no PU currently
 */
Time
PUModel::GetNextOffTime(Time timeNow) {


	Time endTime=timeNow+Seconds(0.001);
	bool active=false;
	Time timeOff = Seconds(0);

	for (int j=0; j<m_numberPus_; j++) {
		for (int i=0; i<m_puData[j].number_data; i++) {

			// Check if there is an overlapping with the current PU activity
			if( (m_puData[j].arrival_time[i]>=timeNow && m_puData[j].departure_time[i]>=endTime && m_puData[j].arrival_time[i]<=endTime) || (m_puData[j].arrival_time[i]<=timeNow && m_puData[j].departure_time[i]>=endTime) ||
					(m_puData[j].arrival_time[i]<=timeNow && m_puData[j].departure_time[i]>=timeNow && m_puData[j].departure_time[i]<=endTime)) {

				active=true;
				m_puData[j].detected[i]=true;

			}

			// If there is on overlapping, then jump out from the cycle
			if (active) {
				timeOff = m_puData[j].departure_time[i];
				NS_LOG_DEBUG ("time off: " << m_puData[j].departure_time[i] <<" i="<< i <<" and j="<< j );
				i=m_puData[j].number_data;
				j=m_numberPus_;
			}
			if (m_puData[j].arrival_time[i]>endTime) {
				i=m_puData[j].number_data;
			}
		}
	}

	return(timeOff);

}


/**********************************************************/
/* DISTANCE METHODS
 **********************************************************/

//distance: Return the current distance from the PU transmitter on a given channel
double 
PUModel::Distance(double x, double y, int channel) {
	double dx=(x-m_puData[channel].x_loc)*(x-m_puData[channel].x_loc);
	double dy=(y-m_puData[channel].y_loc)*(y-m_puData[channel].y_loc);
	double dist=std::sqrt((float)(dx+dy));

	return dist;
}




///distance_receiver: Return the current distance from the PU receiver on a given channel 
double 
PUModel::DistanceFromReceiver(double x, double y, int channel) {

	double dx=(x-m_puData[channel].x_loc_receiver)*(x-m_puData[channel].x_loc_receiver);
	double dy=(y-m_puData[channel].y_loc_receiver)*(y-m_puData[channel].y_loc_receiver);
	double dist=std::sqrt((float)(dx+dy));

	return dist;
}

void
PUModel::SetPuMapFile(char * fileName)
{
  ReadData(fileName);
}

}
