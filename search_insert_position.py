def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 5))  # Output: 2
    print(search_insert([1, 3, 5, 6], 2))  # Output: 1
    print(search_insert([1, 3, 5, 6], 7))  # Output: 4