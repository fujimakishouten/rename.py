#!/usr/bin/env python3

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import argparse
import os
import shutil
import sys
import tempfile


# Parse arguments
parser = argparse.ArgumentParser(description="Rename files in directory with sequence number")
parser.add_argument("-s", "--start", type=int, default=1, help="Start number (Default: 1)")
parser.add_argument("-z", "--zfill", type=str, default="auto", help="Pad width (Default: auto)")
parser.add_argument("directory", nargs="?", type=str, default=os.curdir, help="Working directory (Default: .)")
arguments = parser.parse_args()


# Get files in directory
directory = arguments.directory
files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))], key=str)
count = len(files)
padding = len(str(count)) if "auto" == arguments.zfill else int(arguments.zfill)


# Rename files
with tempfile.TemporaryDirectory() as temporary:
    for f in files:
        shutil.move(os.path.join(directory, f), os.path.join(temporary, f))

    counter = arguments.start
    for f in files:
        basename = str(counter).zfill(padding)
        extension = "" if -1 == f.find(".") else f.split(".", 1)[1]
        filename = ".".join([basename, extension])
        counter = counter + 1

        shutil.move(os.path.join(temporary, f), os.path.join(directory, filename))



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
 
