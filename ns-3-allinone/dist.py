#! /usr/bin/env python
from __future__ import print_function
import sys
from optparse import OptionParser
import os
import tarfile
from xml.dom import minidom as dom
from cStringIO import StringIO
import time


def tar_add_tree(tar, srcdir, tgtdir, exclude_dir_cb, exclude_file_cb):
    """
    Add a source tree to an archive while changing name and excluding
    directories/files via callbacks.
    """
    assert len(os.path.sep) == 1
    for (dirpath, dirnames, filenames) in os.walk(srcdir):
        assert dirpath.startswith(srcdir)
        reldirpath = dirpath[len(srcdir)+1:]

        # directories to exclude
        while True:
            for i, dirname in enumerate(dirnames):
                if os.path.islink (os.path.join(dirpath,dirname)):
                    # Add, but do not follow, symbolic links
                    srcpath = os.path.join(dirpath, dirname)
                    tgtpath = os.path.join(tgtdir, reldirpath, dirname)
                    tar.add(srcpath, tgtpath)
                if exclude_dir_cb(reldirpath, dirname):
                    break
            else:
                break
            del dirnames[i]
            
        for filename in filenames:
            if exclude_file_cb(reldirpath, filename):
                continue
            srcpath = os.path.join(dirpath, filename)
            tgtpath = os.path.join(tgtdir, reldirpath, filename)
            #print(srcpath, "=>", tgtpath)
            tar.add(srcpath, tgtpath)
            

def main():
    parser = OptionParser()
    (options, dummy_args) = parser.parse_args()

    # first of all, change to the directory of the script
    os.chdir(os.path.dirname(__file__))


    try:
        dot_config = open(".config", "rt")
    except IOError:
        print("** ERROR: missing .config file; you probably need to run the download.py script first.", file=sys.stderr)
        sys.exit(2)

    config = dom.parse(dot_config)
    dot_config.close()

    ns3_config, = config.getElementsByTagName("ns-3")
    ns3_dir = ns3_config.getAttribute("dir")
    ns3_version = open(os.path.join(ns3_dir, "VERSION"), "rt").readline().strip()
    
    print("NS-3 version: %r" % (ns3_version,))
    dist_dir = "ns-allinone-%s" % ns3_version
    arch_name = "%s.tar.bz2" % dist_dir

    tar = tarfile.open(arch_name, 'w:bz2')


    # Create/add a new .config file with modified dir attributes
    new_config = config.cloneNode(True)


    # add the ns-3 tree
    new_ns3_dir = "ns-%s" % ns3_version
    new_config.getElementsByTagName("ns-3")[0].setAttribute("dir", new_ns3_dir)
    def dir_excl(reldirpath, dirname):
        if dirname[0] == '.':
            return True
        if reldirpath == '' and dirname == 'build':
            return True
        return False
    def file_excl(reldirpath, filename):
        # Retain directories in doc/[manual|tutorial|models]/source/_static/
        if filename == '.hidden':
            return False
        if filename == '.ns3rc':
            return False
        if filename.startswith('.'):
            return True
        if filename.endswith('.pyc') or filename.endswith('.pyo'):
            return True
        if filename.endswith('~'):
            return True
        return False
    print("Adding %s as %s" % (ns3_dir, os.path.join(dist_dir, new_ns3_dir)))
    tar_add_tree(tar, ns3_dir, os.path.join(dist_dir, new_ns3_dir), dir_excl, file_excl)

    # add pybindgen
    pybindgen_dir = config.getElementsByTagName("pybindgen")[0].getAttribute("dir")
    new_pybindgen_dir = "pybindgen-%s" % config.getElementsByTagName("pybindgen")[0].getAttribute("version")
    new_config.getElementsByTagName("pybindgen")[0].setAttribute("dir", new_pybindgen_dir)    
    def dir_excl(reldirpath, dirname):
        if dirname[0] == '.':
            return True
        if reldirpath == '' and dirname == 'build':
            return True
        return False
    def file_excl(reldirpath, filename):
        if filename.startswith('.'):
            return True
        if filename.endswith('.pyc') or filename.endswith('.pyo'):
            return True
        if filename.endswith('~'):
            return True
        return False
    print("Adding %s as %s" % (pybindgen_dir, os.path.join(dist_dir, new_pybindgen_dir)))
    tar_add_tree(tar, pybindgen_dir, os.path.join(dist_dir, new_pybindgen_dir), dir_excl, file_excl)

    # add NetAnim
    netanim_dir = config.getElementsByTagName("netanim")[0].getAttribute("dir");
    new_netanim_dir = config.getElementsByTagName("netanim")[0].getAttribute("version")
    assert new_netanim_dir.startswith("netanim")
    new_config.getElementsByTagName("netanim")[0].setAttribute("dir", new_netanim_dir)
    def dir_excl(reldirpath, dirname):
        if dirname[0] == '.':
            return True
        return False
    def file_excl(reldirpath, filename):
        if filename.startswith('.'):
            return True
        if filename.endswith('~'):
            return True
        return False
    print("Adding %s as %s" % (netanim_dir, os.path.join(dist_dir, new_netanim_dir)))
    tar_add_tree(tar, netanim_dir, os.path.join(dist_dir, new_netanim_dir), dir_excl, file_excl)

    # add bake
    bake_dir = config.getElementsByTagName("bake")[0].getAttribute("dir");
    new_bake_dir = config.getElementsByTagName("bake")[0].getAttribute("version")
    assert new_bake_dir.startswith("bake")
    new_config.getElementsByTagName("bake")[0].setAttribute("dir", new_bake_dir)
    def dir_excl(reldirpath, dirname):
        if dirname[0] == '.':
            return True
        return False
    def file_excl(reldirpath, filename):
        if filename.startswith('.'):
            return True
        if filename.endswith('~'):
            return True
        return False
    print("Adding %s as %s" % (bake_dir, os.path.join(dist_dir, new_bake_dir)))
    tar_add_tree(tar, bake_dir, os.path.join(dist_dir, new_bake_dir), dir_excl, file_excl)

    # add the build script files
    print("Adding the build script files")
    for filename in ["build.py", "constants.py", "util.py", "README"]:
        tar.add(filename, os.path.join(dist_dir, filename))


    # Add the modified .config file
    new_config_file = StringIO()
    new_config.writexml(new_config_file)
    tarinfo = tarfile.TarInfo(os.path.join(dist_dir, ".config"))
    tarinfo.mtime = time.time()
    tarinfo.mode = 0o644
    tarinfo.type = tarfile.REGTYPE
    tarinfo.size = new_config_file.tell()
    new_config_file.seek(0)
    tar.addfile(tarinfo, new_config_file)
    

    tar.close()

    return 0

if __name__ == '__main__':
    sys.exit(main())
