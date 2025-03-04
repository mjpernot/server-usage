# Classification (U)

"""Program:  get_svr_info.py

    Description:  Unit testing of get_svr_info in server_usage.py.

    Usage:
        test/unit/server_usage/get_svr_info.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class System():                                         # pylint:disable=R0903

    """Class:  System

    Description:  Class which is a representation of a Linux server.  A server
        object is used as a proxy for operating with the system.  The basic
        methods and attributes to contain information about the physical
        server.

    Methods:
        __init__

    """

    def __init__(self, host=None, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the System class.

        Arguments:

        """

        if host:
            self.host = host

        else:
            self.host = "HOST_NAME"

        if host_name:
            self.host_name = host_name

        else:
            self.host_name = "SERVER_NAME"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_svr_info

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.test_data = {"servername": "SERVER_NAME",
                          "datetime": "2018-10-11 12:00:01"}

    @mock.patch("server_usage.gen_libs")
    def test_get_svr_info(self, mock_lib):

        """Function:  test_get_svr_info

        Description:  Test data is returned in correct format.

        Arguments:

        """

        mock_lib.get_date.return_value = "2018-10-11"
        mock_lib.get_time.return_value = "12:00:01"

        self.assertEqual(server_usage.get_svr_info(System()), self.test_data)


if __name__ == "__main__":
    unittest.main()
