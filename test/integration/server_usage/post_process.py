# Classification (U)

"""Program:  post_process.py

    Description:  Integration testing of post_process in server_usage.py.

    Usage:
        test/integration/server_usage/post_process.py

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
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_raw_print
        test_format_print
        test_mongo_insert
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.proc_data = {"pid": 1000, "ppid": 100, "uss_mem": 90}
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args2.args_array = {"-f": True}
        self.args3.args_array = {"-n": True, "-m": True}
        self.base_dir = "test/integration/server_usage"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("configuration", self.config_path)
        svr = mongo_libs.create_instance(
            "configuration", self.config_path, mongo_class.Server)
        svr.connect()

        if self.cfg.db in svr.fetch_dbs():
            print("ERROR:  Test environment not clean - database: %s exists"
                  % (self.cfg.db))
            mongo_libs.disconnect([svr])
            self.skipTest("Pre-conditions not met.")

        mongo_libs.disconnect([svr])

    def test_raw_print(self):

        """Function:  test_raw_print

        Description:  Test with printing unformatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args, self.cfg))

    def test_format_print(self):

        """Function:  test_format_print

        Description:  Test printing formatted data.

        Arguments:

        """

        self.assertFalse(server_usage.post_process({}, self.args2, self.cfg))

    def test_mongo_insert(self):

        """Function:  test_mongo_insert

        Description:  Test inserting data into Mongo database.

        Arguments:

        """

        server_usage.post_process(self.proc_data, self.args3, self.cfg)
        coll = mongo_libs.crt_coll_inst(self.cfg, self.cfg.db, self.cfg.coll)
        coll.connect()

        self.assertTrue(coll.coll_cnt() == 1)

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
