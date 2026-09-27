def reverse_string(text):
    new_text = []
    for _ in range(len(text) - 1 , -1, -1):
        new_text.append(text[_])
    return "".join(new_text)

text = input("Enter text: ")
print(f"The reverse of {text} is {reverse_string(text)}")

def reverse_string(text):
    return text[::-1]

text = input("Enter text: ")
print(f"The reverse of {text} is {reverse_string(text)}")