from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Dakar", 14.1234, 17.3456)
    assert p1.get_lat_long() == (14.1234, 17.3456)
