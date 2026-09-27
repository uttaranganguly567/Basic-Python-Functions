def factorial(n):
    fact = 1
    for _ in range(1, n+1):
        fact *= _
    return fact

n = int(input("Enter the number: "))
print(f"The factorial of {n} is {factorial(n)}.")