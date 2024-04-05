from pytest import fixture
import re


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
