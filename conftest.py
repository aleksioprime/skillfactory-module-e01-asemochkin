import pytest

@pytest.fixture(params=['a', 'b', 'c', 'd'])
def letters(request):
    return request.param