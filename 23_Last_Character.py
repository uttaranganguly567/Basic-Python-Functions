def last_character(text):
    return text[-1]

text = input("Enter text: ")
print(f"The last character of {text} is {last_character(text)}")

def last_character(text):
    for i in range(len(text) -1, 0, -1):
        c = text[i]
        break
    
    return c

text = input("Enter text: ")
print(f"The last character of {text} is {last_character(text)}")