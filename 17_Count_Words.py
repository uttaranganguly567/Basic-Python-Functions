def count_words(text):
    count = 0
    for _ in text:
        if _ == " ":
            count += 1
    count += 1
    return count

text = input("Enter text: ")
print(f"The number of words in '{text}' is {count_words(text)}")