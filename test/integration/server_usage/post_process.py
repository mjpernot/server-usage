#!/usr/bin/python
# Classification (U)

"""Program:  post_process.py

    Description:  Integration testing of post_process in server_usage.py.

    Usage:
        test/integration/server_usage/post_process.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import lib.cmds_gen as cmds_gen
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_raw_print -> Test with printing unformatted data.
        test_format_print -> Test printing formatted data.
        test_mongo_insert -> Test inserting data into Mongo database.
        tearDown -> Clean up of integration testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.proc_data = {"pid": 1000, "ppid": 100, "uss_mem": 90}

        self.base_dir = "test/integration/server_usage"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("configuration", self.config_path)

        svr = mongo_class.Server(self.cfg.name, self.cfg.user, self.cfg.passwd,
                                 self.cfg.host, self.cfg.port, self.cfg.auth,
                                 self.cfg.conf_file)
        svr.connect()

        if self.cfg.db in svr.fetch_dbs():
            print("ERROR:  Test environment not clean - database: %s exists"
                  % (self.cfg.db))
            cmds_gen.disconnect([svr])
            self.skipTest("Pre-conditions not met.")

        cmds_gen.disconnect([svr])

    def test_raw_print(self):

        """Function:  test_raw_print

        Description:  Test with printing unformatted data.

        Arguments:
            None

        """

        args_array = {}

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.post_process(self.proc_data,
                                                       args_array, self.cfg))

    def test_format_print(self):

        """Function:  test_format_print

        Description:  Test printing formatted data.

        Arguments:
            None

        """

        args_array = {"-f": True}

        self.assertFalse(server_usage.post_process({}, args_array, self.cfg))

    def test_mongo_insert(self):

        """Function:  test_mongo_insert

        Description:  Test inserting data into Mongo database.

        Arguments:
            None

        """

        args_array = {"-n": True, "-m": True}

        server_usage.post_process(self.proc_data, args_array, self.cfg)

        coll = mongo_libs.crt_coll_inst(self.cfg, self.cfg.db, self.cfg.coll)
        coll.connect()

        if coll.coll_cnt() == 1:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        db = mongo_class.DB(self.cfg.name, self.cfg.user, self.cfg.passwd,
                            self.cfg.host, self.cfg.port, self.cfg.db,
                            self.cfg.auth, self.cfg.conf_file)

        db.db_connect(self.cfg.db)
        db.db_cmd("dropDatabase")
        cmds_gen.disconnect([db])


if __name__ == "__main__":
    unittest.main()
