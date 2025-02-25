import random

from helpers.helpers import Helpers
from api.apis import Apis

import pytest
import sys
from unittest.mock import patch
from main import main


#main function tests
@pytest.mark.parametrize("args, expected_output", [
    (["main.py", "--locations", "Madison, WI"], ["Madison, Wisconsin, US, 43.074761, -89.3837613"]),
    (["main.py", "--locations", "95126"], ["San Jose, US, 37.3249, -121.9153"]),
    (["main.py", "--locations", "99999"], ["99999 is a wrong zip code"]),
    (["main.py", "--locations", "NonExistentCity"], ["NonExistentCity is a wrong location"]),
    (["main.py", "--locations", ""], ["Location/zip code is required"]),
    (["main.py", "--locations", "95126", "Madison, WI"], ["San Jose, US, 37.3249, -121.9153", "Madison, Wisconsin, US, 43.074761, -89.3837613"])
])
def test_main_function_happy_path(args, expected_output):
    with patch.object(sys, "argv", args):
        output = main()
        assert output == expected_output

def test_multiple_locations():
    args_list = ["main.py", "--locations"]
    number_of_inputs = random.randint(1, 15)
    args_list.extend(["94107"]*number_of_inputs)
    with patch.object(sys, "argv", args_list):
        output = main()
        assert len(output) == number_of_inputs


#api tests
zip_data={"95126":{'country': 'US','latitude': 37.3249,'longitude': -121.9153,'place_name': 'San Jose','state': None},
          "94107":{'place_name': 'San Francisco', 'state': None, 'country': 'US', 'latitude': 37.7621, 'longitude':
              -122.3971}}

location_name_data={"Madison, WI":{'country': 'US','latitude': 43.074761,'longitude': -89.3837613,'place_name': 'Madison','state': 'Wisconsin'},
                    "Redwood city, CA":{'country': 'US', 'latitude': 37.4863239,'longitude': -122.232523,'place_name': 'Redwood City','state': 'California'}}

@pytest.mark.parametrize("zip", zip_data)
def test_api_get_coordinates_by_zip_happy_path(zip):
    assert Apis.api_get_coordinates_by_zip(zip) == zip_data[zip]

@pytest.mark.parametrize("location_name", location_name_data)
def test_api_get_coordinates_by_location_name_happy_path(location_name):
    assert Apis.api_get_coordinates_by_location_name(location_name) == location_name_data[location_name]


def test_api_get_coordinates_by_zip_with_no_authorisation():
    assert Apis.api_get_coordinates_by_zip("95126", is_api_key=False) == 401

def test_api_get_coordinates_by_location_name_with_no_authorisation():
    assert Apis.api_get_coordinates_by_location_name("Madison, WI", is_api_key=False) == 401

def test_api_get_coordinates_by_zip_with_wrong_zip():
    assert Apis.api_get_coordinates_by_zip("1") == 400
    assert Apis.api_get_coordinates_by_zip("") == 400

def test_api_get_coordinates_by_location_name_with_wrong_location_name():
    assert Apis.api_get_coordinates_by_location_name("MadisonWI") == "Location not found"
    assert Apis.api_get_coordinates_by_location_name("Madiso") == "Location not found"

#helpers tests

helpers_zip_data={"95126":'San Jose, US, 37.3249, -121.9153',
                  "94107":'San Francisco, US, 37.7621, -122.3971'}

helpers_location_name_data={"Madison, WI":'Madison, Wisconsin, US, 43.074761, -89.3837613',
                    "Redwood city, CA":'Redwood City, California, US, 37.4863239, -122.232523'}
@pytest.mark.parametrize("zip", helpers_zip_data)
def test_helper_get_coordinates_by_zip_happy_path(zip):
    assert Helpers.get_coordinates_by_zip_code(zip) == helpers_zip_data[zip]

@pytest.mark.parametrize("location_name", helpers_location_name_data)
def test_helper_get_coordinates_by_location_happy_path(location_name):
    assert Helpers.get_coordinates_by_location_name(location_name) == helpers_location_name_data[location_name]


def test_helper_get_coordinates_by_zip_with_wrong_zip_code():
    assert Helpers.get_coordinates_by_zip_code("99999") == '99999 is a wrong zip code'
def test_helper_get_coordinates_by_location_name_with_wrong_name():
    assert Helpers.get_coordinates_by_location_name("fsqfws") == 'fsqfws is a wrong location'

