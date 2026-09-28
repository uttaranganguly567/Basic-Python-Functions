def count_consonants(text):
    count = 0
    for _ in text:
        if _ not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

text = input("Enter the text: ")
print(f"The number of consonants in {text} are {count_consonants(text)}.")