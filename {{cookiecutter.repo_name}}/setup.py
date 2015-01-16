# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install or upgrade setuptools or pip")
    sys.exit(1)

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://{{ cookiecutter.repo_name }}.rtfd.org."""

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + doclink + '\n\n',
    license='MIT',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    zip_safe=False,
    include_package_data=True,
    # This lets setuptools include_package_data work with git
    setup_requires=["setuptools_git >= 0.3"],
    packages=find_packages(),
    install_requires=[],
    tests_require=['nose'],
    test_suite='nose.collector',
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
