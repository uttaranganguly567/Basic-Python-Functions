def count_case(text):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    for _ in text:
        if _.isupper():
            upper_count += 1
        elif _.islower():
            lower_count += 1
        elif _.isdigit():
            digit_count += 1
        elif _ == " ":
            space_count += 1

    print(f"Upper Case Count: {upper_count}\nLower Case Count: {lower_count}\nDigit Count: {digit_count}\nSpace Count: {space_count}")

count_case(input("Enter text: "))