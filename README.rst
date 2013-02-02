pytest-contextfixture makes it possible to define pytest fixtures as context managers.

A contextfixture works like a standard fixture, but it allows the
definition to be written as a generator. This simplifies the teardown
code and allows for other context managers to be used within a fixture.

Installation
============

pip install pytest-contextfixture



Usage
=====

Consider this example, using the standard `pytest.fixture`::

    import pytest

    @pytest.fixture
    def dependency(request)
        def teardown():
            # fixture teardown code goes here
        request.addfinalizer(teardown)

        return 1234

    def test_foo(dependency):
        assert fn_under_test(dependency) == 'expected'


With `pytest.contextfixture`, this is equivalent::

    import pytest

    @pytest.contextfixture
    def dependency(request):
        # fixture setup code goes here
        yield 1234
        # fixture teardown code goes here

    def test_foo(dependency):
        assert fn_under_test(dependency) == 'expected'


While this is a slightly nicer syntax, when using other context managers
to get a dependency for a fixture, this becomes more useful::

    @pytest_contextfixture
    def dependency(request):
        with setup_something():
            with setup_something_else() as d:
                yield d

    def test_foo(dependency):
        assert fn_under_test(dependency) == 'expected'

test_foo will then run in the context of setup_something and
setup_something_else.
