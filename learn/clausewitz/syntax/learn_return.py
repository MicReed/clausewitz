from returns.result import Result, safe

# @safe decorator captures all exceptions, not just ZeroDivisionError. This means that if any other kind of exception occurs within the divide function, it would also be captured and stored in a Failure instance, rather than being raised. 
@safe
def divide(a: int, b: int) -> Result[int, ZeroDivisionError]:
    '''
    Result[+ValueType, +ErrorType] is a type hint that represents a value that can be either a success or a failure.
    in this case, the returned result would be expected to be either a int when running successfully or a ZeroDivisionError that stored as return.result.Failure type when failing.
    
    '''
    return a / b

c= divide(5, 2)
print(type(c))