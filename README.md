# `optional_import`: Optional imports in Python

## Usage

This library has one function:

```python
from optional_import import optional_import
```

### Example: Optionally importing a module `foo`

Import `foo` is it exists; do nothing otherwise.

```python
with optional_import():
    import foo
```

### Example: Optionally importing local settings from Django `settings.py`:

A common pattern in Django is to put default settings in `settings.py`,
put optional site-specific settings in `settings_local.py`, and import `*`
from the local settings file if it exists.

```python
with optional_import():
    from .settings_local import *
```

## Why not just catch `ImportError`?

Optional imports can almost be achieved as:

```python
try:
    import foo
except ImportError:
    pass
```

But this approach is deficient: If `foo` exists but raises `ImportError`,
we want that error to be raised, but instead it is unintentionally
swallowed by the `except` clause.
