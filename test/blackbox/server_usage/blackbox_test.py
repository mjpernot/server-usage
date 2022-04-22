#!/usr/bin/python
# Classification (U)

"""Program:  blackbox_test.py

    Description:  Blackbox testing of server_usage.py program.

    Usage:
        test/blackbox/server_usage/blackbox_test.py test_option other_arguments

    Arguments:

"""

# Libraries and Global Variables

# Standard
import os
import sys

# Third-party
import json

# Local
sys.path.append(os.getcwd())
import lib.gen_libs as gen_libs
import mongo_lib.mongo_class as mongo_class
import mongo_lib.mongo_libs as mongo_libs
import version

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
        data = open(out_file).read()

        for item in search_list:

            if item not in data:
                status = False
                print("\t\tError:  %s not present in %s" % (item, out_file))

        if json_fmt:
            try:
                _ = json.loads(json.dumps(data))

            except:
                status = False
                print("\t\tError:  %s is not in JSON format" % (out_file))

        os.remove(out_file)

    else:
        status = False
        print("\t\tError:  %s is not present" % (out_file))

    return status


def mongo_check(config_path, config_file):

    """Function:  mongo_check

    Description:  Check the contents of the output file based on the items in
        the search_list variable and check to see if file is in JSON format.

    Arguments:
        (input) config_path -> Path name to configuration file.
        (input) config_file -> Name of configuration file, without .py ext.
        (output) status -> True|False - Status of checks.

    """

    status = True
    cfg = gen_libs.load_module(config_file, config_path)
    coll = mongo_libs.crt_coll_inst(cfg, cfg.db, cfg.coll)
    coll.connect()
    status = coll.coll_cnt() == 1
    mongo = mongo_libs.create_instance(
        config_file, config_path, mongo_class.DB)
    mongo.db_connect(cfg.db)
    mongo.db_cmd("dropDatabase")

    mongo_libs.disconnect([coll, mongo])

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

    cmdline = gen_libs.get_inst(sys)
    base_dir = "test/blackbox/server_usage"
    test_path = os.path.join(os.getcwd(), base_dir)
    config_path = os.path.join(test_path, "config")
    search_list = ["servername", "datetime", "mem_used", "tot_mem"]
    option = cmdline.argv[1]

    if option == "stdout":
        out_file = cmdline.argv[2]
        status = file_check(out_file, search_list)

    elif option == "json":
        out_file = cmdline.argv[2]
        status = file_check(out_file, search_list, json_fmt=True)

    elif option == "mongo":
        status = mongo_check(config_path, "configuration")

    else:
        print("\n\tWarning:  Unknown test option:  %s" % (option))
        sys.exit()

    if status:
        print("\n\tTest Successful")

    else:
        print("\n\tTest Failure")


if __name__ == "__main__":
    sys.exit(main())
