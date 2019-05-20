#!/usr/bin/python
# Classification (U)

"""Program:  get_svr_info.py

    Description:  Unit testing of get_svr_info in server_usage.py.

    Usage:
        test/unit/server_usage/get_svr_info.py

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

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class System(object):

    """Class:  System

    Description:  Class which is a representation of a Linux server.  A server
        object is used as a proxy for operating with the system.  The basic
        methods and attributes to contain information about the physical
        server.

    Super-Class:  object

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.

    """

    def __init__(self, host=None, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the System class.

        Arguments:
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        self.host = "HOST_NAME"
        self.host_name = "SERVER_NAME"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_get_svr_info -> Test data is returned in correct format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.test_data = {"servername": "SERVER_NAME",
                          "datetime": "2018-10-11 12:00:01"}

    @mock.patch("server_usage.gen_libs")
    def test_get_svr_info(self, mock_lib):

        """Function:  test_get_svr_info

        Description:  Test data is returned in correct format.

        Arguments:
            None

        """

        mock_lib.get_date.return_value = "2018-10-11"
        mock_lib.get_time.return_value = "12:00:01"

        self.assertEqual(server_usage.get_svr_info(System()), self.test_data)


if __name__ == "__main__":
    unittest.main()
