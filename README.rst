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

    >>> from optional_import import optional_import

A successful import works as usual:

.. code:: python

    >>> with optional_import():
    ...     import collections
    >>> type(collections)
    <type 'module'>

If the import does not exist, ``optional_import`` suppresses the
``ImportError`` that would otherwise be raised.

.. code:: python

    >>> import unicorns
    Traceback (most recent call last):
      ...
    ImportError: No module named unicorns

    >>> with optional_import():
    ...     import unicorns

    >>> unicorns
    Traceback (most recent call last):
      ...
    NameError: name 'unicorns' is not defined


Example: Django local settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common pattern in Django is to put default settings in ``settings.py``,
put optional site-specific settings in ``settings_local.py``, and import
``*`` from the local settings file if it exists.

.. code:: python

    with optional_import():
        from .settings_local import *


Why not just catch ``ImportError``?
-----------------------------------

Optional imports can almost be achieved simply by catching ``ImportError``:

.. code:: python

    try:
        import foo
    except ImportError:
        pass

But this approach introduces a problem: If ``foo`` exists but raises
``ImportError``, we want that error to be raised, but instead it is
swallowed by the ``except`` clause.

With ``optional_import``, the error is raised as desired. In the following
example, the ``bad`` module tries to import a nonexistent package ``unicorns``:

.. code:: python

    >>> with optional_import():
    ...     import bad
    Traceback (most recent call last):
      ...
    ImportError: No module named unicorns
