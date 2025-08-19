def is_palindrome(s: str) -> bool:
    left: int = 0
    right: int = 0
    right = len(s) - 2
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

input_str: str = ""
input_str = input()

print(input_str)
print(is_palindrome(input_str))