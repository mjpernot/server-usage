#!/usr/bin/python
# Classification (U)

"""Program:  get_proc_mem.py

    Description:  Unit testing of get_proc_mem in server_usage.py.

    Usage:
        test/unit/server_usage/get_proc_mem.py

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


class PSUtil(object):

    """Class:  PSUtil

    Description:  Class which is a mock representation of a
        psutil.process_iter class.

    Super-Class:  object

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.
        ppid -> Mock the psutil.process_iters.ppid() function.
        memory_percent -> Mock psutil.process_iters.memory_percent() function.

    """

    def __init__(self, name, pid, p_pid, uss, percent):

        """Method:  __init__

        Description:  Initialization of an instance of the PSUtil class.

        Arguments:
            None

        """

        # Named tuple for the attributes returned from psutil.process_iter.
        Fullmem = collections.namedtuple("Fullmem", "uss percent")
        fullmem = Fullmem(uss, percent)

        self.pid = pid
        self.p_pid = p_pid
        self.info = {"name": name, "memory_full_info": fullmem}

    def ppid(self):

        """Method:  ppid

        Description:  Mock the psutil.process_iters.ppid() function.

        Arguments:
            None

        """

        return self.p_pid

    def memory_percent(self):

        """Method:  memory_percent

        Description:  Mock the psutil.process_iters.memory_percent() function.

        Arguments:
            None

        """

        return self.info["memory_full_info"].percent


def psutil_generator():

    """Function:  psutil_generator

    Description:  Generator function to mock the psutil.process_iters function.

    Arguments:
        None

    """

    yield PSUtil("system_proc1", 1001, 11, 90000000, 50)
    yield PSUtil("system_proc2", 1002, 12, 100000000, 55)
    yield PSUtil("system_proc3", 1003, 13, 110000000, 60)
    yield PSUtil("system_proc4", 1004, 14, 140000000, 70)
    yield PSUtil("system_proc5", 1005, 15, 150000000, 75)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_pass_string -> Test which passes a string for the memory argument.
        test_pass_list -> Test which passes a list for the memory argument.
        test_less_then_zero -> Test less then zero is passed for memory.
        test_default_setting -> Test where default setting is used.
        test_zero_memory -> Test where zero memory setting is checked for.
        test_multiple_rows -> Test where multiple rows are returned.
        test_one_row -> Test where one row is returned.
        test_zero_rows -> Test where zero rows are returned.
        test_get_proc_mem -> Test data is returned in correct format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.data1 = {"per_used": "50.00", "pid": 1001, "ppid": 11,
                      "proc": "system_proc1", "uss_mem": 90000000}
        self.data2 = {"per_used": "55.00", "pid": 1002, "ppid": 12,
                      "proc": "system_proc2", "uss_mem": 100000000}
        self.data3 = {"per_used": "60.00", "pid": 1003, "ppid": 13,
                      "proc": "system_proc3", "uss_mem": 110000000}
        self.data4 = {"per_used": "70.00", "pid": 1004, "ppid": 14,
                      "proc": "system_proc4", "uss_mem": 140000000}
        self.data5 = {"per_used": "75.00", "pid": 1005, "ppid": 15,
                      "proc": "system_proc5", "uss_mem": 150000000}

    @mock.patch("server_usage.gen_libs.str_2_type")
    @mock.patch("server_usage.psutil.process_iter")
    def test_pass_string(self, mock_psutil, mock_str):

        """Function:  test_pass_string

        Description:  Test which passes a string for the memory argument.

        Arguments:
            None

        """

        test_data = [self.data2, self.data3, self.data4, self.data5]

        mock_psutil.return_value = psutil_generator()
        mock_str.return_value = 89

        self.assertEqual(server_usage.get_proc_mem('89'), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_pass_list(self, mock_psutil):

        """Function:  test_pass_list

        Description:  Test which passes a list for the memory argument.

        Arguments:
            None

        """

        test_data = [self.data3, self.data4, self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem([120]), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_less_then_zero(self, mock_psutil):

        """Function:  test_less_then_zero

        Description:  Test less then zero is passed for memory setting.

        Arguments:
            None

        """

        test_data = [self.data3, self.data4, self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(-10), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_default_setting(self, mock_psutil):

        """Function:  test_default_setting

        Description:  Test where default setting is used.

        Arguments:
            None

        """

        test_data = [self.data3, self.data4, self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_zero_memory(self, mock_psutil):

        """Function:  test_zero_memory

        Description:  Test where zero memory setting is checked for.

        Arguments:
            None

        """

        test_data = [self.data1, self.data2, self.data3, self.data4,
                     self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(0), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_multiple_rows(self, mock_psutil):

        """Function:  test_multiple_rows

        Description:  Test where multiple rows are returned.

        Arguments:
            None

        """

        test_data = [self.data3, self.data4, self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(102), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_one_row(self, mock_psutil):

        """Function:  test_one_row

        Description:  Test where one row is returned.

        Arguments:
            None

        """

        test_data = [self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(140), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_zero_rows(self, mock_psutil):

        """Function:  test_zero_rows

        Description:  Test where zero rows are returned.

        Arguments:
            None

        """

        test_data = []

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(200), test_data)

    @mock.patch("server_usage.psutil.process_iter")
    def test_get_proc_mem(self, mock_psutil):

        """Function:  test_get_proc_mem

        Description:  Test data is returned in correct format.

        Arguments:
            None

        """

        test_data = [self.data5]

        mock_psutil.return_value = psutil_generator()

        self.assertEqual(server_usage.get_proc_mem(140), test_data)


if __name__ == "__main__":
    unittest.main()
