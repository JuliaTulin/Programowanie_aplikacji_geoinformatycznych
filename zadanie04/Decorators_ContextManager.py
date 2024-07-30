import time
import functools

# Dekorator mierzący czas wykonania funkcji w określonych jednostkach
def exe_time(unit):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if unit == 'seconds':
                print(f"Execution time of function {func.__name__}: {elapsed_time:.6f} seconds")
            elif unit == 'microseconds':
                elapsed_time_micro = elapsed_time * 1_000_000
                print(f"Execution time of function {func.__name__}: {elapsed_time_micro:.6f} microseconds")
            else:
                raise ValueError("Unit must be 'seconds' or 'microseconds'.")
            
            return result
        return wrapper
    return decorator

# przykłady wykorzystania dekoratora
@exe_time(unit='seconds')
def test_seconds():
    for _ in range(1000000):
        pass

@exe_time(unit='microseconds')
def test_microseconds():
    for _ in range(1000000):
        pass

test_seconds()
test_microseconds()
