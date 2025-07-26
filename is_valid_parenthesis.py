def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            print(f"Top element: {top_element}")
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

print(is_valid("()"))      # Output: true
print(is_valid("()[]{}"))  # Output: true
print(is_valid("(]"))      # Output: false
print(is_valid("([])"))    # Output: true
print(is_valid("{{(})}}")) # Output: false