from scripts.chp2.video4.mapmaker_challenge import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp1:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp1.value) == "Invalid latitude, longitude combination."

    with pytest.raises(TypeError) as exp2:
        Point(123, 70.2356, -90.0000)
    assert str(exp2.value) == "Invalid name datatype."
