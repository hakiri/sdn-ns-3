#!/bin/bash

echo "Delete Any older version of Opennet if it exist"
sudo rm -rf ~/OpenNet
echo "Create new folder and pull the git repository"
cd ~/ && git clone https://github.com/dlinknctu/OpenNet.git 
echo "Copy existing files into the directory of OpenNet"
sudo cp ~/Bureau/backup/*.* ~/OpenNet 
echo "Change directory to OpenNet"
cd ~/OpenNet

echo "Print Me if succeed  change directory"
var=$(pwd)
echo "The current working directory $var."

sudo $var/install.sh -a
