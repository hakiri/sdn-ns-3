#!/bin/bash
#==============================================================================
#title           : install.sh
#description     : This script will install OpenNet
#                  Support Ubuntu 14.04.1, CentOS 7, Fedora 21
#==============================================================================

set -o nounset
set -e

ROOT_PATH=`pwd -P`
OVS_VERSION='2.4.0'
MININET_VERSION='2.2.1'
NS3_VERSION='3.24'
PYGCCXML_VERSION='1.0.0'
NETANIM_VERSION='3.106'
DIST=Unknown
RELEASE=Unknown
CODENAME=Unknown
CORE_VERSION='4.8'
#function detect_env {
	# Attempt to identify Linux release

DIST=Unknown
RELEASE=Unknown
CODENAME=Unknown
ARCH=`uname -m`
if [ "$ARCH" = "x86_64" ]; then ARCH="amd64"; fi
if [ "$ARCH" = "i686" ]; then ARCH="i386"; fi

test -e /etc/debian_version && DIST="Debian"
grep Ubuntu /etc/lsb-release &> /dev/null && DIST="Ubuntu"
if [ "$DIST" = "Ubuntu" ] || [ "$DIST" = "Debian" ]; then
    install='sudo apt-get -y install'
    remove='sudo apt-get -y remove'
    pkginst='sudo dpkg -i'
    # Prereqs for this script
    if ! which lsb_release &> /dev/null; then
        $install lsb-release
    fi
fi
test -e /etc/fedora-release && DIST="Fedora"
if [ "$DIST" = "Fedora" ]; then
    install='sudo yum -y install'
    remove='sudo yum -y erase'
    pkginst='sudo rpm -ivh'
    # Prereqs for this script
    if ! which lsb_release &> /dev/null; then
        $install redhat-lsb-core
    fi
fi
if which lsb_release &> /dev/null; then
    DIST=`lsb_release -is`
    RELEASE=`lsb_release -rs`
    CODENAME=`lsb_release -cs`
fi
echo "Detected Linux distribution: $DIST $RELEASE $CODENAME $ARCH"

# Kernel params

KERNEL_NAME=`uname -r`
KERNEL_HEADERS=kernel-headers-${KERNEL_NAME}

if ! echo $DIST | egrep 'Ubuntu|Debian|Fedora'; then
    echo "Install.sh currently only supports Ubuntu, Debian and Fedora."
    exit 1
fi

# More distribution info
DIST_LC=`echo $DIST | tr [A-Z] [a-z]` # as lower case
	

# usage: if version_ge 1.20 1.2.3; then echo "true!"; fi
function version_ge {
    # sort -V sorts by *version number*
    latest=`printf "$1\n$2" | sort -V | tail -1`
    # If $1 is latest version, then $1 >= $2
    [ "$1" == "$latest" ]
}


function detect_os {

    test -e /etc/fedora-release && DIST="Fedora"
    test -e /etc/centos-release && DIST="CentOS"
    if [ "$DIST" = "Fedora" ] || [ "$DIST" = "CentOS" ]; then
        install='yum -y install'
        remove='yum -y erase'
        pkginst='rpm -ivh'
        # Prereqs for this script
        if ! which lsb_release &> /dev/null; then
            $install redhat-lsb-core
        fi
    fi
    if which lsb_release &> /dev/null; then
        DIST=`lsb_release -is`
        RELEASE=`lsb_release -rs`
        CODENAME=`lsb_release -cs`
    fi

    grep Ubuntu /etc/lsb-release &> /dev/null && DIST="Ubuntu"
    if [ "$DIST" = "Ubuntu" ] ; then
        install='apt-get -y install'
        remove='apt-get -y remove'
        pkginst='dpkg -i'
        # Prereqs for this script
        if ! which lsb_release &> /dev/null; then
            $install lsb-release
        fi
    fi
    echo "Detected Linux distribution: $DIST $RELEASE $CODENAME"

}

