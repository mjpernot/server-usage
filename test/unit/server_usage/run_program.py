#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in server_usage.py.

    Usage:
        test/unit/server_usage/run_program.py

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

# Version
__version__ = version.__version__


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Mock of the gen_class.ProgramLock class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Class instance initilization.
        __del__ -> Deletion of the ProgramLock instance.

    """

    def __init__(self, argv, flavor_id=""):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgramLock class.

        Arguments:
            (input) argv -> Arguments from the command line.
            (input) flavor_id -> Unique identifier for an instance.

        """

        self.lock_created = True

    def __del__(self):

        """Method:  __del__

        Description:  Deletion of the ProgramLock instance.

        Arguments:
            None

        """

        return True


class System(object):

    """Class:  System

    Description:  Mock of the gen_class.System class.

    Super-Class:  object

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        set_host_name -> Set the hostname attribute.

    """

    def __init__(self, host=None, host_name=None):

        """Method:  __init__

        Description:  Initialization of an instance of the System class.

        Arguments:
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        self.host = host
        self.host_name = host_name

    def set_host_name(self, host_name=None):

        """Method:  set_host_name

        Description:  Set the hostname attribute either from argument or pull
            from the server.

        Arguments:
            (input) host_name -> Host name of server.

        """

        if host_name:
            self.host_name = host_name

        else:
            self.host_name = "Server_Name"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_programlock_fail -> Test ProgramLock fails to lock.
        test_run_program -> Test run_program function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        Cfg = collections.namedtuple("Cfg", "memory_threshold")
        self.cfg = Cfg(100)

        self.args = {"-c": "config_file", "-d": "config_dir"}

    @mock.patch("server_usage.gen_class.ProgramLock")
    @mock.patch("server_usage.gen_libs.load_module")
    @mock.patch("server_usage.gen_class.System")
    def test_programlock_fail(self, mock_class, mock_load, mock_lock):

        """Function:  test_programlock_fail

        Description:  Test ProgramLock fails to lock.

        Arguments:
            None

        """

        mock_lock.side_effect = server_usage.gen_class.SingleInstanceException
        mock_load = self.cfg
        mock_class.return_value = System()

        with gen_libs.no_std_out():
            self.assertFalse(server_usage.run_program(self.args))

    @mock.patch("server_usage.post_process")
    @mock.patch("server_usage.get_proc_mem")
    @mock.patch("server_usage.get_svr_mem")
    @mock.patch("server_usage.get_svr_info")
    @mock.patch("server_usage.gen_libs.load_module")
    @mock.patch("server_usage.gen_class")
    def test_run_program(self, mock_class, mock_load, mock_info, mock_mem,
                         mock_proc, mock_post):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:
            None

        """

        mock_class.ProgramLock.return_value = ProgramLock([], "Server_Name")
        mock_class.System.return_value = System()
        mock_load = self.cfg
        mock_info.return_value = {"servername": "Server_Name",
                                  "datetime": "2018-10-17 12:00:01"}
        mock_mem.return_value = {"tot_mem": 100000000, "mem_used": 80000000,
                                 "mem_per": 80}
        mock_proc.return_value = [{"pid": 100, "ppid": 10, "proc": "proc_name",
                                   "uss_mem": 20000000,
                                   "per_used": "%.2f" % 25.15}]
        mock_post.return_value = True

        self.assertFalse(server_usage.run_program(self.args))


if __name__ == "__main__":
    unittest.main()
