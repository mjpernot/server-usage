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
import server_usage
import lib.gen_libs as gen_libs
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
        test_mongo_failed
        test_mongo_connect
        test_print_format
        test_print_raw
        test_suppress_false
        test_suppress_true
        test_mongo_false
        test_mongo_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.proc_data = {"Data": "String"}
        cfg = collections.namedtuple("Cfg", "db coll")
        self.cfg = cfg("database", "collection")
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args3 = ArgParser()
        self.args4 = ArgParser()
        self.args.args_array = {"-n": True, "-m": True}
        self.args2.args_array = {"-f": True}
        self.args4.args_array = {"-n": True}

    @mock.patch("server_usage.mongo_libs.ins_doc")
    def test_mongo_failed(self, mock_mongo):

        """Function:  test_mongo_failed

        Description:  Test with failed connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = (False, "Connection Failure")

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(
                    self.proc_data, self.args, self.cfg))

    @mock.patch("server_usage.mongo_libs.ins_doc")
    def test_mongo_connect(self, mock_mongo):

        """Function:  test_mongo_connect

        Description:  Test with successful connection to Mongo.

        Arguments:

        """

        mock_mongo.return_value = (True, None)

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args, self.cfg))

    @mock.patch("server_usage.gen_libs.display_data")
    def test_print_format(self, mock_display):

        """Function:  test_print_format

        Description:  Test with printing formatted data.

        Arguments:

        """

        mock_display.return_value = True

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args2, self.cfg))

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test with printing unformatted data.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(
                    self.proc_data, self.args3, self.cfg))

    def test_suppress_false(self):

        """Function:  test_suppress_false

        Description:  Test with suppress option set to false.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(
                    self.proc_data, self.args3, self.cfg))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppress option set to true.

        Arguments:

        """

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args4, self.cfg))

    def test_mongo_false(self):

        """Function:  test_mongo_false

        Description:  Test with mongo option set to false.

        Arguments:

        """

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args4, self.cfg))

    @mock.patch("server_usage.mongo_libs.ins_doc")
    def test_mongo_true(self, mock_mongo):

        """Function:  test_mongo_true

        Description:  Test with mongo option set to true.

        Arguments:

        """

        mock_mongo.return_value = (True, None)

        self.assertFalse(
            server_usage.post_process(self.proc_data, self.args, self.cfg))


if __name__ == "__main__":
    unittest.main()
