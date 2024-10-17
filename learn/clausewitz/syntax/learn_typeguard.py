from typeguard import typechecked

@typechecked
def add_numbers(a: int, b: int) -> int:
    return a + b

# Correct usage
print(add_numbers(1, 2))  # Output: 3

# Incorrect usage, will raise a TypeError because 'b' is not an int
print(add_numbers(1, '2'))