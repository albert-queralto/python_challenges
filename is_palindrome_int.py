def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    
    while x != 0:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10
    
    return original == reversed_num

def is_palindrome_v2(x: int) -> bool:
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    print("Enter an integer number:")
    x = int(input().strip())
    print(is_palindrome(x))