def sum_array(n):
    suma = 0
    for i in n:
        suma += i
    return suma

print(sum_array([1, 2, 3, 4, 5, 6]))

print(sum_array([3, 56, 785, 353, 23]))

print(sum_array([10, 10, 10, 10, 10]))

# Time Complexity: O(n)
# Space Complexity: O(1)