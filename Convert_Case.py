def convert_uppercase(text):
    return text.upper()

text = input("Enter text: ")
print(f"Uppercase: {convert_uppercase(text)}")

def convert_uppercase(text):
    l = []
    for _ in text:
        l.append(_.upper())

    return "".join(l)

text = input("Enter text: ")
print(f"Uppercase: {convert_uppercase(text)}")