# -*- coding: utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import)

import os
import tempfile
import shutil
import pathlib
import platform

try:
    import unittest2 as unittest
except ImportError:
    import unittest

# Use subprocess32 if available
try:
    import subprocess32 as subprocess
except:
    import subprocess as subprocess


def check_output(*args, **kwargs):
    """Subprocess check_output, but prints commands and output by default.
    Also allows printing of error message for helpful debugging.

    Use print_all=False to turn off all printing."""
    print_all = kwargs.pop('print_all', None)
    if print_all is not None:
        print_in = print_all
        print_out = print_all
    else:
        print_in = kwargs.pop('print_in', True)
        print_out = kwargs.pop('print_out', True)

    if print_in:
        print('')
        print(' '.join(args[0]))

    try:
        out_bytes = subprocess.check_output(*args, **kwargs)
        out_lines = out_bytes.decode('utf-8').splitlines()
    except subprocess.CalledProcessError as e:
        # Wrap in try/except so that check_output can print
        raise e

    if print_out:
        for line in out_lines:
            print(line)

    return out_lines

windows = platform.system() == 'Windows'

def find_git_cmd(windows):
    """Determine whether the git command is git or git.cmd on Windows.
    This changed in version 1.8.3"""
    git = 'git'

    if windows:
        try:
            check_output([git, '--version'])
        except subprocess.CalledProcessError:
            try:
                git = 'git.cmd'
                check_output([git, '--version'])
            except subprocess.CalledProcessError:
                msg = "git does not appear to be on your path."
                raise subprocess.CalledProcessError(msg)

    return git

git = find_git_cmd(windows)


def rm_rf(*args):
    """Recursively delete directories, if they exist"""
    for directory in args:
        try:
            shutil.rmtree(str(directory))
        except OSError:
            pass


class TestCookieCutterSciPackage(unittest.TestCase):
    def setUp(self):
        self.dir = pathlib.Path(tempfile.mkdtemp())
        self.cookiecutter_dir = pathlib.Path('.').absolute()

    def tearDown(self):
        rm_rf(self.dir)

    def test_integration(self):
        os.chdir(str(self.dir))
        check_output(['cookiecutter', str(self.cookiecutter_dir), '--no-input'])
        os.chdir('myscipkg')
        check_output(['git', 'init'])
        check_output(['git', 'add', '-A'])
        check_output(['git', 'commit', '-a', '-m', 'Test commit'])
        check_output(['git', 'tag', '0.1'])

        check_output(['python', 'setup.py', 'install'])

        version_lines = check_output(['python', 'setup.py', '--version'])
        version = version_lines[0]
        expversion = u'0.1'
        self.assertEqual(version, expversion)

        check_output(['python', 'setup.py', 'test'])
        check_output(['invoke', 'build_docs'])


if __name__ == '__main__':
    unittest.main()
