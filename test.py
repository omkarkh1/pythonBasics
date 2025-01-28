def test_1():
    assert 1 == 1

## Failing test

# def test_2():
#     assert 2 == 1

#assert a == b
#assert a!=b
#assert a
#assert not a
#assert element in list
#assert element not in list


import pytest

@pytest.fixture
def sample_fixture():
    return "Hello, pytest!"

def test_example(sample_fixture):
    assert sample_fixture == "Hello, pytest!"
