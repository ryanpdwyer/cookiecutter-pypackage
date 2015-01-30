TODO
====

- [x] Test Makefile upload command

Improve cross-platform capabilities
-----------------------------------

- [x] Switch the tests to use python rather than a bash script
- [x] Switch fabfile in docs to an invoke tasks file
- [ ] `invoke.run` doesn't display output on Windows—this is really annoying. Use hand-written `subprocess.check_output` with printing instead
- [ ] Should I write a version of the `check_output` function that doesn't require a list?
        ```python
        check_output('python', 'setup.py', '--version')
        ```

        vs.

        ```python
        check_output(['python', 'setup.py', '--version'])
        ```

        Maybe not—breaks compatibility with `subprocess.check_output` for minimal gain.
