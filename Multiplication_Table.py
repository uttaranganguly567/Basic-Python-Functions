def multiplication_table(n):
    for _ in range(1, 11):
        print(f"{n} * {_} = {n * _}")

multiplication_table(int(input("Enter the number: ")))