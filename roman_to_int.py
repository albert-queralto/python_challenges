def roman_to_int(s: str) -> int:
    s = s.upper()
    
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
            total -= roman_to_int_map[s[i]]
        else:
            total += roman_to_int_map[s[i]]
    
    return total

if __name__ == "__main__":
    print(roman_to_int("III")) # 3
    print(roman_to_int("IV")) # 4
    print(roman_to_int("IX")) # 9
    print(roman_to_int("LVIII")) # 58
    print(roman_to_int("MCMXCIV")) # 1994