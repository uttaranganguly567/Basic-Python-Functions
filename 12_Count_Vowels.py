def count_vowels(text):
    count = 0
    for _ in text:
        if _ in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

text = input("Enter the text: ")
print(f"The number of vowels in {text} are {count_vowels(text)}.")