function enviroment {

    echo "Prepare Enviroment"
    if [ "$DIST" = "Fedora" ] || [ "$DIST" = "CentOS" ]; then
        $install make git vim openssh openssh-server unzip curl gcc wget \
        gcc-c++ python python-devel cmake glibc-devel.i686 glibc-devel.x86_64 net-tools \
        make python-devel openssl-devel kernel-devel graphviz kernel-debug-devel \
        autoconf automake rpm-build redhat-rpm-config libtool \
        mercurial qt4 qt4-devel qt-devel qt-config

        SELINUX_STATUS="$(grep SELINUX=disabled /etc/selinux/config)"
        if [ $? -eq 1 ]; then
            sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
            setenforce 0
        fi
        systemctl stop firewalld.service
        systemctl disable firewalld.service
    fi
    if [ "$DIST" = "Ubuntu" ] ; then
        $install gcc g++ python python-dev make cmake gcc-4.8-multilib g++-4.8-multilib \
        python-setuptools unzip curl build-essential debhelper make autoconf automake \
        patch dpkg-dev libssl-dev libncurses5-dev libpcre3-dev graphviz python-all \
        python-qt4 python-zopeinterface python-twisted-conch uuid-runtime \
        qt4-dev-tools
    fi
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python

}

function pygccxml {
	rm -rf pygccxml*
    echo "Fetch and install pygccxml"
    cd $ROOT_PATH
    if [ ! -f pygccxml-$PYGCCXML_VERSION.zip ]; then
        wget http://nchc.dl.sourceforge.net/project/pygccxml/pygccxml/pygccxml-1.0/pygccxml-$PYGCCXML_VERSION.zip
    fi
    unzip -o pygccxml-$PYGCCXML_VERSION.zip && cd $ROOT_PATH/pygccxml-$PYGCCXML_VERSION
    python setup.py install

    if [ "$DIST" = "Fedora" ] || [ "$DIST" = "CentOS" ]; then
        sed -e "s/gccxml\_path=''/gccxml\_path='\/usr\/local\/bin'/" -i /usr/lib/python2.7/site-packages/pygccxml/parser/config.py
    fi

    if [ "$DIST" = "Ubuntu" ]; then
        sed -e "s/gccxml_path=''/gccxml_path='\/usr\/local\/bin'/" -i /usr/local/lib/python2.7/dist-packages/pygccxml/parser/config.py
    fi

}

function gccxml {
	rm -rf gccxml*
    echo "Install gccxml"
    cd $ROOT_PATH
    if [ ! -d gccxml ]; then
        git clone https://github.com/gccxml/gccxml.git
    fi
    cd gccxml
    mkdir -p gccxml-build && cd gccxml-build
    cmake ../
    make
    make install
	
	sudo ln -sf /usr/local/bin/gccxml /bin/gccxml
	
	#if [ -L 'ls /bin/gccxml']; then
		#echo "Delete if True if gccxml exists and is a symbolic link"
		#sudo rm /bin/gccxml
	#else
		#echo "Add new symbolic link"
        #sudo ln -s /usr/local/bin/gccxml /bin/gccxml
    #fi

}

function ns3 {

    echo "Fetch ns-$NS3_VERSION"
    cd $ROOT_PATH
    rm -rf  ns-3-allinone
    if wget https://www.nsnam.org/release/ns-allinone-$NS3_VERSION.tar.bz2  2> /dev/null; then    
		tar xf ns-allinone-$NS3_VERSION.tar.bz2
	elif hg clone http://code.nsnam.org/ns-3-allinone  2> /dev/null; then  
        cd ns-3-allinone && ./download.py
    elif hg clone http://code.nsnam.org/bake 2> /dev/null; then  
		./bake.py configure -e ns-3-dev
		./bake.py check
		./bake.py download
	else 
		echo "ns-allinone-$NS3_VERSION not provided"
    fi

}

function netanim {

    echo "Build NetAnim"
    cd $ROOT_PATH/ns-3-allinone/netanim
    qmake-qt4 NetAnim.pro
    make
}

function mininet {
    echo "Installing Mininet dependencies"
    if [ "$DIST" = "Fedora" ]; then
        $install gcc make socat psmisc xterm openssh-clients iperf python-networkx \
            iproute telnet python-setuptools libcgroup-tools gsl-bin libgsl0-dev libgsl0ldbl \
            ethtool help2man pyflakes pylint python-pep8 flex kimwitu cl-yason bison libfl-dev tcpdump \
            libxml2 libxml2-dev sqlite sqlite3 libsqlite3-dev
    else
        $install gcc make socat psmisc xterm ssh iperf iproute telnet \
            python-setuptools cgroup-bin ethtool help2man \
            pyflakes pylint pep8 libxml2 libxml2-dev sqlite sqlite3 libsqlite3-dev \
            flex kimwitu cl-yason bison libfl-dev tcpdump gsl-bin libgsl0-dev libgsl0ldbl python-networkx
    fi

    echo "Fetch dlinknctu/mininet"
    echo "Base on Mininet $MININET_VERSION"
    echo "Default branch: opennet"
    cd $ROOT_PATH
    if [ ! -d mininet ]; then
        git clone --branch opennet https://github.com/dlinknctu/mininet.git
    fi

    echo "Install mininet"
    cd $ROOT_PATH/mininet/
    ./util/install.sh -n

}


