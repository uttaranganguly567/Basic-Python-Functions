def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

if(check_palindrome(input("Enter text: "))):
    print("Palindrome.")
else:
    print("Not palindrome.")