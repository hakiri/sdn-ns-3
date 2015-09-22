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

#include "spectrum-data.h"


namespace ns3 {

TypeId
SpectrumData::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::SpectrumData")
    .SetParent<Object> ()
    .AddConstructor<SpectrumData> ()
  ;
  return tid;
}



// SpectrumData initializer
SpectrumData::SpectrumData()  {

}



// ReadSpectrumFile: load the information form the spectrum file into the spectrum_table_
void
SpectrumData::ReadSpectrumFile(char *fileName) {
	
	FILE* fd;	
	
	fd=fopen(fileName,"rt");	
	
	if (IO_SPECTRUM_DEBUG) 
		printf("Reading PU Data from File: %s \n", fileName);
	

	if (fd==NULL) {
		printf(" ERROR. Can't open file %s \n",fileName);
		exit(0);
	}


	// For each channel in the range [0: MAX_CHANNELS]
	// the spectrum file contains these entries:
	// - bandwidth (b/s)
	// - packet error rate 
	
	for (int i=0; i<MAX_CHANNELS; i++)  {
		
		int channel;
		float bandwidth;
		float per;
	
		// read the next entry
		fscanf(fd,"%d %f %f",&channel,&bandwidth,&per);
		
		if (ferror(fd)) {
			printf(" ERROR. Can't read Spectrum Information from file %s \n", fileName);		
			exit(0);
		}


		if (IO_SPECTRUM_DEBUG)
			printf("[READING SPECTRUM FILE] #CHANNEL: %d #BANDWIDTH: %f PER: %f\n",channel, bandwidth, per); 
	
		// save the information in the spectrum_table_
		m_spectrumTable_[channel].bandwidth=bandwidth;
		m_spectrumTable_[channel].per=per;
	 }
	
	 fclose(fd);
}




// GetSpectrumData: return the spectrum_entry for the current channel
SpectrumEntry 
SpectrumData::GetSpectrumData(int channel) {

	if ((channel>=0) && (channel <MAX_CHANNELS)) 
		return m_spectrumTable_[channel];

	else  {
		printf(" ERROR. Can't retrive Spectrum Information for channel %d \n", channel);		
		exit(0);
	
	 }
	
}

}
