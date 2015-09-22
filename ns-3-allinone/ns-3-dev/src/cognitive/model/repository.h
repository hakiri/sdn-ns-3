// Switchable Interface Implementation START
// @author:  Marco Di Felice	

#ifndef repository_H
#define repository_H


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "common-cognitive-header.h"
#include "ns3/object.h"
#include "ns3/core-module.h"
#include "ns3/tag.h"
#include "ns3/log.h"


namespace ns3 {

// Channel Entry for receiver nodes
struct RepositoryEntryRecv {
	// receiving channel
	int rxChannel;
};



// Channel Entry for sender nodes
struct RepositoryEntrySend {
	//Flag indicating wheter the channel is used for transmitting
	bool active;
	//Last time the channel was used
	double time;
};



// Cross-Layer Repository class
class Repository : public Object
{

public:
	static TypeId GetTypeId (void);
	// Initializer
	Repository();

	// Set/Get Function for the Receiver Channel Table
	int GetRxChannel(int node);
	void SetRxChannel(int node, int channel);

	// Set/Get Function for the Sender Channel Table
	void UpdateTxChannel(int node, int channel, double time);


private:

	// Receiver Channel table: m_repositoryTable[i] contains the channels used for receiving by node i
	RepositoryEntryRecv m_repositoryTable[MAX_NODES];
	// Sender Channel table: repository_table_sender[i][j] contains the information (active/time) for sending node i and channel j
	RepositoryEntrySend m_repositoryTableSender[MAX_NODES][MAX_CHANNELS];
	// Returns a random channel between 1 and MAX_CHANNELS
	int GetRandomChannel();

};

// Switchable Interface Implementation END
}
#endif

