# Classification (U)

"""Program:  post_process.py

    Description:  Unit testing of post_process in server_usage.py.

    Usage:
        test/unit/server_usage/post_process.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

try:
    import simplejson as json
except ImportError:
    import json

# Local
sys.path.append(os.getcwd())
import server_usage                             # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class MailTest():

    """Class:  MailTest

    Description:  Class which is a representation of an email.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, toline, subj=None, frm=None, msg_type=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:

        """

        if isinstance(subj, list):
            subj = list(subj)

        if isinstance(toline, list):
            self.toline = list(toline)

        else:
            self.toline = toline

        self.subj = subj
        self.frm = frm
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:

        """

        if txt_ln:

            if isinstance(txt_ln, str):
                self.msg = self.msg + txt_ln

            else:
                self.msg = self.msg + json.dumps(txt_ln)

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Send email.

        Arguments:

        """

        status = True

        if use_mailx:
            status = True

        return status


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_outfile_mode2_flat2
        test_outfile_mode2_flat
        test_outfile_mode2
        test_outfile_mode_flat2
        test_outfile_mode_flat
        test_outfile_mode
        test_outfile_flat2
        test_outfile_flat
        test_outfile
        test_email_subj
        test_email_no_subj
        test_email_mailx2
        test_email_mailx
        test_email_indent
        test_email
        test_indent_true
        test_indent_false
        test_suppress_false_expand2
        test_suppress_false_expand
        test_suppress_false
        test_suppress_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.proc_data = {"Data": "String"}
        self.args = ArgParser()
        self.args.args_array["-n"] = True
        self.args2 = ArgParser()
        self.outfile = "path/to/open"
        self.mail = MailTest("toaddr")

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode2_flat2(self):

        """Function:  test_outfile_mode2_flat2

        Description:  Test with outfile and mode option and flat mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "w"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode2_flat(self):

        """Function:  test_outfile_mode2_flat

        Description:  Test with outfile and mode option and flat mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "w"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_mode2(self, mock_file):

        """Function:  test_outfile_mode2

        Description:  Test with outfile and mode option.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "w"
        self.args.args_array["-r"] = True

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode_flat2(self):

        """Function:  test_outfile_mode_flat2

        Description:  Test with outfile and mode option and flatten mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "a"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_mode_flat(self):

        """Function:  test_outfile_mode_flat

        Description:  Test with outfile and mode option and flatten mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "a"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_mode(self, mock_file):

        """Function:  test_outfile_mode

        Description:  Test with outfile and mode option.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-m"] = "a"
        self.args.args_array["-r"] = True

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_flat2(self):

        """Function:  test_outfile_flat2

        Description:  Test with outfile option in flatten mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_libs.write_file",
                mock.Mock(return_value=True))
    def test_outfile_flat(self):

        """Function:  test_outfile_flat

        Description:  Test with outfile option in flatten mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile(self, mock_file):

        """Function:  test_outfile

        Description:  Test with outfile option in expand mode.

        Arguments:

        """

        self.args.args_array["-o"] = "path/to/open"
        self.args.args_array["-r"] = True

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email_subj(self, mock_mail):

        """Function:  test_email_subj

        Description:  Test with email option with subject option.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"
        self.args.args_array["-s"] = "EmailSubject"

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email_no_subj(self, mock_mail):

        """Function:  test_email_no_subj

        Description:  Test with email option with no subject option.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email_mailx2(self, mock_mail):

        """Function:  test_email_mailx2

        Description:  Test with email option with mailx option.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email_mailx(self, mock_mail):

        """Function:  test_email_mailx

        Description:  Test with email option with mailx option.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"
        self.args.args_array["-u"] = True

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email_indent(self, mock_mail):

        """Function:  test_email_indent

        Description:  Test with email option with indent.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"
        self.args.args_array["-k"] = 4

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    @mock.patch("server_usage.gen_class.setup_mail")
    def test_email(self, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        self.args.args_array["-e"] = "To_Address"

        mock_mail.return_value = self.mail

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    def test_indent_true(self):

        """Function:  test_indent_true

        Description:  Test pass in indent arg.

        Arguments:

        """

        self.args.args_array["-k"] = 4

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    def test_indent_false(self):

        """Function:  test_indent_false

        Description:  Test with no indent arg passed in.

        Arguments:

        """

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))

    def test_suppress_false_expand2(self):

        """Function:  test_suppress_false_expand2

        Description:  Test with suppression is false and expand option.

        Arguments:

        """

        self.args.args_array["-k"] = 4

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args2))

    def test_suppress_false_expand(self):

        """Function:  test_suppress_false_expand

        Description:  Test with suppression is false and expand option.

        Arguments:

        """

        self.args.args_array["-r"] = True
        self.args.args_array["-k"] = 4

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args2))

    def test_suppress_false(self):

        """Function:  test_suppress_false

        Description:  Test with suppress option set to false.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                server_usage.post_process(self.proc_data, self.args2))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppress option set to true.

        Arguments:

        """

        self.assertFalse(server_usage.post_process(self.proc_data, self.args))


if __name__ == "__main__":
    unittest.main()
