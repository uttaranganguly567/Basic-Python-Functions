def count_characters(text):
    count = 0
    for _ in text:
        count += 1

    return count

text = input("Enter text: ")
print(f"The number of letters in {text} is {count_characters(text)}")