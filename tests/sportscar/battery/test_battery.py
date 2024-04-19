from pytest import mark


@mark.battery
class BatteryTests:
    @mark.smoke
    def test_fundamental_battery_functions_as_expected(self, serial_number_from_file):
        print()
        serial_number = serial_number_from_file
        print("initial value", serial_number)
        serial_number.append("hello")
        print("value after append", serial_number)
        assert True

    @mark.smoke
    def test_other_fundamental_battery_functions_as_expected(self, serial_number_from_file):
        print()
        serial_number = serial_number_from_file
        print("initial value", serial_number)
        serial_number.append("hello")
        print("value after append", serial_number)
        assert True

    @mark.smoke
    def test_battery_units_health(self, get_battery_unit):
        assert True == get_battery_unit.battery_measure_cell_health()


    def test_battery_functions_as_expected(self):
        assert True
