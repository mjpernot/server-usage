# Classification (U)

"""Program:  post_process.py

    Description:  Unit testing of post_process in server_usage.py.

    Usage:
        test/unit/server_usage/post_process.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections
import mock

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_print_format
        test_print_raw
        test_suppress_false
        test_suppress_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.proc_data = {"Data": "String"}
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args.args_array = {"-n": True, "-m": True}
        self.args2.args_array = {"-f": True}
        self.args4.args_array = {"-n": True}

    @mock.patch("server_usage.gen_libs.display_data")
    def test_print_format(self, mock_display):

        """Function:  test_print_format

        Description:  Test with printing formatted data.

        Arguments:

        """

        mock_display.return_value = True

        self.assertFalse(server_usage.post_process(self.proc_data, self.args2))

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test with printing unformatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args3))

    def test_suppress_false(self):

        """Function:  test_suppress_false

        Description:  Test with suppress option set to false.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args3))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppress option set to true.

        Arguments:

        """

        self.assertFalse(server_usage.post_process(self.proc_data, self.args4))


if __name__ == "__main__":
    unittest.main()
