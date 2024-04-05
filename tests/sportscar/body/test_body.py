from pytest import mark


@mark.body
def test_body_functions_as_expected():
    assert True


@mark.smoke
@mark.body
def test_fundamental_body_functions_as_expected():
    assert True
