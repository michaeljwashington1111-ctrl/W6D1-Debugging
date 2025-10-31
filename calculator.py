def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    # BUG: No zero check → ZeroDivisionError when b == 0
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
    # BUG: XOR (^) instead of exponent (**)
    return a ^ b

def average(numbers):
    # BUG: divides by len(numbers)-1
    total = 0
    for n in numbers:
        total += n
    return total / (len(numbers) - 1)

if __name__ == "__main__":
    print("Demo: 10 / 0 =", divide(10, 0))  # triggers traceback
