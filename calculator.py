def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b

def sum_evens(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total

