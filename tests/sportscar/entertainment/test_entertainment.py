from pytest import mark


@mark.entertainment
def test_entertainment_functions_as_expected(serial_number_from_file):
    print()
    serial_number = serial_number_from_file
    print("initial value", serial_number)
    serial_number.append("hello")
    print("value after append", serial_number)
    assert True
