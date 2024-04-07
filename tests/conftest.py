import re
from pytest import fixture

from config import Engine


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


def pytest_addoption(parser):
    parser.addoption(
        "--engine-type",
        action="store",
        # default="diesel", # not suggested for real-life practices
        # dest='engine_type',
        help="Engine type for the vehicle under test"
    )


@fixture(scope='session')
def get_engine_type(request):
    return request.config.getoption("--engine-type")


@fixture(scope='session')
def get_engine(get_engine_type):
    engine = Engine(get_engine_type)
    print(f"\n{engine.engine} created")
    yield engine
    print(f"\n{engine.engine} destroyed")
