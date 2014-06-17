import sure

from optional_import import optional_import


def test_good():
    """
    Import `good`. Should work normally.
    """

    with optional_import():
        from . import good

    good.x.should.equal(42)


def test_bad():
    """
    Try to import `bad`, which exists but raises `ImportError`
    when  imported. The `ImportError` should be re-raised.
    """

    def a():
        with optional_import():
            from . import bad

    a.should.throw(ImportError)


def test_nonexistent():
    """
    Try to import a module that doesn't exist. Should not raise.
    """

    with optional_import():
        from . import omgwtfbbq
