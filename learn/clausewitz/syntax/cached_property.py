from cached_property import cached_property
import time

class MyClass:
    def __init__(self,value):
        self._value = value

    
    # set once on first access and then cached
    # The cached_property decorator in Python is used to create a property whose value is computed once upon first access and then cached as a regular attribute for the life of the instance.
    @cached_property
    def expensive_computation(self):
        # Simulate an expensive computation
        time.sleep(2)  # Sleep for 2 seconds to simulate computation time
        result = self._value * 2  # Example computation
        return result

# Usage
a = MyClass(5)
start_time = time.time()
print(a.expensive_computation)  # This will take around 2 seconds
print(f"First call took {time.time() - start_time} seconds.")

start_time = time.time()
print(a.expensive_computation)  # This will be instant
print(f"Second call took {time.time() - start_time} seconds.")