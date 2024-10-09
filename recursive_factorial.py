def recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive(n - 1)

print(recursive(2))

print(recursive(5))

print(recursive(10))

# Time Complexity: O(n)
# Space Complexity: O(1)