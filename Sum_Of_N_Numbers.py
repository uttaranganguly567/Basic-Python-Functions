def sum_natural(n):
    sum = 0
    for _ in range(1, n+1):
        sum += _
    print (f"The sum is {sum}")

sum_natural(int(input("Enter range: ")))