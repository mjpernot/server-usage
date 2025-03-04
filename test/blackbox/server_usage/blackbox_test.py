#!/usr/bin/python
# Classification (U)

"""Program:  blackbox_test.py

    Description:  Blackbox testing of server_usage.py program.

    Usage:
        test/blackbox/server_usage/blackbox_test.py test_option other_arguments

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import os
import sys
import json

# Local
sys.path.append(os.getcwd())
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def file_check(out_file, search_list, json_fmt=False):

    """Function:  file_check

    Description:  Check the contents of the output file based on the items in
        the search_list variable and check to see if file is in JSON format.

    Arguments:
        (input) out_file -> Path and file name of output file.
        (input) search_list -> List of items to be checked for in output file.
        (input) json_fmt -> True|False -> Output file is in JSON format.
        (output) status -> True|False - Status of checks.

    """

    status = True

    if os.path.isfile(out_file):
        with open(out_file, mode="r", encoding="UTF-8") as fhldr:
            data = fhldr.read()

        for item in search_list:

            if item not in data:
                status = False
                print(f"\t\tError:  {item} not present in {out_file}")

        if json_fmt:
            try:
                _ = json.loads(json.dumps(data))

            except:                                     # pylint:disable=W0702
                status = False
                print(f"\t\tError:  {out_file} is not in JSON format")

        os.remove(out_file)

    else:
        status = False
        print(f"\t\tError:  {out_file} is not present")

    return status


def main():

    """Function:  main

    Description:  Control the blackbox testing of server_usage.py program.

    Variables:
        base_dir -> Directory path to blackbox testing directory.
        out_file -> Path and file name of output file.
        search_list -> List of items to be checked for in output file.
        status -> True|False - Status of checks.

    Arguments:

    """

    search_list = ["servername", "datetime", "mem_used", "tot_mem"]
    option = sys.argv[1]

    if option == "stdout":
        out_file = sys.argv[2]
        status = file_check(out_file, search_list)

    elif option == "json":
        out_file = sys.argv[2]
        status = file_check(out_file, search_list, json_fmt=True)

    else:
        print(f"\n\tWarning:  Unknown test option:  {option}")
        sys.exit()

    if status:
        print("\n\tTest Successful")

    else:
        print("\n\tTest Failure")


if __name__ == "__main__":
    sys.exit(main())
