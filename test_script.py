# An example of a test script that can be run with the DysPython interpreter

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    # Test basic arithmetic
    print("2 + 2 =", 2 + 2)
    
    # Test string manipulation
    name = "Alice"
    age = 30
    print(f"{name} is {age} years old")
    
    # Test loop
    for i in range(5):
        print(f"Loop iteration {i}")
    
    # Test conditional
    x = 10
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    
    # Test function calls
    print("Factorial of 5:", factorial(5))
    print("10th Fibonacci number:", fibonacci(10))
    
    # Test list comprehension
    squares = [x**2 for x in range(5)]
    print("Squares:", squares)
    
    # Test exception handling
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught zero division error")

if __name__ == "__main__":
    main()