from pytest import mark


@mark.engine
def test_engine_functions_as_expected():
    assert True


@mark.smoke
@mark.engine
def test_fundamental_engine_functions_as_expected(serial_number_from_file, get_engine):
    assert True == get_engine.engine_run_fundamental_functions(serial_number_from_file)
