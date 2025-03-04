# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in server_usage.py.

    Usage:
        test/integration/server_usage/main.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
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


if __name__ == "__main__":
    unittest.main()
