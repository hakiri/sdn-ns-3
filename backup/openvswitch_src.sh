function openvswitch_src {
	
	echo "Build Openvswitch from source code..."
	apt-get update
    cd $ROOT_PATH   
    OVS_SRC=openvswitch-$OVS_VERSION
    OVS_TARBALL_LOC=http://openvswitch.org/releases
	rm -rf openvswitch*
	
	if wget $OVS_TARBALL_LOC/openvswitch-$OVS_VERSION.tar.gz 2> /dev/null; then
			tar xzf openvswitch-$OVS_VERSION.tar.gz
	else
		echo "Failed to find OVS at $OVS_TARBALL_LOC/openvswitch-$OVS_RELEASE.tar.gz"
		cd $ROOT_PATH
		return
	fi
	
	apt-get update
	$install -y git automake autoconf gcc uml-utilities build-essential git pkg-config linux-headers-`uname -r` \
				fakeroot debhelper libtool automake libssl-dev pkg-config bzip2 openssl python-all procps python-qt4 \
				python-zopeinterface python-twisted-conch dkms	
	
	
	## OPTION 1; use Ubuntu packages pre-built packages
	$ install openvswitch-common openvswitch-datapath-dkms openvswitch-datapath-source openvswitch-dbg openvswitch-ipsec \
			  openvswitch-switch openvswitch-test openvswitch-testcontroller openvswitch-vtep python-openvswitch
			  
	## OPTION 2: Build from source code
	cd openvswitch-$OVS_VERSION	
	./configure --with-linux=/lib/modules/`uname -r`/build
	make && make install
	make modules_install
	sudo rmmod openvswitch
	depmod -a
	
	insmod datapath/linux/openvswitch.ko
	
	mkdir -p /usr/local/etc/openvswitch
	ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema
	
	ovsdb-server -v --remote=punix:/usr/local/var/run/openvswitch/db.sock \
                     --remote=db:Open_vSwitch,manager_options \
                     --private-key=db:SSL,private_key \
                     --certificate=db:SSL,certificate \
                     --pidfile --detach --log-file

	
	##Test Openvswitch
	echo "Test Openvswtch"
	# FIX ME
	#sudo /etc/init.d/openvswitch-controller stop
	#update-rc.d openvswitch-controller disable	    
    #echo "Start OVS server process:"
    #sudo /etc/init.d/openvswitch-switch start   
    #echo "Once you have finished, you can confirm that you have the latest Open vSwitch installed and the latest kernel module"
    #sudo ovs-vsctl show 
	
	ovs-vsctl --no-wait init
	ovs-vswitchd --pidfile --detach
	ovs-vsctl show
	
	
	}




