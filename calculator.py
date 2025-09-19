# calculator.py

def add(a, b):
    # BUG: should be a + b
    return a - b  

def subtract(a, b):
    # BUG: should be a - b
    return a + b  

def multiply(a, b):
    return a * b  

def divide(a, b):
    # BUG: does not handle division by zero
    return a / b  

if __name__ == "__main__":
    print("Calculator Demo")
    print("Add 10 and 5:", add(10, 5))          # Expected 15
    print("Subtract 10 and 5:", subtract(10, 5)) # Expected 5
    print("Multiply 10 and 5:", multiply(10, 5)) # Expected 50
    print("Divide 10 by 0:", divide(10, 0))      # Should handle error
