def check_prime(n):
    if n <= 1:
        return False
    limit = int(n ** 0.5)

    for _ in range(2, limit + 1):
        if n % _ == 0:
            return False

    return True

if (check_prime(int(input("Enter the number: ")))):
    print("Prime Number.")

else:
    print("Not Prime.")