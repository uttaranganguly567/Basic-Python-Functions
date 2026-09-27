def remove_spaces(text):
    l = []
    for _ in text:
        if _ != " ":
            l.append(_)

    return "".join(l)

text = input("Enter text: ")
print(f"Without spaces: {remove_spaces(text)}")