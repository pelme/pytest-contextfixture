
import pytest
from contextlib import contextmanager
from functools import wraps

def pytest_namespace():
    # TODO: Make it possible to pass standard pytest.fixture args here too, like scope, params etc..
    def contextfixture(fn):
        ctxmgr = contextmanager(fn)

        @pytest.fixture
        @wraps(fn)
        def actual_fixture(request, scope='function'):
            ctxinst = ctxmgr()

            # TODO: Proper exception propagation?
            request.addfinalizer(lambda: ctxinst.__exit__(None, None, None))
            return ctxinst.__enter__()

        return actual_fixture

    return {'contextfixture': contextfixture]

    # pytest.contextfixture = pytest_contextfixture

