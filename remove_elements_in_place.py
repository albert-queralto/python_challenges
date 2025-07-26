def remove_element(nums: list[int], val: int) -> int:
    if not nums:
        return 0
    
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    return i

if __name__ == "__main__":
    print(remove_element([3, 2, 2, 3], 3))  # Output: 2
    print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Output: 5
    print(remove_element([], 0))  # Output: 0
    print(remove_element([1], 1))  # Output: 0
    print(remove_element([1, 1], 1))  # Output: 0
    print(remove_element([1, 1, 1], 1))  # Output: 0
    print(remove_element([1, 2, 3], 1))  # Output: 2
    print(remove_element([1, 2, 3], 2))  # Output: 2
    print(remove_element([1, 2, 3], 3))  # Output: 2
    print(remove_element([1, 2, 2, 3], 2))  # Output: 2
    print(remove_element([1, 1, 2, 2, 3], 2))  # Output: 3
    print(remove_element([1, 1, 1, 2, 2, 3], 2))  # Output: 4
    print(remove_element([1, 2, 2, 3, 3], 2))  # Output: 3
    print(remove_element([1, 1, 2, 2, 3, 3], 2))  # Output: 4
    print(remove_element([1, 1, 1, 2, 2, 3, 3], 2))  # Output: 5
    print(remove_element([1, 2, 2, 3, 3, 4], 2))  # Output: 4
    print(remove_element([1, 1, 2, 2, 3, 3, 4], 2))  # Output: 5
    print(remove_element([1, 1, 1, 2, 2, 3, 3, 4], 2))  # Output: 6