.. figure:: https://circleci.com/gh/cardforcoin/optional_import.png?circle-token=d834124e03717f6619b867f13c8a85f254298df5
   :alt: Build status

optional_import
===============

Optional imports in Python

.. pypi - Everything below this line goes into the description for PyPI.

Usage
-----

This library contains only the context manager ``optional_import``:

.. code:: python

    from optional_import import optional_import

An import within the ``optional_import`` context fails silently if the
import does not exist.

Example: Optionally importing a module ``foo``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Import ``foo`` is it exists; do nothing otherwise.

.. code:: python

    with optional_import():
        import foo

Example: Optionally importing local settings from Django ``settings.py``:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common pattern in Django is to put default settings in ``settings.py``,
put optional site-specific settings in ``settings_local.py``, and import
``*`` from the local settings file if it exists.

.. code:: python

    with optional_import():
        from .settings_local import *

Why not just catch ``ImportError``?
-----------------------------------

Optional imports can almost be achieved as:

.. code:: python

    try:
        import foo
    except ImportError:
        pass

But this approach is deficient: If ``foo`` exists but raises ``ImportError``,
we want that error to be raised, but instead it is unintentionally swallowed
by the ``except`` clause.
