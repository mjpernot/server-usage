# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in server_usage.py.

    Usage:
        test/integration/server_usage/run_program.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mongo
        test_print_format
        test_no_print
        test_print_raw
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/server_usage"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("configuration", self.config_path)
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-c": "configuration", "-d": self.config_path}
        self.args2.args_array = {
            "-c": "configuration", "-d": self.config_path, "-n": True,
            "-m": True}
        svr = mongo_libs.create_instance(
            "configuration", self.config_path, mongo_class.Server)
        svr.connect()

        if self.cfg.db in svr.fetch_dbs():
            print("ERROR:  Test environment not clean - database: %s exists"
                  % (self.cfg.db))
            mongo_libs.disconnect([svr])
            self.skipTest("Pre-conditions not met.")

        mongo_libs.disconnect([svr])

    def test_mongo(self):

        """Function:  test_mongo

        Description:  Test inserting data into Mongo database.

        Arguments:

        """

        server_usage.run_program(self.args2)

        coll = mongo_libs.crt_coll_inst(self.cfg, self.cfg.db, self.cfg.coll)
        coll.connect()

        self.assertTrue(coll.coll_cnt() == 1)

    def test_print_format(self):

        """Function:  test_print_format

        Description:  Test printing formatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.run_program(self.args))

    def test_no_print(self):

        """Function:  test_no_print

        Description:  Test standard out suppression.

        Arguments:

        """

        self.args.args_array["-n"] = True

        self.assertFalse(server_usage.run_program(self.args))

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test printing unformatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.run_program(self.args))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        mongo = mongo_libs.create_instance(
            "configuration", self.config_path, mongo_class.DB)
        mongo.db_connect(self.cfg.db)
        mongo.db_cmd("dropDatabase")
        mongo_libs.disconnect([mongo])


if __name__ == "__main__":
    unittest.main()
