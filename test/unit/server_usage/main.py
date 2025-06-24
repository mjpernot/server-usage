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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_dir_chk
        arg_require
        arg_parse2
        arg_cond_req_or
        arg_cond_req
        arg_file_chk

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.opt_con_req = None
        self.opt_con_req2 = True
        self.file_perm_chk = None
        self.file_crt = None
        self.arg_file_chk2 = True
        self.argparse2 = True

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2

    def arg_cond_req(self, opt_con_req):

        """Method:  arg_cond_req

        Description:  Method stub holder for gen_class.ArgParser.arg_cond_req.

        Arguments:

        """

        self.opt_con_req = opt_con_req

        return self.opt_con_req2

    def arg_file_chk(self, file_perm_chk, file_crt):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk
        self.file_crt = file_crt

        return self.arg_file_chk2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_help_true
        test_help_false
        test_root_run_false
        test_root_run_true
        test_require_false
        test_require_true
        test_arg_cond_false
        test_arg_cond_true
        test_arg_file_false
        test_arg_file_true
        test_dir_chk_crt_false
        test_dir_chk_crt_true
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {"-c": "config_file", "-d": "config_dir"}

    @mock.patch("server_usage.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parse2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_libs.help_func")
    @mock.patch("server_usage.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parse2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_libs.help_func")
    @mock.patch("server_usage.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_help_false(self, mock_lib, mock_arg):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_root_run_false(self, mock_lib, mock_arg):

        """Function:  test_root_run_false

        Description:  Test with root_run returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_root_run_true(self, mock_lib, mock_arg):

        """Function:  test_root_run_true

        Description:  Test with root_run returns True.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_require_false(self, mock_lib, mock_arg):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_require_true(self, mock_lib, mock_arg):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_arg_cond_false(self, mock_lib, mock_arg):

        """Function:  test_arg_cond_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        self.args.opt_con_req2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_arg_cond_true(self, mock_lib, mock_arg):

        """Function:  test_arg_cond_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_arg_file_false(self, mock_lib, mock_arg):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        self.args.arg_file_chk2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_arg_file_true(self, mock_lib, mock_arg):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_dir_chk_crt_false(self, mock_lib, mock_arg):

        """Function:  test_dir_chk_crt_false

        Description:  Test with arg_dir_chk_crt returns False.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.run_program", mock.Mock(return_value=True))
    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_dir_chk_crt_true(self, mock_lib, mock_arg):

        """Function:  test_dir_chk_crt_true

        Description:  Test with arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())

    @mock.patch("server_usage.run_program", mock.Mock(return_value=True))
    @mock.patch("server_usage.gen_class.ArgParser")
    @mock.patch("server_usage.gen_libs")
    def test_run_program(self, mock_lib, mock_arg):

        """Function:  test_run_program

        Description:  Test with run_program call.

        Arguments:

        """

        mock_lib.help_func.return_value = False
        mock_lib.root_run.return_value = True
        mock_arg.return_value = self.args

        self.assertFalse(server_usage.main())


if __name__ == "__main__":
    unittest.main()
