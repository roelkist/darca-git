====================
Darca Git
====================

**Darca Git** is a lightweight abstraction over Git CLI commands, built to integrate with `darca-executor` and the Darca ecosystem.

- 🔗 No dependency on `gitpython`
- 🔐 Runs shell-safe commands via `darca-executor`
- 🧪 100% tested with `pytest`
- 🧰 Integrated with darca-space-git for space-aware Git

Installation
============

Clone and install the project using:

.. code-block:: bash

    make install

Usage
=====

.. code-block:: python

    from darca_git.git import Git

    git = Git()
    git.init("/your/repo")
    git.status("/your/repo")

Testing
=======

Run tests with full coverage:

.. code-block:: bash

    make test

Documentation
=============

Docs are built with Sphinx:

.. code-block:: bash

    make docs

Pre-commit Hooks
================

Check formatting, linting and more with:

.. code-block:: bash

    make precommit

Full quality check:

.. code-block:: bash

    make check
