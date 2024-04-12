from pytest import mark
from pytest import xfail


@mark.body
def test_body_functions_as_expected():
    assert True


@mark.smoke
@mark.body
def test_fundamental_body_functions_as_expected(serial_number_from_file):
    print()
    serial_number = serial_number_from_file
    print("initial value", serial_number)
    serial_number.append("hello")
    print("value after append", serial_number)
    assert True


@mark.smoke
@mark.body
@mark.engine
def test_body_engine_compatibility(get_body, get_engine):
    is_compatible = get_body.is_engine_compatible(get_engine)
    if is_compatible:
        print(f"\n{get_body.body_type} is compatible with engine {get_engine.engine_type}")
    else:
        print(f"\n{get_body.body_type} is not compatible with engine {get_engine.engine_type}")

    if not is_compatible and get_body.body_type == 'coupes' and get_engine.engine_type == 'hybrid':
        xfail(reason=f"{get_engine.engine_type} engine is not supported for {get_body.body_type}")
    assert is_compatible
