def character_frequency(text, ch):
    count = 0
    for _ in text:
        if _ == ch:
            count += 1

    return count

text = input("Enter text: ")
ch = input("Enter character: ")

print(f"The number of times '{ch}' appeared in '{text}' is {character_frequency(text, ch)}")