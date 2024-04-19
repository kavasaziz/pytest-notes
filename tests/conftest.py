import re
import json

from pytest import fixture

from config import Body
from config import Engine
from config import Battery

# function is the default scope
@fixture(scope='module')
def serial_number_from_file():
    with open('sample_file.txt', 'r') as file:
        sample_string = file.read()

    # Define the regex pattern to match MAC addresses
    pattern = r"SerialNumber=[0-9]+"

    # Find all matches of the pattern in the string
    matches = re.findall(pattern, sample_string)

    # Extract MAC addresses from matches
    serial_number = [match.split('=')[1] for match in matches]
    return serial_number


# Add parsers for cli arguments
def pytest_addoption(parser):
    # default values not suggested for real-life practices
    options = [
        ("--engine-type", "diesel", "Engine type for the vehicle under test"),
        ("--config", "config.json", "Path of config file"),
    ]

    for option, default, help_msg in options:
        parser.addoption(
            option,
            action="store",
            default=default,
            help=help_msg
        )


# cli argument return options
@fixture(scope='session')
def get_engine_type(request):
    return request.config.getoption("--engine-type")


@fixture(scope='session')
def get_config_path(request):
    return request.config.getoption("--config")


TEST_DATA_PATH = "test_data/test_data.json"


def load_test_data(path=TEST_DATA_PATH):
    with open(path) as test_data_file:
        return json.load(test_data_file)


# Test instances used throughout the test execution
@fixture(scope='session')
def get_engine(get_engine_type):
    engine = Engine(get_engine_type)
    print(f"\n{engine.engine} created")
    yield engine
    print(f"\n{engine.engine} destroyed")


@fixture(scope="session")
def get_config(get_config_path):
    with open(get_config_path) as config_file:
        yield json.load(config_file)


@fixture(scope="session", params=load_test_data()["body_types"])
def get_body_list(request):
    body_type = request.param
    yield body_type


@fixture(scope="module")
def get_body(get_body_list, get_config):
    body_type = get_body_list
    body_instance = Body(body_type, get_config["supported_engines"])
    yield body_instance


@fixture(scope="session", params=load_test_data()["battery_units"])
def get_battery_info(request):
    battery_unit = request.param
    yield battery_unit


@fixture(scope="module")
def get_battery_unit(get_battery_info):
    battery_info = get_battery_info
    battery_unit = Battery(battery_info)
    yield battery_unit
