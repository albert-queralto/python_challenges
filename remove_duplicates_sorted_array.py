def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2]))  # Output: 2
    print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: 5
    print(remove_duplicates([]))  # Output: 0
    print(remove_duplicates([1]))  # Output: 1
    print(remove_duplicates([1, 1]))  # Output: 1
    print(remove_duplicates([1, 1, 1]))  # Output: 1
    print(remove_duplicates([1, 2, 3]))  # Output: 3
    print(remove_duplicates([1, 2, 2, 3]))  # Output: 3
    print(remove_duplicates([1, 1, 2, 2, 3]))  # Output: 3
    print(remove_duplicates([1, 1, 1, 2, 2, 3]))  # Output: 3
    print(remove_duplicates([1, 2, 2, 3, 3]))  # Output: 3
    print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: 3
    print(remove_duplicates([1, 1, 1, 2, 2, 3, 3]))  # Output: 3
    print(remove_duplicates([1, 2, 2, 3, 3, 4]))  # Output: 4
    print(remove_duplicates([1, 1, 2, 2, 3, 3, 4]))  # Output: 4
    print(remove_duplicates([1, 1, 1, 2, 2, 3, 3, 4]))  # Output: 4
    print(remove_duplicates([1, 2, 2, 3, 3, 4, 4]))  # Output: 4
    print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]))  # Output: 4
    print(remove_duplicates([1, 1, 1, 2, 2, 3, 3, 4, 4]))  # Output: 4