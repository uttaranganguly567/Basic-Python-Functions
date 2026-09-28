def first_character(text):
    for _ in text:
        c = _
        break

    return c

text = input("Enter text: ")
print(f"First character of {text} is {first_character(text)}")