#!/usr/bin/env python3.7

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import os
import sys
import tempfile
import argparse
import shutil


def extname(name):
    return "" if -1 == name.find(".") else name.split(".", 1)[1]

def rename(directory, start, extension, prefix, suffix, verbose, zfill, dryrun):
    """Rename files in the directory."""
    # Get files in directory
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))], key=str)
    directories = sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))], key=str)
    count = len(files)
    padding = len(str(count)) if "auto" == zfill else int(zfill)
    end = "\033[K\r"

    # Dry run
    if dryrun:
        print(os.path.abspath(directory).split("/")[-1])
        for i, f in enumerate(files):
            basename = prefix + str(start + i).zfill(padding) + suffix
            ext = extname(f) if None == extension else extension
            filename = ".".join([basename, ext]) if ext else basename

            print("{0} => {1}".format(f, filename))
        print()
        sys.exit(0)


    # Rename files
    if count:
        if verbose:
            print("Rename {0} files".format(count), end=end)
        with tempfile.TemporaryDirectory() as temporary:
            current = 1
            for f in files:
                if verbose:
                    print('"{0}" Move to temporary directory {1}/{2}'.format(os.path.abspath(directory).split("/")[-1], current, count), end=end)
                shutil.move(os.path.join(directory, f), os.path.join(temporary, f))
                current = current + 1

            current = 1
            counter = start
            for f in files:
                basename = prefix + str(counter).zfill(padding) + suffix
                ext = extname(f) if None == extension else extension
                filename = ".".join([basename, ext]) if ext else basename

                if verbose:
                    print('"{0}" file renamed {1}/{2}'.format(os.path.abspath(directory).split("/")[-1], current, count), end=end)
                shutil.move(os.path.join(temporary, f), os.path.join(directory, filename))
                current = current + 1
                counter = counter + 1

        if verbose:
            print("", end=end)
            print('"{0}" {1} files renamed'.format(os.path.abspath(directory).split("/")[-1], count))


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Rename files in directory with sequence number")
    parser.add_argument("-c", "--count", type=int, default=1, help="Initial count (Default: 1)")
    parser.add_argument("-d", "--dryrun", action="store_true", help="Dry run")
    parser.add_argument("-e", "--extension", type=str, required=False, help="Overwrite extension with")
    parser.add_argument("-p", "--prefix", type=str, default="", required=False, help="Prefix")
    parser.add_argument("-s", "--suffix", type=str, default="", required=False, help="Suffix")
    parser.add_argument("-v", "--verbose", action="store_const", const="verbose", help="Verbose output")
    parser.add_argument("-z", "--zfill", type=str, default="auto", help="Pad width (Default: auto)")
    parser.add_argument("directory", nargs="?", type=str, default=os.curdir, help="Working directory (Default: .)")
    arguments = parser.parse_args()

    # Get arguments
    directory = arguments.directory
    start = arguments.count
    extension = arguments.extension
    prefix = arguments.prefix
    suffix = arguments.suffix
    verbose = False if False == arguments.verbose else True
    zfill = arguments.zfill
    dryrun = arguments.dryrun

    # Execute rename
    rename(directory, start, extension, prefix, suffix, verbose, zfill, dryrun)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