function openvswitch {
	
    cd $ROOT_PATH
    DIST=$(lsb_release -i | awk '{print $3}')
    if [ "$DIST" = "Ubuntu" ]; then
        wget http://openvswitch.org/releases/openvswitch-$OVS_VERSION.tar.gz
        tar zxvf openvswitch-$OVS_VERSION.tar.gz && cd openvswitch-$OVS_VERSION
        #TODO Need to integrate *deb
        DEB_BUILD_OPTIONS='parallel=2 nocheck' fakeroot debian/rules binary
        dpkg -i $ROOT_PATH/openvswitch-switch_$OVS_VERSION*.deb $ROOT_PATH/openvswitch-common_$OVS_VERSION*.deb \
                $ROOT_PATH/openvswitch-pki_$OVS_VERSION*.deb
    fi

    if [ "$DIST" = "CentOS" ] || [ "$DIST" = "Fedora" ]; then
        mkdir -p $ROOT_PATH/rpmbuild/SOURCES/ && cd $ROOT_PATH/rpmbuild/SOURCES/
        wget http://openvswitch.org/releases/openvswitch-$OVS_VERSION.tar.gz
        tar zxvf openvswitch-$OVS_VERSION.tar.gz && cd openvswitch-$OVS_VERSION
        rpmbuild -bb --define "_topdir $ROOT_PATH/rpmbuild" --without check rhel/openvswitch.spec
        rpm -ivh --replacepkgs --replacefiles --nodeps $ROOT_PATH/rpmbuild/RPMS/x86_64/openvswitch*.rpm
        /etc/init.d/openvswitch start
    fi

}

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
				python-zopeinterface python-twisted-conch dkms	python-simplejson vtun lxc
		
	## OPTION 1; use Ubuntu packages pre-built packages
	$ install openvswitch-common openvswitch-datapath-dkms openvswitch-datapath-source openvswitch-dbg openvswitch-ipsec \
			  openvswitch-switch openvswitch-test openvswitch-testcontroller openvswitch-vtep python-openvswitch
			  
	## OPTION 2: Build from source code
	cd openvswitch-$OVS_VERSION	
	./configure --with-linux=/lib/modules/`uname -r`/build
	make && make install
	make modules_install
	
	touch /usr/local/etc/ovs-vswitchd.conf
	mkdir -p /usr/local/etc/openvswitch
	sudo rmmod openvswitch
	depmod -a
	
	insmod datapath/linux/openvswitch.ko
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

function remove_ovs {
    pkgs=`dpkg --get-selections | grep openvswitch | awk '{ print $1;}'`
    echo "Removing existing Open vSwitch packages:"
    echo $pkgs
    if ! $remove $pkgs; then
        echo "Not all packages removed correctly"
    fi
    # For some reason this doesn't happen
    if scripts=`ls /etc/init.d/*openvswitch* 2>/dev/null`; then
        echo $scripts
        for s in $scripts; do
            s=$(basename $s)
            echo SCRIPT $s
            sudo service $s stop
            sudo rm -f /etc/init.d/$s
            sudo update-rc.d -f $s remove
        done
    fi
    echo "Done removing OVS"
}

function core {
	rm -rf core-$CORE_VERSION
	CORE_TARBALL_LOC=http://downloads.pf.itd.nrl.navy.mil/core/source/

	DIST=$(lsb_release -i | awk '{print $3}')
	echo $DIST
	if [ "$DIST" = "Ubuntu" ]; then
	install='apt-get -y install'
    remove='apt-get -y erase'
	fi

	echo "Build core from source code"
	
	$install bash bridge-utils ebtables iproute libev-dev python tcl8.5 tk8.5 libtk-img \
				autoconf automake gcc libev-dev make python-dev libreadline-dev pkg-config imagemagick help2man
	
	if wget $CORE_TARBALL_LOC/core-$CORE_VERSION.tar.gz 2> /dev/null; then
				tar xzf core-$CORE_VERSION.tar.gz
		else
			echo "Failed to find CORE at $CORE_TARBALL_LOC/core-$CORE_VERSION.tar.gz"
			cd $ROOT_PATH
				return
	fi
	
		cd core-$CORE_VERSION
		./bootstrap.sh
		./configure
		make
		sudo make install
		echo "Test Core Daemon"
		sudo /etc/init.d/core-daemon start	
	}
	
	
