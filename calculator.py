def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def average(numbers):
   if len(numbers) == 0:
       return None
   return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("add(2,3) =", add(2,3))
    print("divide(10,2) =", divide(10,2))
