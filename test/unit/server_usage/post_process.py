#!/usr/bin/python
# Classification (U)

"""Program:  post_process.py

    Description:  Unit testing of post_process in server_usage.py.

    Usage:
        test/unit/server_usage/post_process.py

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
import mock
import collections

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_print_format -> Test with printing formatted data.
        test_print_raw -> Test with printing unformatted data.
        test_suppress_false -> Test with suppress option set to false.
        test_suppress_true -> Test with suppress option set to true.
        test_mongo_false -> Test with mongo option set to false.
        test_mongo_true -> Test with mongo option set to true.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.proc_data = {"Data": "String"}
        cfg = collections.namedtuple("Cfg", "db coll")
        self.cfg = cfg("database", "collection")

    @mock.patch("server_usage.gen_libs.display_data")
    def test_print_format(self, mock_display):

        """Function:  test_print_format

        Description:  Test with printing formatted data.

        Arguments:
            None

        """

        args_array = {"-f": True}
        mock_display.return_value = True

        self.assertFalse(server_usage.post_process(self.proc_data,
                                                   args_array, self.cfg))

    def test_print_raw(self):

        """Function:  test_print_raw

        Description:  Test with printing unformatted data.

        Arguments:
            None

        """

        args_array = {}

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.post_process(self.proc_data,
                                                       args_array, self.cfg))

    def test_suppress_false(self):

        """Function:  test_suppress_false

        Description:  Test with suppress option set to false.

        Arguments:
            None

        """

        args_array = {}

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.post_process(self.proc_data,
                                                       args_array, self.cfg))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppress option set to true.

        Arguments:
            None

        """

        args_array = {"-n": True}

        self.assertFalse(server_usage.post_process(self.proc_data, args_array,
                                                   self.cfg))

    def test_mongo_false(self):

        """Function:  test_mongo_false

        Description:  Test with mongo option set to false.

        Arguments:
            None

        """

        args_array = {"-n": True}

        self.assertFalse(server_usage.post_process(self.proc_data, args_array,
                                                   self.cfg))

    @mock.patch("server_usage.mongo_libs.ins_doc")
    def test_mongo_true(self, mock_mongo):

        """Function:  test_mongo_true

        Description:  Test with mongo option set to true.

        Arguments:
            None

        """

        args_array = {"-n": True, "-m": True}
        mock_mongo.return_value = True

        self.assertFalse(server_usage.post_process(self.proc_data, args_array,
                                                   self.cfg))


if __name__ == "__main__":
    unittest.main()
