def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

if __name__ == "__main__":
    print(strStr("hello", "ll"))  # Output: 2
    print(strStr("aaaaa", "bba"))  # Output: -1
    print(strStr("", ""))  # Output: 0
    print(strStr("a", ""))  # Output: 0
    print(strStr("", "a"))  # Output: -1
    print(strStr("mississippi", "issip"))  # Output: 4
    print(strStr("mississippi", "pi"))  # Output: 9
    print(strStr("mississippi", "issipi"))  # Output: -1