

def is_palindrome(s: str) -> bool:
    start: int = 0
    end: int = 0
    end = len(s) - 2
    while start < end:
        if s[start] != s[end]:
            return False
        start = start + 1
        end = end - 1
    
    return True
print(is_palindrome(input()))