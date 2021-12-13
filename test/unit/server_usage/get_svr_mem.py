#!/usr/bin/python
# Classification (U)

"""Program:  get_svr_mem.py

    Description:  Unit testing of get_svr_mem in server_usage.py.

    Usage:
        test/unit/server_usage/get_svr_mem.py

    Arguments:

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
import collections
import mock

# Local
sys.path.append(os.getcwd())
import server_usage
import version

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

        server = collections.namedtuple("Server", "total used percent")
        self.svr = server(500, 250, 50)
        self.test_data = {"tot_mem": 500, "mem_used": 250, "mem_per": 50}

    @mock.patch("server_usage.psutil.virtual_memory")
    def test_get_svr_mem(self, mock_psutil):

        """Function:  test_get_svr_mem

        Description:  Test data is returned in correct format.

        Arguments:

        """

        mock_psutil.return_value = self.svr

        self.assertEqual(server_usage.get_svr_mem(), self.test_data)


if __name__ == "__main__":
    unittest.main()
