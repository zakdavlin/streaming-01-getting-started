"""
Import this module to provide a standard header that can 
help with debugging. 

This file is named:   about.py
This module is named: about

Important: To work correctly, 
           this file must be in the same directory 
           as the source file that imports it.

To import this file, first import it at the top of your file with:
    
    import about as about

To use the print_header() method, call it with the built-in name of your file:

    print(about.get_header(__file__))

To learn about more search for:

    builtin attributes python

"""

# imports

import datetime
import os
import platform
import sys

# declare program constants
# we assume data is kept in a directory named 'data'
# if your organization is different, please update the data_folder below:

data_folder = "" # "data"
divider = "=============================================================="

# define helper functions


def get_source_directory_path():
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def get_data_directory_path():
    """Returns the absolute path to the data directory."""
    datapath = os.sep.join([os.getcwd(), data_folder])
    return datapath


def get_data_file_path(fn):
    """Return the absolute path to a data file given just the file name (fn)."""
    dir = get_data_directory_path()
    fullPath = os.sep.join([dir, fn])
    return fullPath


def get_header(fn):
    """This function prints helpful information about a file."""
    return f"""

{divider}
{divider}

 Welcome! 

 It's {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}

 This file is running on:    {os.name} {platform.system()} {platform.release()}
 
 The Python version is:      {platform.python_version()}
 
 The Python interpreter is at: 
 {sys.executable}

 The active environment should be either conda OR pip (one should be None):

     Active conda env is: {os.environ.get('CONDA_DEFAULT_ENV') }
     Active pip env is:   {os.environ.get('PIP_DEFAULT_ENV')}
 
 The path to the active virtual environment is:

 {sys.prefix}
 
 The Current Working Directory (CWD) where this command was launched is:

 {os.getcwd()}
 
 The absolute path to the data directory is:

 {get_data_directory_path()}
 
 The absolute path to this source directory is:

 {get_source_directory_path()}
 
 The absolute path to this file is:

 {fn}
 
{divider}
{divider}

"""


# -------------------------------------------------------------
# Call some functions and execute code!

# Call our print_header() function on this file to test it
print(get_header(__file__)) # uncomment to test

print_to_file = True
if print_to_file:
    # print to a file
    fn = "about.txt"
    with open(fn, "w") as f:
        f.write(get_header(__file__))

