from datetime import datetime
from time import sleep

def timekeeper_decorator(func):
    def wrapper(*args, **kwargs):
        before = datetime.now()
        result = func(*args, **kwargs)
        print(f"{func.__name__} applied for {(datetime.now() - before).total_seconds()} seconds")
        return result
    return wrapper

@timekeeper_decorator
def quick_arithmetic_sum(sequence):
    count = len(sequence)
    return (sequence[0] + sequence[count-1]) * count / 2

@timekeeper_decorator
def arithmetic_sum(sequence):
    summ = 0
    for num in sequence:
        summ += num
    return summ

count_range = 10000000
list_numbers = [num for num in range(1, count_range)]

print(quick_arithmetic_sum(list_numbers))
print(arithmetic_sum(list_numbers))

