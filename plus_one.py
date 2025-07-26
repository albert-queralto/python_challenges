def plus_one(digits: list[int]) -> list[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
    print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(plus_one([0]))  # Output: [1]
    print(plus_one([9]))  # Output: [1, 0]
    print(plus_one([9, 9]))  # Output: [1, 0, 0]
    print(plus_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
    print(plus_one([1, 0, 9]))  # Output: [1, 1, 0]
    print(plus_one([1, 9, 9]))  # Output: [2, 0, 0]
    print(plus_one([9, 9, 9, 9]))  # Output: [1, 0, 0, 0, 0]
    print(plus_one([1, 0, 0, 0, 0]))  # Output: [1, 0, 0, 0, 1]
    print(plus_one([1, 0, 0, 0, 9]))  # Output: [1, 0, 0, 1, 0]
    print(plus_one([1, 0, 0, 9, 9]))  # Output: [1, 0, 1, 0, 0]
    print(plus_one([1, 0, 9, 9, 9]))  # Output: [1, 1, 0, 0, 0]
    print(plus_one([1, 9, 9, 9, 9]))  # Output: [2, 0, 0, 0, 0]
    print(plus_one([9, 9, 9, 9, 9]))  # Output: [1, 0, 0, 0, 0, 0]
    print(plus_one([1, 0, 0, 0, 0, 0]))  # Output [1, 0, 0, 0, 0, 1]