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
