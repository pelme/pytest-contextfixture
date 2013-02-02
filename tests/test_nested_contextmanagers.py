import pytest
from contextlib import contextmanager


# Keep track on what has been teared down
class TeardownStates(object):
    outer_teardowned = False
    inner_teardowned = False

s = TeardownStates()


@contextmanager
def outer():
    s.outer_teardowned = False
    yield
    print 'tearing down outer'
    assert s.inner_teardowned

    s.outer_teardowned = True


@contextmanager
def inner():
    s.b_teardowned = False
    yield
    print 'tearing down inner'
    assert not s.outer_teardowned

    s.inner_teardowned = True


@pytest.contextfixture
def dependency(request):
    with outer():
        with inner():
            yield 1234
            print 'teardown in fixture'


def test_teardown_order(dependency):
    assert dependency == 1234

    # Make sure the context managers have not been exited
    assert not s.outer_teardowned
    assert not s.inner_teardowned
    print 'exiting test case'
