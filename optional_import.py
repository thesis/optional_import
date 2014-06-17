from contextlib import contextmanager
import sys


@contextmanager
def optional_import():
    """
    Example- Import foo if it exists, do nothing otherwise:

        with optional_import():
            import foo

    The advantage of using this instead of

        try:
            import foo
        except ImportError:
            pass

    is that it doesn't swallow any ImportError that might be raised
    from foo.
    """

    try:
        yield
    except ImportError:
        #
        # The trace has depth at least two (1- yield; 2- import).
        #
        # If the depth is exactly 2, then the import failed directly
        # (`import foo` where `foo` does not exist), which is okay
        # because `foo` is an optional import.
        #
        # If the depth is greater than 2, then the ImportError came
        # from somewhere else, so it needs to be raised.
        #
        if sys.exc_info()[-1].tb_next.tb_next:
            raise
