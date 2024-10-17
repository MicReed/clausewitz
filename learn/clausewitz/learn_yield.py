import time
from typing import Callable

def time_count(func:Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {str(func.__name__)}: {end_time - start_time} seconds")
    return wrapper

@time_count
def get_numbers_yield(loop_range):
    def filter_divisible(numbers, divisor):
        for number in numbers:
            if number % divisor != 0:
                yield number  # Yield numbers not divisible by divisor

    # Example usage
    numbers = list(range(1,loop_range+1))
    divisor = 2

    filtered_numbers = filter_divisible(numbers, divisor)
    # print(type(filtered_numbers))  # <class 'generator'>

    for number in filtered_numbers:
        # print(number)
        pass

@time_count
def get_numbers(loop_range):
    def filter_divisible(numbers, divisor):
        results = []
        for number in numbers:
            if number % divisor != 0:
                results.append(number)  # Append numbers not divisible by divisor
        return results

    # Example usage
    numbers = list(range(1,loop_range+1))
    divisor = 2

    filtered_numbers = filter_divisible(numbers, divisor)
    # print(type(filtered_numbers))  # <class 'generator'>

    for number in filtered_numbers:
        pass

# get_numbers(100000000)
get_numbers_yield(100000000)