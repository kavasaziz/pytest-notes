class Engine:
    SUPPORTED_ENGINE_TYPES = ["electrical", "diesel", "hybrid"]


    def __init__(self, engine_type):
        if engine_type is None:
            raise ValueError("engine_type can't be None")

        self.engine_type = engine_type.lower()

        if self.engine_type not in self.SUPPORTED_ENGINE_TYPES:
            raise ValueError(f"{engine_type} is not amoung supported engine types: {self.SUPPORTED_ENGINE_TYPES}")

        self.engine = {
            "electrical": "Electrical Engine",
            "diesel": "Diesel Engine",
            "hybrid": "Hybrid Engine",
        }[self.engine_type]



    def engine_run_fundamental_functions(self, serial_numbers):
        print(f"Engine type is {self.engine_type}")
        print("initial value", serial_numbers)
        if ("electrical" == self.engine_type):
            serial_numbers.append("hello")
            print("value after append", serial_numbers)

        return True


class Body:
    SUPPORTED_BODY_TYPES = ["coupes", "cabriolets"]


    def __init__(self, body_type, supported_engines):
        if body_type is None:
            raise ValueError("body_type can't be None")

        self.body_type = body_type.lower()

        if self.body_type not in self.SUPPORTED_BODY_TYPES:
            raise ValueError(f"{body_type} is not amoung supported body types: {self.SUPPORTED_BODY_TYPES}")

        self.body = {
            "coupes": "coupes body",
            "cabriolets": "cabriolets body",
        }[self.body_type]

        self.supported_engines = supported_engines[self.body_type]


    def is_engine_compatible(self, engine):
        if engine.engine_type in self.supported_engines:
            return True
        return False

import time

class Battery:

    SUPPORTED_BATTERY_TYPES = ["alpha", "gamma", "prime"]


    def __init__(self, battery_info):
        if battery_info["type_info"] is None:
            raise ValueError("body_type can't be None")

        self.type_info = battery_info["type_info"].lower()

        if self.type_info not in self.SUPPORTED_BATTERY_TYPES:
            raise ValueError(f"{self.type_info} is not amoung supported body types: {self.SUPPORTED_BATTERY_TYPES}")

        self.battery_interface = {
            "alpha": "INTERFACE_A",
            "gamma": "INTERFACE_G",
            "prime": "INTERFACE_P"
        }[self.type_info]

        self.capacity = int(battery_info["capacity"])


    def battery_measure_cell_health(self):
        time.sleep(self.capacity)
        return True
