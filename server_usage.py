#!/usr/bin/python
# Classification (U)

"""Program:  server_usage.py

    Description:  Monitor the memory usage for processes on a Linux server.

    Usage:
        server_usage.py -c file -d path
            [-n] [-r [-k N]] [-o dir_path/file [-m a|w]]
            [-e to_email [to_email2 ...] [-s subject_line] [-u] [-k N]]
            [-v | -h]

    Arguments:
        -c configuration => Configuration file.
        -d path => Directory path for "-c" option.
        -n => Suppress standard out.
        -r => Expand the JSON format.
            -k N => Indentation for expanded JSON format.
        -e to_email_address(es) => Enables emailing and sends output to one or
                more email addresses.  Email addresses are delimited by a
                space.
            -s subject_line => Subject line of email.
            -u => Override the default mail command and use mailx.
            -k N => Indentation for expanded JSON format.
        -o path/file => Directory path and file name for output.
            -m a|w => Append or write to output to output file. Default is
                write.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.

    Notes:
        Configuration file format (config/condiguration.py.TEMPLATE).
            memory_threshold = 100

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        server_usage.py -c configuration -d config

"""

# Libraries and Global Variables

# Standard
import sys
import pprint
import psutil

try:
    import simplejson as json
except ImportError:
    import json

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
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
             "per_used": f"{p.memory_percent():.2f}"}
            for p in psutil.process_iter(attrs=["name", "memory_full_info"])
            if p.info["memory_full_info"] and
            p.info["memory_full_info"].uss > mem_threshold * 1024 * 1024]


def post_process(proc_data, args):

    """Function:  post_process

    Description:  Send the data to the requested output and format if
        requested.

    Arguments:
        (input) proc_data -> Dictionary of process data
        (input) args -> ArgParser class instance

    """

    proc_data = dict(proc_data)
    cfg = {"indent": args.get_val("-k", def_val=4)} if args.arg_exist("-k") \
        else {}

    if args.arg_exist("-e"):
        subj = args.get_val("-s", def_val="Server_Usage")
        mail = gen_class.setup_mail(args.get_val("-e"), subj=subj)
        mail.add_2_msg(json.dumps(proc_data, **cfg))
        mail.send_mail(use_mailx=args.arg_exist("-u"))

    if args.arg_exist("-o") and args.arg_exist("-r"):
        with open(args.get_val("-o"), mode=args.get_val("-m", def_val="w"),
                  encoding="UTF-8") as ofile:
            pprint.pprint(proc_data, stream=ofile, **cfg)

    elif args.arg_exist("-o"):
        gen_libs.write_file(
            args.get_val("-o"), args.get_val("-m", def_val="w"), proc_data)

    if not args.arg_exist("-n") and args.arg_exist("-r"):
        pprint.pprint(proc_data, **cfg)

    elif not args.arg_exist("-n"):
        print(proc_data)


def run_program(args):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args -> ArgParser class instance

    """

    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    server = gen_class.System()
    server.set_host_name()

    try:
        prog_lock = gen_class.ProgramLock(sys.argv, server.host_name)
        proc_data = get_svr_info(server)
        proc_data.update(get_svr_mem())
        proc_data["processes"] = get_proc_mem(cfg.memory_threshold)
        post_process(proc_data, args)
        del prog_lock

    except gen_class.SingleInstanceException:
        print(f"WARNING:  server_usage lock in place for: {server.host_name}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        file_crt -> contains options which require files to be created
        opt_con_req_list -> contains the options that require other options
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5}
    file_perm_chk = {"-o": 6}
    file_crt = ["-o"]
    opt_con_req_list = {"-s": ["-e"], "-u": ["-e"], "-m": ["-o"], "-k": ["-r"]}
    opt_multi_list = ["-e", "-s"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-o", "-e", "-s", "-m", "-k"]

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message):
        if gen_libs.root_run():
            if args.arg_require(opt_req=opt_req_list)                   \
               and args.arg_cond_req(opt_con_req=opt_con_req_list)      \
               and args.arg_file_chk(
                   file_perm_chk=file_perm_chk, file_crt=file_crt)      \
               and args.arg_dir_chk(dir_perms_chk=dir_perms_chk):
                run_program(args)

        else:
            print("Error:  Must run program as root.")


if __name__ == "__main__":
    sys.exit(main())
