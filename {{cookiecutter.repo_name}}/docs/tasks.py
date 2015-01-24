# :title: fabfile.py
# :author: John A. Marohn (jam99@cornell.edu)
# :date: 2014-07-26
# :subject: substitute/extend "make html" and "make open"
# :ref: http://docs.fabfile.org/en/1.4.1/tutorial.html
# :ref: http://ipython.org/ipython-doc/1/interactive/nbconvert.html


import os
import shutil

try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess

import pathlib
import webbrowser


from invoke import task

cwd = pathlib.Path('.').absolute()


# Helper functions for unix-like removing folders and files.
def rm_rf(*args):
    """Recursively delete directories, if they exist"""
    for directory in args:
        try:
            shutil.rmtree(str(directory))
        except OSError:
            pass


@task(default=True)
def help():
    """Print out a helpful message."""

    print("""\
Usage:  inv[oke] [--core-opts] task1 [--task1-opts] ... taskN [--taskN-opts]

Tasks:

clean      Delete the contents of the _build/ directory
html       Create sphinx documentation as stand-alone HTML files
open       Open the HTML documentation in a web browser


To see more about a specific task, run invoke --help task""")


@task
def clean():
    """Delete the contents of the _build/ directory."""

    rm_rf(cwd/'_build')


@task
def html():
    """Create sphinx documentation as stand-alone HTML files."""

    subprocess.call(['sphinx-build', '-b', 'html', str(cwd),
        str(cwd/'_build/html')])
    print("Build finished; see _build/html/index.html")


@task
def open():
    """Open the HTML documentation in a browser"""
    index_path = cwd/'_build/html/index.html'
    webbrowser.open(index_path.as_uri())
