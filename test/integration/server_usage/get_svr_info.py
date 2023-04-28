# Classification (U)

"""Program:  get_svr_info.py

    Description:  Integration testing of get_svr_info in server_usage.py.

    Usage:
        test/integration/server_usage/get_svr_info.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import server_usage
import version

__version__ = version.__version__


class System(object):

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
                          "datetime": "TEST_DATATIME"}

    def test_get_svr_info(self):

        """Function:  test_get_svr_info

        Description:  Test data is returned in correct format.

        Arguments:

        """

        data = server_usage.get_svr_info(System())

        self.assertEqual(data["servername"], self.test_data["servername"])


if __name__ == "__main__":
    unittest.main()
