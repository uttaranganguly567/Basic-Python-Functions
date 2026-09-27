def find_largest(a, b, c):
    if a > b:
        if a > c:
            print(f"{a} is greatest.")
        else:
            print(f"{c} is greatest.")
    elif b > c:
        if b > a:
            print(f"{b} is greatest.")
        else: 
            print(f"{a} is greatest.")
    else:
        print(f"{c} is greatest.")

find_largest(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))