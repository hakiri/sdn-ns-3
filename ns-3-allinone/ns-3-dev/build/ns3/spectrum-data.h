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


#ifndef SPECTRUM_DATA_H
#define SPECTRUM_DATA_H


#include "common-cognitive-header.h"
#include <stdio.h>
#include "ns3/object.h"

// Verbose mode
#define IO_SPECTRUM_DEBUG 1

namespace ns3 {
// Spectrum Entry Information
struct SpectrumEntry  {
	
	// current bandwidth
	double bandwidth;
	
	// Packet Error Rate (PER) value	
	double per;

 };


class SpectrumData : public Object {

	public:
	static TypeId GetTypeId (void);
		// SpectrumData Initializer
		SpectrumData();
		
		// Return the spectrum-entry information for the current channel
		SpectrumEntry GetSpectrumData(int channel);

	private:
		
		// read the current spectrum file, and load the information in the spectrum_table_
		void ReadSpectrumFile(char *fileName);
		
		// Spectrum_table, loaded by the spectrum file
		SpectrumEntry m_spectrumTable_[MAX_CHANNELS];

 };

}
#endif



