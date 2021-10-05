import pytest
from scripts import data_processor, map_population_update


@pytest.fixture(scope="session")
def get_path():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="function")
def get_object_dict(get_path):
    data = data_processor.csv_reader(get_path)
    data_to_transform = map_population_update.MapData(data, False)
    population_dict = {
            'Andorra': 77142,
            'Argentina': 44780677,
            'Cape Verde': 546388,
            'Germany': 83670653,
            'Greece': 10473455,
            'India': 1366417754,
            'Japan': 128860301,
            'Morocco': 36471769,
            'Senegal': 16296364,
            'United States': 329064917
    }
    yield data_to_transform, population_dict


def test_data_population_update(get_object_dict):
    """
    Happy Path test
    """
    data_to_transform, population_dict = get_object_dict
    data_to_transform.add_population(population_dict)
    for row in data_to_transform.get_data():
        assert 'Population' in row
        assert 'Updated' in row


def test_data_population_no_update(get_object_dict):
    """
    Sad Path test: We don't want the data transformed twice

    """
    data_to_transform, population_dict = get_object_dict
    data_to_transform.add_population(population_dict) # first transform
    # Try calling the function again
    with pytest.raises(Exception) as e:
        data_to_transform.add_population(population_dict) # trigger error on second transform
    assert str(e.value) == 'You cannot transform the data twice'
