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


from invoke import run

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
        run('cookiecutter "{0}" --no-input'.format(str(self.cookiecutter_dir)))
        os.chdir('myscipkg')
        run('git init')
        run('git add -A')
        run('git commit -a -m "Test commit"')
        run('git tag 0.1')

        run('python setup.py install')

        version_out = run('python setup.py --version')
        version = version_out.stdout.strip('\n').strip('\r')
        expversion = '0.1'
        self.assertEqual(version, expversion)

        run('python setup.py test')
        run('invoke build_docs')


if __name__ == '__main__':
    unittest.main()
