from gamutin.core.mathing import remap


def test_remap_1():
    initial_value = 0.5
    result = remap(initial_value, 0, 1, 0.5, 1.0)
    assert result == 0.75

    initial_value = 0.5
    result = remap(initial_value, 0, 1, -10, 10)
    assert result == 0.0

    initial_value = 0.0
    result = remap(initial_value, -10, 10, 0, 1)
    assert result == 0.5
