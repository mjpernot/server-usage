# Classification (U)

"""Program:  post_process.py

    Description:  Integration testing of post_process in server_usage.py.

    Usage:
        test/integration/server_usage/post_process.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_suppress_print
        test_format_print
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
        self.args2.args_array = {"-r": True}
        self.args3.args_array = {"-n": True}
        self.base_dir = "test/integration/server_usage"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")

    def test_suppress_print(self):

        """Function:  test_suppress_print

        Description:  Test with  suppressing printing data.

        Arguments:

        """

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args3))

    def test_format_print(self):

        """Function:  test_format_print

        Description:  Test printing formatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.post_process({}, self.args2))


if __name__ == "__main__":
    unittest.main()
