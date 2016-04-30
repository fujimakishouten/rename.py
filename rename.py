#!/usr/bin/env python3

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import argparse
import os
import shutil
import sys
import tempfile


# Parse arguments
parser = argparse.ArgumentParser(description="Rename files in directory with sequence number")
parser.add_argument("-c", "--count", type=int, default=1, help="Initial count (Default: 1)")
parser.add_argument("-p", "--prefix", type=str, default="", required=False, help="Prefix")
parser.add_argument("-s", "--suffix", type=str, default="", required=False, help="Suffix")
parser.add_argument("-v", "--verbose", action="store_const", const="verbose", help="Verbose output")
parser.add_argument("-z", "--zfill", type=str, default="auto", help="Pad width (Default: auto)")
parser.add_argument("directory", nargs="?", type=str, default=os.curdir, help="Working directory (Default: .)")
arguments = parser.parse_args()


# Get files in directory
directory = arguments.directory
prefix = arguments.prefix
suffix = arguments.suffix
files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))], key=str)
count = len(files)
padding = len(str(count)) if "auto" == arguments.zfill else int(arguments.zfill)
verbose = False if False == arguments.verbose else True
end = "\033[K\r"


# Rename files
if count:
    if verbose:
        print("Rename {0} files".format(count), end="\033[K\r")
    with tempfile.TemporaryDirectory() as temporary:
        current = 1
        for f in files:
            if verbose:
                print("Move to temporary directory {0}/{1}".format(current, count), end=end)
            shutil.move(os.path.join(directory, f), os.path.join(temporary, f))
            current = current + 1

        current = 1
        counter = arguments.count
        for f in files:
            basename = prefix + str(counter).zfill(padding) + suffix
            extension = "" if -1 == f.find(".") else f.split(".", 1)[1]
            filename = ".".join([basename, extension]) if extension else basename

            if verbose:
                print("File renamed {0}/{1}".format(current, count), end=end)
            shutil.move(os.path.join(temporary, f), os.path.join(directory, filename))
            current = current + 1
            counter = counter + 1

    if verbose:
        print("{0}{1} files renamed".format(end, count))



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
 
