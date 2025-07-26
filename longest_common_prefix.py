def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    print(f"Initial prefix: {prefix}")
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
            print(f"New prefix: {prefix}")
        if not prefix:
            break
    
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))  # Output: "fl"
    print(longest_common_prefix(["dog","racecar","car"]))     # Output: ""