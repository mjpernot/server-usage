#!/usr/bin/python
# Classification (U)

"""Program:  server_usage.py

    Description:  Monitor the memory usage for processes on a Linux server.

    Usage:
        server_usage.py -c file -d path [-n | -m | -f] [-v | -h]

    Arguments:
        -c configuration => Configuration file.  Required argument.
        -d path => Directory path for "-c" option.  Required argument.

        -n => Do not print results to standard out.
        -m => Save results to Mongo database.
        -f => Format the output to standard out.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.

    Notes:
        Mongo configuration file format (config/mongo.py.TEMPLATE).
        The configuration file format for the Mongo connection used for
        inserting data into a database.

        There are two ways to connect methods:  single Mongo database or a
        Mongo replica set.

            Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            host = "HOST_IP"
            name = "HOSTNAME"
            port = 27017
            conf_file = None

            memory_threshold = 100
            db = "sysmon"

            coll = "mem_usage"
            auth = True
            auth_db = "admin"
            auth_mech = "SCRAM-SHA-1"

            Replica set connection:  Same format as above, but with these
                additional entries at the end of the configuration file.  By
                default all these entries are set to None to represent not
                connecting to a replica set.

            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

            Note:  If using SSL connections then set one or more of the
                following entries.  This will automatically enable SSL
                connections. Below are the configuration settings for SSL
                connections.  See configuration file for details on each entry:

            ssl_client_ca = None
            ssl_client_key = None
            ssl_client_cert = None
            ssl_client_phrase = None

            FIPS Environment for Mongo:  If operating in a FIPS 104-2
                environment, this package will require at least a minimum of
                pymongo==3.8.0 or better.  It will also require a manual change
                to the auth.py module in the pymongo package.  See below for
                changes to auth.py.  In addition, other modules may require to
                have the same modification as the auth.py module.  If a
                stacktrace occurs and it states "= hashlib.md5()" is the
                problem, then note the module name "= hashlib.md5()" is in and
                make the same change as in auth.py:  "usedforsecurity=False".
            - Locate the auth.py file python installed packages on the system
                in the pymongo package directory.
            - Edit the file and locate the "_password_digest" function.
            - In the "_password_digest" function there is an line that should
                match: "md5hash = hashlib.md5()".  Change it to
                "md5hash = hashlib.md5(usedforsecurity=False)".
            - Lastly, it will require the Mongo configuration file entry
                auth_mech to be set to: SCRAM-SHA-1 or SCRAM-SHA-256.

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        server_usage.py -c configuration -d config

"""

# Libraries and Global Variables
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import psutil

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .mongo_lib import mongo_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs
    import lib.gen_class as gen_class
    import mongo_lib.mongo_libs as mongo_libs
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_svr_info(server):

    """Function:  get_svr_info

    Description:  Retrieve and return server information and create the inital
        header.

    Arguments:
        (input) server -> Instance of the Server class
        (output) -> Dictionary holding the basic server information

    """

    return {"servername": server.host_name,
            "datetime":
            str(gen_libs.get_date()) + " " + str(gen_libs.get_time())}


def get_svr_mem():

    """Function:  get_svr_mem

    Description:  Retrieve and return server memory information and status.

    Arguments:
        (output) -> Dictionary holding the basic server information

    """

    svr = psutil.virtual_memory()

    return {"tot_mem": svr.total, "mem_used": svr.used, "mem_per": svr.percent}


def get_proc_mem(mem_threshold=100):

    """Function:  get_proc_mem

    Description:  Return a list of processes that meet the memory threshold
        usage.
        NOTE:  Checking the "uss" attribute which is a bit more accurate then
            the "rss" attribute.

    Arguments:
        (input) mem_threshold -> Memory threshold for a process, in MBs
        (output) -> List of processes that meet the memory threshold

    """

    if isinstance(mem_threshold, str):
        mem_threshold = gen_libs.str_2_type(mem_threshold)

    elif not isinstance(mem_threshold, int):
        mem_threshold = 100

    if mem_threshold < 0:
        mem_threshold = 100

    return [{"pid": p.pid, "ppid": p.ppid(), "proc": p.info["name"],
             "uss_mem": p.info["memory_full_info"].uss,
             "per_used": "%.2f" % p.memory_percent()}
            for p in psutil.process_iter(attrs=["name", "memory_full_info"])
            if p.info["memory_full_info"].uss > mem_threshold * 1024 * 1024]


def post_process(proc_data, args_array, cfg):

    """Function:  post_process

    Description:  Send the data to the requested output and format if
        requested.

    Arguments:
        (input) proc_data -> Dictionary of process data
        (input) args_array -> Dictionary of command line options and values
        (input) cfg -> Configuration module settings

    """

    proc_data = dict(proc_data)
    args_array = dict(args_array)

    if "-n" not in args_array:
        if "-f" in args_array:
            gen_libs.display_data(proc_data)

        else:
            print(proc_data)

    if "-m" in args_array:
        status = mongo_libs.ins_doc(cfg, cfg.db, cfg.coll, proc_data)

        if not status[0]:
            print("Error: Mongo connection -> %s" % (status[1]))


def run_program(args_array):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dictionary of command line options and values

    """

    args_array = dict(args_array)
    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])
    server = gen_class.System()
    server.set_host_name()

    try:
        prog_lock = gen_class.ProgramLock(sys.argv, server.host_name)
        proc_data = get_svr_info(server)
        proc_data.update(get_svr_mem())
        proc_data["processes"] = get_proc_mem(cfg.memory_threshold)
        post_process(proc_data, args_array, cfg)
        del prog_lock

    except gen_class.SingleInstanceException:
        print("WARNING:  server_usage lock in place for: %s"
              % (server.host_name))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories
        opt_req_list -> contains options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_chk_list = ["-d"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if gen_libs.root_run():
            if not arg_parser.arg_require(args_array, opt_req_list) \
               and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
                run_program(args_array)

        else:
            print("Error:  Must run program as root.")


if __name__ == "__main__":
    sys.exit(main())
