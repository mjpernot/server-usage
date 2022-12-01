# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in server_usage.py.

    Usage:
        test/integration/server_usage/main.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import mongo_lib.mongo_libs as mongo_libs
import mongo_lib.mongo_class as mongo_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mongo
        test_print_format
        test_no_print
        test_print_raw
        test_arg_dir_chk_crt_func
        test_arg_require_func
        test_root_run_func
        test_help_func
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
        self.argv_list = [os.path.join(self.base_dir, "main.py"),
                          "-c", "configuration", "-d", self.config_path]
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

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.extend(("-m", "-n"))
        cmdline.argv = self.argv_list
        server_usage.main()
        coll = mongo_libs.crt_coll_inst(self.cfg, self.cfg.db, self.cfg.coll)
        coll.connect()

        self.assertTrue(coll.coll_cnt() == 1)

    def test_print_format(self):

        """Function:  test_print_format

        Description:  Test printing formatted data.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    def test_no_print(self):

        """Function:  test_no_print

        Description:  Test standard out suppression.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-n")
        cmdline.argv = self.argv_list

        self.assertFalse(server_usage.main())

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test printing unformatted data.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    @mock.patch("server_usage.run_program")
    def test_arg_dir_chk_crt_func(self, mock_run):

        """Function:  test_arg_dir_chk_crt_func

        Description:  Test arg_dir_chk_crt function.

        Arguments:

        """

        mock_run.return_value = True

        cmdline = gen_libs.get_inst(sys)
        cmdline.argv = self.argv_list

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.arg_parser.arg_dir_chk_crt")
    def test_arg_require_func(self, mock_arg):

        """Function:  test_arg_require_func

        Description:  Test arg_require function.

        Arguments:

        """

        mock_arg.return_value = True

        cmdline = gen_libs.get_inst(sys)
        cmdline.argv = self.argv_list

        self.assertFalse(server_usage.main())

    def test_root_run_func(self):

        """Function:  test_root_run_func

        Description:  Test root_run function.

        Arguments:

        """

        self.argv_list.remove("-c")

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    def test_help_func(self):

        """Function:  test_help_func

        Description:  Test help_func function.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-v")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

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
