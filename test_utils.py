import pytest

import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)

    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)

    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)

    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "value, expected", [(0, "0"), (1, "1"), (2, "10"), (5, "101"), (100, "1100100")]
)
def test_natural_to_binary(value, expected):
    result = utils.natural_to_binary(value)

    assert result == expected


@pytest.mark.parametrize("value", [-1, 101])
def test_natural_to_binary_out_of_range(value):
    with pytest.raises(ValueError):
        utils.natural_to_binary(value)


@pytest.mark.parametrize("value", [1.5, "3", None, True])
def test_natural_to_binary_not_natural(value):
    with pytest.raises(TypeError):
        utils.natural_to_binary(value)
