def count_vowels_consonants(text):
    count = 0
    for _ in text:
        if _ in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(f"Vowels: {count}")

    count = 0
    for _ in text:
        if _ not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(f"Consonants: {count}")

count_vowels_consonants(input("Enter text: "))