function olsr {
	cd $ROOT_PATH
	rm -rf olsrd/
	echo "Build OLSR from last built source code"
	git clone http://olsr.org/git/olsrd.git
	cd olsrd
	make && make libs
	sudo make install_libs
	cd ..
	}


# Install RYU
function ryu {
	sudo rm -rf ryu
    echo "Installing RYU..."
	
	# install Ryu dependencies"
    $install autoconf automake g++ libtool python make
    if [ "$DIST" = "Ubuntu" ]; then
        $install libxml2 libxslt-dev python-pip python-dev
        sudo pip install gevent
    elif [ "$DIST" = "Debian" ]; then
        $install libxml2 libxslt-dev python-pip python-dev
        sudo pip install gevent
    fi
	echo "if needed, update python-six"
    # if needed, update python-six
    SIX_VER=`pip show six | grep Version | awk '{print $2}'`
    if version_ge 1.7.0 $SIX_VER; then
        echo "Installing python-six version 1.7.0..."
        sudo pip install -I six==1.7.0
    fi
    
    echo "fetch RYU"
    # fetch RYU
    cd $ROOT_PATH/
    git clone git://github.com/osrg/ryu.git ryu
    cd ryu

	echo "install ryu"
    # install ryu
    sudo python ./setup.py install

	
    # Add symbolic link to /usr/bin
    sudo ln -sf ./bin/ryu-manager /usr/local/bin/ryu-manager
}

# "Install" POX
function pox {
	sudo rm -rf pox
    echo "Installing POX into $ROOT_PATH/pox..."
    cd $ROOT_PATH
    git clone https://github.com/noxrepo/pox.git
}

