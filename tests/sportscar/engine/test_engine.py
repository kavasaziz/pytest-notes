from pytest import mark


@mark.engine
def test_engine_functions_as_expected():
    assert True


@mark.smoke
@mark.engine
def test_fundamental_engine_functions_as_expected(serial_number_from_file, get_engine):
    assert True == get_engine.engine_run_fundamental_functions(serial_number_from_file)


@mark.xfail(reason="Broken after release train #")
@mark.engine
def test_engine_type_diesel(get_engine_type):
    print("\nxfail test is executed")
    assert "diesel" == get_engine_type


@mark.skip(reason="Not a compatible test case")
@mark.engine
def test_engine_type_electrical(get_engine_type):
    print("\nskip test is not executed")
    assert "electrical" == get_engine_type


@mark.xfail(reason="This future should be deprecated after release trian #")
@mark.engine
def test_engine_deprecated_future(get_engine_type):
    assert False
