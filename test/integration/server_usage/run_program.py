#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in server_usage.py.

    Usage:
        test/integration/server_usage/run_program.py

    Arguments:

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

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_mongo -> Test inserting data into Mongo database.
        test_print_format -> Test printing formatted data.
        test_no_print -> Test standard out suppression.
        test_print_raw -> Test printing unformatted data.
        tearDown -> Clean up of integration testing.

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

        self.args_array = {"-c": "configuration", "-d": self.config_path}

        svr = mongo_class.Server(
            self.cfg.name, self.cfg.user, self.cfg.passwd, host=self.cfg.host,
            port=self.cfg.port, auth=self.cfg.auth,
            conf_file=self.cfg.conf_file)
        svr.connect()

        if self.cfg.db in svr.fetch_dbs():
            print("ERROR:  Test environment not clean - database: %s exists"
                  % (self.cfg.db))
            cmds_gen.disconnect([svr])
            self.skipTest("Pre-conditions not met.")

        cmds_gen.disconnect([svr])

    def test_mongo(self):

        """Function:  test_mongo

        Description:  Test inserting data into Mongo database.

        Arguments:

        """

        self.args_array.update({"-n": True, "-m": True})

        server_usage.run_program(self.args_array)

        coll = mongo_libs.crt_coll_inst(self.cfg, self.cfg.db, self.cfg.coll)
        coll.connect()

        self.assertTrue(coll.coll_cnt() == 1)

    def test_print_format(self):

        """Function:  test_print_format

        Description:  Test printing formatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.run_program(self.args_array))

    def test_no_print(self):

        """Function:  test_no_print

        Description:  Test standard out suppression.

        Arguments:

        """

        self.args_array["-n"] = True

        self.assertFalse(server_usage.run_program(self.args_array))

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test printing unformatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.run_program(self.args_array))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        mongo = mongo_class.DB(
            self.cfg.name, self.cfg.user, self.cfg.passwd, host=self.cfg.host,
            port=self.cfg.port, db=self.cfg.db, auth=self.cfg.auth,
            conf_file=self.cfg.conf_file)

        mongo.db_connect(self.cfg.db)
        mongo.db_cmd("dropDatabase")
        cmds_gen.disconnect([mongo])


if __name__ == "__main__":
    unittest.main()
