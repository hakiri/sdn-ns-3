#! /usr/bin/env python
from __future__ import print_function
import sys
from optparse import OptionParser
import os
import shutil
import urllib
from glob import glob

from util import run_command, fatal, CommandError
import constants
from xml.dom import minidom as dom


def get_ns3(ns3_branch):
    print("""
    #
    # Get NS-3
    #
    """)
    ns3_dir = os.path.split(ns3_branch)[-1]
    ns3_branch_url = constants.NSNAM_CODE_BASE_URL + ns3_branch

    if not os.path.exists(ns3_dir):
        print("Cloning ns-3 branch")
        run_command(['hg', 'clone', ns3_branch_url, ns3_dir])
    else:
        print("Updating ns-3 branch")
        run_command(['hg', '--cwd', ns3_dir, 'pull', '-u'])

    return ns3_dir


def get_pybindgen(ns3_dir):
    print("""
    #
    # Get PyBindGen
    #
    """)

    if sys.platform in ['cygwin']:
        print("Architecture (%s) does not support PyBindGen ... skipping" % (sys.platform,))
        raise RuntimeError

    # (peek into the ns-3 wscript and extract the required pybindgen version)
    ns3_python_wscript = open(os.path.join(ns3_dir, "bindings", "python", "wscript"), "rt")
    required_pybindgen_version = None
    for line in ns3_python_wscript:
        if 'REQUIRED_PYBINDGEN_VERSION' in line:
            required_pybindgen_version = eval(line.split('=')[1].strip())
            ns3_python_wscript.close()
            break
    if required_pybindgen_version is None:
        fatal("Unable to detect pybindgen required version")
    print("Required pybindgen version: ", required_pybindgen_version)

    # work around http_proxy handling bug in bzr
    # if 'http_proxy' in os.environ and 'https_proxy' not in os.environ:
    #     os.environ['https_proxy'] = os.environ['http_proxy']

    if 'post' in required_pybindgen_version:
        # given a version like '0.17.0.post41+ngd10fa60', the last 7 characters
        # are part of a git hash, which should be enough to identify a revision
        rev = required_pybindgen_version[-7:]
    else:
        rev = required_pybindgen_version

    if os.path.exists(constants.LOCAL_PYBINDGEN_PATH):
        print("Trying to update pybindgen; this will fail if no network connection is available.  Hit Ctrl-C to skip.")

        try:
            run_command(["git", "fetch", constants.PYBINDGEN_BRANCH],
                        cwd=constants.LOCAL_PYBINDGEN_PATH)
        except KeyboardInterrupt:
            print("Interrupted; Python bindings will be disabled.")
        else:
            print("Update was successful.")
    else:
        print("Trying to fetch pybindgen; this will fail if no network connection is available.  Hit Ctrl-C to skip.")
        try:
            run_command(["git", "clone", constants.PYBINDGEN_BRANCH,
                        constants.LOCAL_PYBINDGEN_PATH])
        except KeyboardInterrupt:
            print("Interrupted; Python bindings will be disabled.")
            shutil.rmtree(constants.LOCAL_PYBINDGEN_PATH, True)
            return False
        print("Fetch was successful.")

    run_command(["git", "checkout", rev, "-q"],
                cwd=constants.LOCAL_PYBINDGEN_PATH)

    ## This causes the version to be generated
    run_command(["python", "setup.py", "clean"],
                cwd=constants.LOCAL_PYBINDGEN_PATH)

    return (constants.LOCAL_PYBINDGEN_PATH, required_pybindgen_version)


