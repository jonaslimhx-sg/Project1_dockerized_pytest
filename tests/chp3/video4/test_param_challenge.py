from io import StringIO
import os
import pytest

from scripts import data_processor, data_aggregator


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        for f in files:
            if file_name_or_type in f:
                if file_name_or_type != '.json':
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data

    yield _specify_type


@pytest.mark.parametrize("country,stat,value", [
    ('Andorra', 'Mean', 1641.42),
    ('Andorra', 'Median', 1538.02),
    ('Argentina', 'Median', 125.0)
])
def test_csv_writer(process_data, country, stat, value):
    """
     TO DO: Update the function to be parametrized with 3 scenarios:
     ('Andorra', 'Mean', 1641.42),
     ('Andorra', 'Median', 1538.02),
     ('Argentina', 'Median', 125.0),

    Hint:
    - In the final assertion, you will need to use an f-string to inject the
      arguments into the final string.

    - For example: f'{stat} would inject the string statistic that we use for
      the csv writer.
    """
    data = process_data(file_name_or_type="clean_map.csv")
    country_res = data_aggregator.atitude_stat_per_country(data, country, stat)
    # country_res is a dict
    # output_locatiion is a file
    output_location = StringIO()
    # .csv_writer opens the file and writes country_res into it.
    data_aggregator.csv_writer(country_res, output_location)

    res = output_location.getvalue().strip('\r\n')
    assert res == 'Country,{0}\r\n{1},{2}'.format(stat, country, value)
