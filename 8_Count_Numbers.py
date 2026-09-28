def count_digits(n):
    if n == 0:
        return 1

    n = abs(n)
    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count

n = int(input("Enter the number: "))
print(f"The number of digits in {n} is {count_digits(n)}.")