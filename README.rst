pytest-contextfixture makes it possible to define pytest fixtures as context managers.

Installation
============

```

pip install pytest-contextfixture

```


Usage
=====

```
@pytest_contextfixture
def dependency(request):
    with setup_something():
        with setup_something_else() as d:
            yield d

def test_foo(dependency):
    assert fn_under_test(dependency) == 'expected'

```

