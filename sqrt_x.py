def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

if __name__ == "__main__":
    print(my_sqrt(4))  # Output: 2
    print(my_sqrt(8))  # Output: 2
    print(my_sqrt(9))  # Output: 3
    print(my_sqrt(16))  # Output: 4
    print(my_sqrt(25))  # Output: 5
    print(my_sqrt(36))  # Output: 6
    print(my_sqrt(49))  # Output: 7
    print(my_sqrt(64))  # Output: 8
    print(my_sqrt(81))  # Output: 9
    print(my_sqrt(100))  # Output: 10
    print(my_sqrt(121))  # Output: 11
    print(my_sqrt(144))  # Output: 12
    print(my_sqrt(169))  # Output: 13
    print(my_sqrt(196))  # Output: 14
    print(my_sqrt(225))  # Output: 15
    print(my_sqrt(256))  # Output: 16
    print(my_sqrt(289))  # Output: 17
    print(my_sqrt(324))  # Output: 18
    print(my_sqrt(361))  # Output: 19
    print(my_sqrt(400))  # Output: 20
    print(my_sqrt(441))  # Output: 21
    print(my_sqrt(484))  # Output: 22
    print(my_sqrt(529))  # Output: 23
    print(my_sqrt(576))  # Output: 24
    print(my_sqrt(625))  # Output: 25
    print(my_sqrt(676))  # Output: 26
    print(my_sqrt(729))  # Output: 27
    print(my_sqrt(784))  # Output: 28
    print(my_sqrt(841))  # Output: 29
    print(my_sqrt(900))  # Output: 30
    print(my_sqrt(961))  # Output: 31
    print(my_sqrt(1024))  # Output: 32
    print(my_sqrt(1089))  # Output: 33
    print(my_sqrt(1156))  # Output: 34
    print(my_sqrt(1225))  # Output: 35