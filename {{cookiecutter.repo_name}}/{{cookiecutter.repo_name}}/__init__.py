# -*- coding: utf-8 -*-
"""
============================
{{ cookiecutter.repo_name }}
============================
"""

# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
