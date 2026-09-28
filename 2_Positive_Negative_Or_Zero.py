def check_number(n):
    if n == 0:
        print("Zero.")
    elif n > 0:
        print("Positive Number.")
    elif n < 0:
        print("Negative Number.")

check_number(int(input("Enter a number: ")))