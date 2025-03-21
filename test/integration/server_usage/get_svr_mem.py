# Classification (U)

"""Program:  get_svr_mem.py

    Description:  Integration testing of get_svr_mem in server_usage.py.

    Usage:
        test/integration/server_usage/get_svr_mem.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections
import psutil

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_svr_mem

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        server = collections.namedtuple("Server", "total")
        self.test_data = server(psutil.virtual_memory().total)

    def test_get_svr_mem(self):

        """Function:  test_get_svr_mem

        Description:  Test data is returned in correct format.

        Arguments:

        """

        self.assertEqual(server_usage.get_svr_mem()["tot_mem"],
                         self.test_data.total)


if __name__ == "__main__":
    unittest.main()
