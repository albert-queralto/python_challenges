def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    first = 1
    second = 2
    for _ in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second

def climb_stairs_recursive(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

def climb_stairs_array(n: int) -> int:
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    print(climb_stairs(2))  # Output: 2
    print(climb_stairs(3))  # Output: 3
    print(climb_stairs(4))  # Output: 5
    print(climb_stairs(5))  # Output: 8
    print(climb_stairs(6))  # Output: 13
    print(climb_stairs(7))  # Output: 21
    print(climb_stairs(8))  # Output: 34
    print(climb_stairs(9))  # Output: 55
    print(climb_stairs(10))  # Output: 89
    print(climb_stairs(11))  # Output: 144
    print(climb_stairs(12))  # Output: 233
    print(climb_stairs(13))  # Output: 377
    print(climb_stairs(14))  # Output: 610
    print(climb_stairs(15))  # Output: 987
    print(climb_stairs(16))  # Output: 1597
    print(climb_stairs(17))  # Output: 2584
    print(climb_stairs(18))  # Output: 4181
    print(climb_stairs(19))  # Output: 6765
    print(climb_stairs(20))  # Output: 10946
    print(climb_stairs(21))  # Output: 17711
    print(climb_stairs(22))  # Output: 28657
    print(climb_stairs(23))  # Output: 46368
    print(climb_stairs(24))  # Output: 75025
    print(climb_stairs(25))  # Output: 121393
    print(climb_stairs(26))  # Output: 196418
    print(climb_stairs(27))  # Output: 317811
    print(climb_stairs(28))  # Output: 514229
    print(climb_stairs(29))  # Output: 832040
    print(climb_stairs(30))  # Output: 1346269
    print(climb_stairs(31))  # Output: 2178309