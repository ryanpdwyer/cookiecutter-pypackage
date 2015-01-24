==========================
cookiecutter-sci-pypackage
==========================

Cookiecutter template for a Python package. See https://github.com/audreyr/cookiecutter.

* Free software: MIT license
* Nose_ runner: Supports `unittest`, `nose` style tests.
* `Travis CI`_: Ready for Travis Continuous Integration testing
* Sphinx_ docs: Documentation ready for generation with ReadTheDocs_
* versioneer2_: versioning: Just use ``git tag`` to update the version number of your package.

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/ryanpdywer/cookiecutter-sci-pypackage.git

Then:

* Go to the generated folder, and make your first commit and first tag (``git tag 0.1``, for example).
* Create a new repository on GitHub, push your first commit there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run ``python setup.py test``
* Release your package the standard Python way.

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original pypackage, uses unittest for
   testing and other minor changes.
* `Nekroze/cookiecutter-pypackage`_: The project this project is based off of.

Fork This
~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Once you have your fork working, add it to the
Similar Cookiecutter Templates list with a brief explanation. It's up to you
whether or not to rename your fork.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _`Travis CI`: http://travis-ci.org/
.. _Nose: http://nose.readthedocs.org/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _versioneer2: https://github.com/ryanpdwyer/versioneer2
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
