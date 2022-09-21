text_ = "rotator"
def is_palindrome(x):
    if x == x[::-1]:
        return "True"
    else:
        return "False"

print(is_palindrome(text_))