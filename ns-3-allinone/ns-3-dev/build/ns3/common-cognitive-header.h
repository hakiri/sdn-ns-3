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

// Common header for cognitive radio functions

#ifndef common_cognitive_H
#define common_cognitive_H

// Max number of nodes in the simulation
#define MAX_NODES		 	200

// Multi-radio multi-channel specification
// Channels/Radio Definition. DO NOT MODIFY HERE!

// Interface Classification
#define CONTROL_RADIO 		0
#define TRANSMITTER_RADIO 	1
#define RECEIVER_RADIO  	2

// Channe/Radio Information
#define MAX_RADIO	3
#define	MAX_CHANNELS 	11 //#modify to accomodate changes (he says dont modify, why ?)

#define SENSING_VERBOSE_MODE

#endif