def get_netanim(ns3_dir):
    print("""
    #
    # Get NetAnim
    #
    """)

    if sys.platform in ['cygwin']:
        print("Architecture (%s) does not support NetAnim... skipping" % (sys.platform))
        raise RuntimeError

    # (peek into the ns-3 wscript and extract the required netanim version)
    try:
        # For the recent versions
        netanim_wscript = open(os.path.join(ns3_dir, "src", "netanim", "wscript"), "rt")
    except:
        print("Unable to detect NetAnim required version.Skipping download")
        pass
        return

    required_netanim_version = None
    for line in netanim_wscript:
        if 'NETANIM_RELEASE_NAME' in line:
            required_netanim_version = eval(line.split('=')[1].strip())
            break
    netanim_wscript.close()
    if required_netanim_version is None:
        fatal("Unable to detect NetAnim required version")
    print("Required NetAnim version: ", required_netanim_version)


    def netanim_clone():
        print("Retrieving NetAnim from " + constants.NETANIM_REPO)
        run_command(['hg', 'clone', constants.NETANIM_REPO, constants.LOCAL_NETANIM_PATH])

    def netanim_update():
        print("Pulling NetAnim updates from " + constants.NETANIM_REPO)
        run_command(['hg', '--cwd', constants.LOCAL_NETANIM_PATH, 'pull', '-u', constants.NETANIM_REPO])

    def netanim_download():
        local_file = required_netanim_version + ".tar.bz2"
        remote_file = constants.NETANIM_RELEASE_URL + "/" + local_file
        print("Retrieving NetAnim from " + remote_file)
        urllib.urlretrieve(remote_file, local_file)
        print("Uncompressing " + local_file)
        run_command(["tar", "-xjf", local_file])
        print("Rename %s as %s" % (required_netanim_version, constants.LOCAL_NETANIM_PATH))
        os.rename(required_netanim_version, constants.LOCAL_NETANIM_PATH)

    if not os.path.exists(os.path.join(ns3_dir, '.hg')):
        netanim_download()
    elif not os.path.exists(constants.LOCAL_NETANIM_PATH):
        netanim_clone()
    else:
        netanim_update()

    return (constants.LOCAL_NETANIM_PATH, required_netanim_version)


def get_bake(ns3_dir):
    print("""
    #
    # Get bake
    #
    """)

    def bake_clone():
        print("Retrieving bake from " + constants.BAKE_REPO)
        run_command(['hg', 'clone', constants.BAKE_REPO])
    def bake_download():
        # Bake does not provide download tarballs; clone instead
        bake_clone()

    def bake_update():
        print("Pulling bake updates from " + constants.BAKE_REPO)
        run_command(['hg', '--cwd', 'bake', 'pull', '-u', constants.BAKE_REPO])

    if not os.path.exists(os.path.join(ns3_dir, '.hg')):
        bake_download()
    elif not os.path.exists('bake'):
        bake_clone()
    else:
        bake_update()


def main():
    parser = OptionParser()
    parser.add_option("-n", "--ns3-branch", dest="ns3_branch", default="ns-3-dev",
                      help="Name of the ns-3 repository", metavar="BRANCH_NAME")
    (options, dummy_args) = parser.parse_args()

    # first of all, change to the directory of the script
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    # Create the configuration file
    config = dom.getDOMImplementation().createDocument(None, "config", None)


    # -- download NS-3 --
    ns3_dir = get_ns3(options.ns3_branch)

    ns3_config = config.documentElement.appendChild(config.createElement("ns-3"))
    ns3_config.setAttribute("dir", ns3_dir)
    ns3_config.setAttribute("branch", options.ns3_branch)

    # -- download pybindgen --
    try:
        pybindgen_dir, pybindgen_version = get_pybindgen(ns3_dir)
    except (CommandError, OSError, RuntimeError) as ex:
        print(" *** Did not fetch pybindgen ({}); python bindings will not be available.".format(ex))
    else:
        pybindgen_config = config.documentElement.appendChild(config.createElement("pybindgen"))
        pybindgen_config.setAttribute("dir", pybindgen_dir)
        pybindgen_config.setAttribute("version", pybindgen_version)

    # -- download NetAnim --
    try:
        netanim_dir, netanim_version = get_netanim(ns3_dir)
    except (CommandError, IOError, RuntimeError):
        print(" *** Did not fetch NetAnim offline animator. Please visit http://www.nsnam.org/wiki/index.php/NetAnim .")
    else:
        netanim_config = config.documentElement.appendChild(config.createElement("netanim"))
        netanim_config.setAttribute("dir", netanim_dir)
        netanim_config.setAttribute("version", netanim_version)

    # -- download bake --
    try:
        get_bake(ns3_dir)
    except (CommandError, IOError, RuntimeError):
        print(" *** Did not fetch bake build tool.")
    else:
        bake_config = config.documentElement.appendChild(config.createElement("bake"))
        bake_config.setAttribute("dir", "bake")
        bake_config.setAttribute("version", "bake")

    # write the config to a file
    dot_config = open(".config", "wt")
    config.writexml(dot_config, addindent="    ", newl="\n")
    dot_config.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
