# -*- coding: utf-8 -*-
import sys
import io

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = '{{ cookiecutter.repo_name }}/_version.py'
versioneer.versionfile_build = '{{ cookiecutter.repo_name }}/_version.py'
versioneer.tag_prefix = ''  # tags are like 1.2.0
versioneer.parentdir_prefix = '{{ cookiecutter.repo_name }}-'  # dirname like 'myproject-1.2.0'

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install or upgrade setuptools or pip")
    sys.exit(1)

readme = io.open('README.rst', mode='r', encoding='utf-8').read()
doclink = """
Documentation
-------------

The full documentation is at http://{{ cookiecutter.repo_name }}.rtfd.org."""
history = io.open('HISTORY.rst', mode='r',
                  encoding='utf-8').read().replace('.. :changelog:', '')

# Use cmdclass.update to add additional commands as necessary. See
# https://docs.python.org/2/distutils/extending.html#integrating-new-commands
cmdclass = versioneer.get_cmdclass()

setup(
    name='{{ cookiecutter.repo_name }}',
    version=versioneer.get_version(),
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    license='MIT',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    zip_safe=False,
    include_package_data=True,
    # This lets setuptools include_package_data work with git
    setup_requires=["setuptools_git >= 0.3"],
    packages=find_packages(),

    # Add requirements here. If the requirement is difficult to install,
    # add to docs/conf.py MAGIC_MOCK, and .travis.yml 'conda install ...'
    install_requires=[],

    tests_require=['nose'],
    test_suite='nose.collector',
    cmdclass=cmdclass,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
