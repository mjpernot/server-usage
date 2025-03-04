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
import unittest
import psutil

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def capture_mem(mem):

    """Function:  capture_mem

    Description:  Used to test the results returned from get_proc_mem.

    Arguments:

    """

    return [{"pid": p.pid, "ppid": p.ppid(), "proc": p.info["name"],
             "uss_mem": p.info["memory_full_info"].uss,
             "per_used": "{p.memory_percent():.2f}"}
            for p in psutil.process_iter(attrs=["name", "memory_full_info"])
            if p.info["memory_full_info"] and
            p.info["memory_full_info"].uss > mem * 1024 * 1024]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_pass_zero
        test_pass_negative
        test_pass_list
        test_pass_dict
        test_pass_int
        test_pass_string
        test_get_proc_mem

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

    def test_pass_list(self):

        """Function:  test_pass_list

        Description:  Test which passes a list for the memory argument.

        Arguments:

        """

        test_data = capture_mem(100)
        program_data = server_usage.get_proc_mem([90])

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
