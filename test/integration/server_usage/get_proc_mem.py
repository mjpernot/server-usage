#!/usr/bin/python
# Classification (U)

"""Program:  get_proc_mem.py

    Description:  Integration testing of get_proc_mem in server_usage.py.

    Usage:
        test/integration/server_usage/get_proc_mem.py

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
import psutil

# Local
sys.path.append(os.getcwd())
import server_usage
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def capture_mem(mem, **kwargs):

    """Function:  capture_mem

    Description:  Used to test the results returned from get_proc_mem.

    Arguments:
        (input) mem -> Memory threshold for a process, in MBs.
        (output) -> List of processes that meet the memory threshold.

    """

    return [{"pid": p.pid, "ppid": p.ppid(), "proc": p.info["name"],
             "uss_mem": p.info["memory_full_info"].uss,
             "per_used": "%.2f" % p.memory_percent()}
            for p in psutil.process_iter(attrs=["name", "memory_full_info"])
            if p.info["memory_full_info"].uss > mem * 1024 * 1024]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_pass_zero -> Test which passes a zero for the memory argument.
        test_pass_negative -> Test which passes a negative for memory argument.
        test_pass_dict -> Test which passes a dict for the memory argument.
        test_pass_int -> Test which passes an integer for the memory argument.
        test_pass_string -> Test which passes a string for the memory argument.
        test_get_proc_mem -> Test data is returned in correct format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    def test_pass_zero(self):

        """Function:  test_pass_zero

        Description:  Test which passes a zero for the memory argument.

        Arguments:

        """

        test_data = capture_mem(0)
        program_data = server_usage.get_proc_mem(0)

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))

    def test_pass_negative(self):

        """Function:  test_pass_negative

        Description:  Test which passes a negative for the memory argument.

        Arguments:

        """

        test_data = capture_mem(100)
        program_data = server_usage.get_proc_mem(-1)

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))

    def test_pass_dict(self):

        """Function:  test_pass_dict

        Description:  Test which passes a dictionary for the memory argument.

        Arguments:

        """

        test_data = capture_mem(100)
        program_data = server_usage.get_proc_mem({"key": 90})

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))

    def test_pass_int(self):

        """Function:  test_pass_int

        Description:  Test which passes an integer for the memory argument.

        Arguments:

        """

        test_data = capture_mem(90)
        program_data = server_usage.get_proc_mem(90)

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))

    def test_pass_string(self):

        """Function:  test_pass_string

        Description:  Test which passes a string for the memory argument.

        Arguments:

        """

        test_data = capture_mem(90)
        program_data = server_usage.get_proc_mem('90')

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))

    def test_get_proc_mem(self):

        """Function:  test_get_proc_mem

        Description:  Test data is returned in correct format.

        Arguments:

        """

        test_data = capture_mem(90)
        program_data = server_usage.get_proc_mem(90)

        self.assertEqual(isinstance(program_data, list),
                         isinstance(test_data, list))


if __name__ == "__main__":
    unittest.main()
