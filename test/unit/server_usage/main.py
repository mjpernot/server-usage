#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in server_usage.py.

    Usage:
        test/unit/server_usage/main.py

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
import mock

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_run_program
        test_dir_chk_crt_false
        test_dir_chk_crt_true
        test_require_false
        test_require_true
        test_root_run_true
        test_root_run_false
        test_help_false
        test_help_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = {"-c": "config_file", "-d": "config_dir"}

    @mock.patch("server_usage.run_program")
    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_run_program(self, mock_lib, mock_arg, mock_run):

        """Function:  test_run_program

        Description:  Test with run_program call.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.run_program")
    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_dir_chk_crt_false(self, mock_lib, mock_arg, mock_run):

        """Function:  test_dir_chk_crt_false

        Description:  Test with arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_dir_chk_crt_true(self, mock_lib, mock_arg):

        """Function:  test_dir_chk_crt_true

        Description:  Test with arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_require_false(self, mock_lib, mock_arg):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_require_true(self, mock_lib, mock_arg):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.arg_parser")
    @mock.patch("server_usage.gen_libs")
    def test_root_run_true(self, mock_lib, mock_arg):

        """Function:  test_root_run_true

        Description:  Test with root_run returns True.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.arg_require.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_libs")
    def test_root_run_false(self, mock_lib):

        """Function:  test_root_run_false

        Description:  Test with root_run returns False.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_libs")
    def test_help_false(self, mock_lib):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_libs.help_func")
    @mock.patch("server_usage.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(server_usage.main())


if __name__ == "__main__":
    unittest.main()
