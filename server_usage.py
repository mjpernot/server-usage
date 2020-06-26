#!/usr/bin/python
# Classification (U)

"""Program:  server_usage.py

    Description:  Monitor the memory usage for processes on a Linux server.

    Usage:
        server_usage.py -c file -d path [-n | -m | -f] [-v | -h]

    Arguments:
        -c configuration => Configuration file.  Required argument.
        -d path => Directory path for "-c" option.  Required argument.
        -f => Format the output to standard out.
        -n => Do not print results to standard out.
        -m => Save results to Mongo database.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.

    Notes:
        Configuration file format (configuration.py).  The Mongo database
        section is only required if saving the results to the database.

            # Is amount of memory required before the process is recorded.
            # Value is in Megabytes.
            memory_threshold = 100

            # Mongo database section.
            # User connection information.
            user = "USER_NAME"
            passwd = "USER_PASSWORD"

            # Database host information.
            host = "HOST_IP"
            name = "HOSTNAME"

            # Database to authentication to.
            db_auth = "AUTHENTICATION_DATABASE"

            # Replica Set Mongo configuration settings.
            # Replica set name.  Set to None if not connectin to a replica set.
            repset = "REPLICA_SET_NAME"

            # Replica host listing.  List of mongo databases in replica set.
            # Set to None if not connecting to a Mongo replica set.
            repset_hosts = "HOST1:PORT, HOST2:PORT, [...]"

            # Database and Collection names
            db = "sysmon"
            coll = "mem_usage"

    Example:
        server_usage.py -c configuration -d config

"""

# Libraries and Global Variables

# Standard
import sys

# Third-party
import psutil

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__


def help_message(**kwargs):

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_svr_info(server, **kwargs):

    """Function:  get_svr_info

    Description:  Retrieve and return server information and create the inital
        header.

    Arguments:
        (input) server -> Instance of the Server class.
        (output) -> Dictionary holding the basic server information.

    """

    return {"servername": server.host_name,
            "datetime":
            str(gen_libs.get_date()) + " " + str(gen_libs.get_time())}


def get_svr_mem(**kwargs):

    """Function:  get_svr_mem

    Description:  Retrieve and return server memory information and status.

    Arguments:
        (output) -> Dictionary holding the basic server information.

    """

    svr = psutil.virtual_memory()

    return {"tot_mem": svr.total, "mem_used": svr.used, "mem_per": svr.percent}


def get_proc_mem(mem_threshold=100, **kwargs):

    """Function:  get_proc_mem

    Description:  Return a list of processes that meet the memory threshold
        usage.
        NOTE:  Checking the "uss" attribute which is a bit more accurate then
            the "rss" attribute.

    Arguments:
        (input) mem_threshold -> Memory threshold for a process, in MBs.
        (output) -> List of processes that meet the memory threshold.

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


def post_process(proc_data, args_array, cfg, **kwargs):

    """Function:  post_process

    Description:  Send the data to the requested output and format if
        requested.

    Arguments:
        (input) proc_data -> Dictionary of process data.
        (input) args_array -> Dictionary of command line options and values.
        (input) cfg -> Configuration module settings.

    """

    proc_data = dict(proc_data)
    args_array = dict(args_array)

    if "-n" not in args_array:
        if "-f" in args_array:
            gen_libs.display_data(proc_data)

        else:
            print(proc_data)

    if "-m" in args_array:
        mongo_libs.ins_doc(cfg, cfg.db, cfg.coll, proc_data)


def run_program(args_array, **kwargs):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dictionary of command line options and values.

    """

    cmdline = gen_libs.get_inst(sys)
    args_array = dict(args_array)
    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])
    server = gen_class.System()
    server.set_host_name()

    try:
        prog_lock = gen_class.ProgramLock(cmdline.argv, server.host_name)
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
        dir_chk_list -> contains options which will be directories.
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if gen_libs.root_run():
            if not arg_parser.arg_require(args_array, opt_req_list) \
               and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
                run_program(args_array)

        else:
            print("Error:  Must run program as root.")


if __name__ == "__main__":
    sys.exit(main())
