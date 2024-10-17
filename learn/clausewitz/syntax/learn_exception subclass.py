class MyCustomError(Exception):
    def __init__(self, message, extra_data):
        super().__init__(message)
        self.extra_data = extra_data

try:
    # Simulate an error condition
    raise MyCustomError("An error occurred!", {"key": "value"})
except MyCustomError as e:
    print(f"Error: {e}")
    print(f"Extra Data: {e.extra_data}")