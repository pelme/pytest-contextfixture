

import pytest


class InitCounter(object):
    count = 0

    def count_and_check(self):
        self.count += 1
        assert self.count == 1
counter = InitCounter()


@pytest.contextfixture(scope='session')
def fixture_with_args(request):
    # Make sure this fixture is only initiated once
    counter.count_and_check()
    yield 1234


@pytest.contextfixture
def fixture_without_args(request):
    yield 5678


def test_fixture_args(fixture_with_args):
    assert fixture_with_args == 1234


def test_fixture_args_again(fixture_with_args):
    assert fixture_with_args == 1234


def test_basic(fixture_without_args):
    assert fixture_without_args == 5678
