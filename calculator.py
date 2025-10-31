def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ^ b

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / (len(numbers) - 1)

if __name__ == "__main__":
    print("Demo: 10 / 0 =", divide(10, 0))
