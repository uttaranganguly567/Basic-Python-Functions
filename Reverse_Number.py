def reverse_number(n):
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev

n = int(input("Enter the number: "))
print(f"The reverse of {n} is {reverse_number(n)}.")