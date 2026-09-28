def remove_vowels(text):
    l = []
    for _ in text:
        if _ not in ['a', 'e', 'i', 'o', 'u']:
            l.append(_)
    return "".join(l)

print(f"{remove_vowels(input("Enter text: "))}")