def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fibonacci(n):
    if n < 0:
        return "Fibonacci is not defined for negative indices."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def menu():
    while True:
        print("\nMenu:")
        print("1. Calculate factorial of a number")
        print("2. Find GCD of two positive numbers")
        print("3. Find nth term of Fibonacci series")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            num = int(input("Enter a number: "))
            print("Factorial of",num,"=",factorial(num))
        
        elif choice == '2':
            a = int(input("Enter the first positive number: "))
            b = int(input("Enter the second positive number: "))
            print("GCD of",a,"and",b,"=",gcd(a,b))
        
        elif choice == '3':
            n = int(input("Enter the term index (n): "))
            print("The",n,"th term of the Fibonacci series =" ,fibonacci(n))
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

menu()
