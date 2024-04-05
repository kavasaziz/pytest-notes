from pytest import mark


@mark.engine
def test_engine_functions_as_expected():
    assert True


@mark.smoke
@mark.engine
def test_fundamental_engine_functions_as_expected(serial_number_from_file):
    print()
    serial_number = serial_number_from_file
    print("initial value", serial_number)
    serial_number.append("hello")
    print("value after append", serial_number)
    assert True
