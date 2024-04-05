from pytest import mark


@mark.engine
def test_engine_functions_as_expected():
    assert True


@mark.smoke
@mark.engine
def test_fundamental_engine_functions_as_expected():
    assert True
