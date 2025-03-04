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
import unittest

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
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
        opt_val_list = ["-c", "-d"]
        argv = [
            "server_usage.py", "-c", "configuration", "-d", self.config_path]
        argv2 = [
            "server_usage.py", "-c", "configuration", "-d", self.config_path,
            "-n"]
        self.args = gen_class.ArgParser(argv, opt_val=opt_val_list)
        self.args.arg_parse2()
        self.args2 = gen_class.ArgParser(argv2, opt_val=opt_val_list)
        self.args2.arg_parse2()

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


if __name__ == "__main__":
    unittest.main()
