.. image:: https://img.shields.io/pypi/status/ReleaseIt
    :alt: PyPI - Status

.. image:: https://img.shields.io/pypi/wheel/ReleaseIt
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/ReleaseIt
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/github/v/release/hendrikdutoit/ReleaseIt
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/github/license/hendrikdutoit/ReleaseIt
    :alt: License

.. image:: https://img.shields.io/github/issues-raw/hendrikdutoit/ReleaseIt
    :alt: GitHub issues

.. image:: https://img.shields.io/pypi/dm/BEETest21
    :alt: PyPI - Downloads

.. image:: https://img.shields.io/github/search/hendrikdutoit/ReleaseIt/GitHub hit
    :alt: GitHub Searches

.. image:: https://img.shields.io/codecov/c/gh/hendrikdutoit/ReleaseIt
    :alt: CodeCov
    :target: https://app.codecov.io/gh/hendrikdutoit/ReleaseIt

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ReleaseIt/Pre-Commit
    :alt: GitHub Actions - Pre-Commit
    :target: https://github.com/hendrikdutoit/ReleaseIt/actions/workflows/pre-commit.yaml

.. image:: https://img.shields.io/github/workflow/status/hendrikdutoit/ReleaseIt/CI
    :alt: GitHub Actions - CI
    :target: https://github.com/hendrikdutoit/ReleaseIt/actions/workflows/ci.yaml

.. image:: https://img.shields.io/testpypi/v/ReleaseIt
    :alt: PyPi

Project Short Description (default ini)

    Project long description or extended summary goes in here (default ini)

=======
Testing
=======

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install - r requirements_test.txt

Run the tests.

.. code-block:: bash

    $ pytest tests
    === XXX passed in SSS seconds ===

==========
Developing
==========

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

.. code-block:: bash

    $ pip install black flake8 pre-commit
    $ pre-commit install

=========
Releasing
=========

Releases are published automatically when a tag is pushed to GitHub.

.. code-block:: bash

    # Set next version number
    export RELEASE = x.x.x
    
    # Create tags
    git commit --allow -empty -m "Release $RELEASE"
    git tag -a $RELEASE -m "Version $RELEASE"
    
    # Push
    git push upstream --tags

