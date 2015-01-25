# -*- coding: utf-8 -*-
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

import os
import tempfile
import shutil
import pathlib
import platform

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    from subprocess32 import check_output
except ImportError:
    from subprocess import check_output

windows = platform.system() == 'Windows'

git = 'git.cmd' if windows else 'git'


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
        check_output(['cookiecutter', str(self.cookiecutter_dir),
                      '--no-input'])
        os.chdir('myscipkg')
        check_output([git, 'init'])
        check_output([git, 'add', '-A'])
        check_output([git, 'commit', '-a', '-m', 'Test commit'])
        check_output([git, 'tag', '0.1'])

        version = check_output(['python', 'setup.py', '--version']).strip('\n').encode('utf-8')
        print(version)
        expversion = '0.1'
        self.assertEqual(version, expversion)

        check_output(['python', 'setup.py', 'install'])
        check_output(['python', 'setup.py', 'test'])
        check_output(['invoke', 'build_docs'])


if __name__ == '__main__':
    unittest.main()
