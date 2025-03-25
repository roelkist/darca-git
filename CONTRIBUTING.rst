=======================
Contributing Guidelines
=======================

We welcome contributions to **darca-git** — from bug fixes to features and docs!

Workflow
========

1. Fork the repository
2. Create a feature branch:

   .. code-block:: bash

      git checkout -b feature/your-feature

3. Install dependencies:

   .. code-block:: bash

      make install

4. Make your changes and run:

   .. code-block:: bash

      make check

5. Push your branch and open a **Pull Request**.

Branch Naming
=============

- `feature/your-feature` for features
- `fix/your-bug` for bug fixes
- `docs/your-doc-change` for docs

Pull Requests
=============

All PRs must:

- Pass `make check` (format, tests, docs)
- Include meaningful tests if applicable
- Follow project style (PEP8 via `black` and `isort`)

Tips
====

- Use `make` targets to automate tasks
- Use `make debug` to inspect your local setup
- Ask questions, open discussions — we're happy to help!