function opennet {
	
    echo "Install OpenNet"
    cd $ROOT_PATH
    echo "Copy files to Mininet directory"
    cp -R $ROOT_PATH/mininet-patch/examples/* $ROOT_PATH/mininet/examples/
    cp -R $ROOT_PATH/mininet-patch/mininet/* $ROOT_PATH/mininet/mininet/

    echo "Re-build mininet"
    cd $ROOT_PATH/mininet/
    ./util/install.sh -n

    echo "Patch NS3"
#    cp $ROOT_PATH/ns3-patch/*.patch $ROOT_PATH/ns-allinone-$NS3_VERSION/ns-$NS3_VERSION
#    cp $ROOT_PATH/ns-3-dev-patch/* $ROOT_PATH/ns-3-allinone/ns-3-dev
    cp $ROOT_PATH/animation-interface.* $ROOT_PATH/ns-3-allinone/ns-3-dev/src/netanim/model
    cp $ROOT_PATH/wscript $ROOT_PATH/ns-3-allinone/ns-3-dev/src/netanim
    cp $ROOT_PATH/sta-wifi-mac.* $ROOT_PATH/ns-3-allinone/ns-3-dev/src/wifi/model
    cp $ROOT_PATH/mac-rx-middle.* $ROOT_PATH/ns-3-allinone/ns-3-dev/src/wifi/model
    cp $ROOT_PATH/mac-low.* $ROOT_PATH/ns-3-allinone/ns-3-dev/src/wifi/model

   cd $ROOT_PATH/ns-3-allinone/ns-3-dev
#   patch -p1 < animation-interface.patch
#   patch -p1 < netanim-python.patch
#    patch -p1 < sta-wifi-scan.patch

    #if [ "$DIST" = "Ubuntu" ]; then
        #sed -e "s/\['network'\]/\['internet', 'network', 'core'\]/" -i src/tap-bridge/wscript
    #fi

#    ./waf configure
    ./waf configure --enable-examples --enable-tests
    ./waf --apiscan=netanim
    ./waf --apiscan=wifi
    ./waf build

}

function core_configure {
	
	echo "Core Configuration"
	
	custom_services_dir = $ROOT_PATH/emulation/core_services
	openvswitch_dir = $ROOT_PATH/openvswitch-$OVS_VERSION
	olsr_dir = $ROOT_PATH/olsrd
	olsrd_dir = $ROOT_PATH/olsrd
	scripts_dir = $ROOT_PATH/scripts
	
	echo "======================================================================="
	echo " Wireless Mesh SDN Installation Complete" 
	echo " Please; prepare NS-3 Waf for compilation"
	echo "======================================================================="
	
	echo "Start new terminal to build the example"
	gnome-terminal -x sh -c '/waf_shell.sh && cd $ROOT_PATH/emulation && core-cleanup.sh && python -i ./ns3SDN.py -d 7200; exec bash'
	echo "Start another new terminal to start emulated nodes"
	gnome-terminal -x sh -c './starthosts.sh && ./startovs.sh; exec bash'
	
	echo "The follwoing commands should run in Core terminal created by the previous command"
	
	#echo " \$ ./waf_shell.sh"
	#echo " \$ cd $ROOT_PATH/emulation"
	#gnome-terminal -x sh -c 'core-cleanup.sh && test2.sh; exec bash'
	#gnome-terminal -x sh -c 'test1.sh && test2.sh; exec bash'
	#x-terminal-emulator core-cleanup.sh 
	#echo "\$ python -i ./ns3SDN.py -d 7200"

	
	}

function waf {

    WAF_SHELL=$ROOT_PATH/waf_shell.sh
    echo "#!/bin/sh" > $WAF_SHELL
    echo "cd $ROOT_PATH/ns-3-allinone-/ns-3-dev/" >> $WAF_SHELL
    echo "./waf shell" >> $WAF_SHELL
    chmod +x $WAF_SHELL

}

function finish {

    echo "======================================================================="
    echo " OpenNet installation complete."
    echo " Before using OpenNet, you need to prepare SDN controller by yourself."
    echo "======================================================================="
    echo " Please try following commands to run the simulation"
    echo " \$ ./waf_shell.sh"
    echo " \$ cd $ROOT_PATH/mininet/examples/opennet"
    echo " \$ python wifiroaming.py"

}

function all {

    detect_os
    enviroment
    pygccxml
    gccxml
    core
    olsr
    ns3
    netanim
    mininet
    openvswitch
    opennet
    ryu
    pox
    waf
    finish

}

function iperf {
	echo "Installing new version of Iperf Traffic Generator"
	sudo apt-get remove iperf3 libiperf0
	wget https://iperf.fr/download/iperf_3.0/libiperf0_3.0.11-1_amd64.deb
	wget https://iperf.fr/download/iperf_3.0/iperf3_3.0.11-1_amd64.deb
	sudo dpkg -i libiperf0_3.0.11-1_amd64.deb iperf3_3.0.11-1_amd64.deb
	rm libiperf0_3.0.11-1_amd64.deb iperf3_3.0.11-1_amd64.deb
	
	}


function usage {

    echo
    echo Usage: $(basename $0) -[$PARA] >&2
    echo "-a: Install OpenNet World"
    echo "-h:  usage"
    echo "-d:  detect_os"
    echo "-e:  enviroment"
    echo "-p:  pygccxml"
    echo "-g:  gccxml"
    echo "-n:  ns3"
    echo "-i:  netanim"
    echo "-m:  mininet"
    echo "-s:  openvswitch"
    echo "-o:  opennet"
    echo "-w:  waf"
    echo "-l:  olsr"
    echo "-r:  remove_ovs"
    echo "-c:  core"
    echo "-y:  ryu"
    echo "-x:  pox"
    echo "-f:  iperf"
	echo "-q: Finish message"
    exit 2

}


PARA='amdhenircylpgxoswf'
if [ $# -eq 0 ]
then
    usage
else
    while getopts $PARA OPTION
    do
        case $OPTION in
        a)  all;;
        h)  usage;;
        d)  detect_os;;
        e)  enviroment;;
        p)  pygccxml;;
        g)  gccxml;;
        n)  ns3;;
        i)  netanim;;
        m)  mininet;;
        s)  openvswitch;;
        o)  opennet;;
        w)  waf;;
        l)  olsr;;
        r)  remove_ovs;;
        c)  core;;
        y)  ryu;;
        x)  pox;;
        f)  iperf;;
        q)  finish;;
        esac
    done
    shift $(($OPTIND - 1))
fi

