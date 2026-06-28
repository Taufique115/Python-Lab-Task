def check_palindrome(text):
    
    reversed_text = text[::-1]
    
    if text == reversed_text:
        return True
    else:
        return False

word = "racecar"
if check_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")