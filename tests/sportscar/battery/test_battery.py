from pytest import mark


@mark.battery
class BatteryTests:
    @mark.smoke
    def test_fundamental_battery_functions_as_expected(self):
        assert True


    def test_battery_functions_as_expected(self):
        assert True
