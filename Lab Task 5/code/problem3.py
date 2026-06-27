def is_palindrome(s):
   
    return s == s[::-1]


user_input = input("Enter a word or string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")