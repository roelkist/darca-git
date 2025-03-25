===========
Usage Guide
===========

Darca Git provides a structured interface to manage Git repositories using CLI commands through `darca-executor`.

Installation
============

Install the dependencies and virtual environment with:

.. code-block:: bash

    make install

Basic Git Operations
====================

.. code-block:: python

    from darca_git.git import Git

    git = Git()
    cwd = "/your/repo"

    git.init(cwd)
    git.clone("https://github.com/example/repo.git", cwd)
    git.status(cwd)
    git.commit("Initial commit", cwd)

Dry Run Mode
============

To simulate changes (in darca-space-git), use the `dry_run=True` option on supported methods like `checkout`.

Running Tests
=============

.. code-block:: bash

    make test
