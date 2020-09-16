# Linear time iterate over all items
arr = [12, 23, 56, 87, 14] # n = 5
for num in arr: # O(n * 1) ==> O(n)
    print(num) # O(1)
for num in arr: # O(n * 1) ==> O(n)
    print(num) # O(1)

# content times how many times it loops
# O(n * 1) ==> O(n)
# O(n * 1) + O(n * 1) + O(1)
# O(2n) + O(1) ==> O(n) + O(1) ==> O(n)
# still O(n) because these are separate and not nested loops

# constant time lookup
print(arr[3]) #O(1)

# quadratic time nested iteration
for x in arr: # O(n)
    for y in arr: # O(n) ==> O(n^2)
        for z in arr: # O(n) ==> O(n^3)
            print(x, y, z) #  O(1) ==> O(1 * n^2)
# O(n^2) + O(n) + O(1 * n^2)
# O(2n^2) + O(n) ==> O(n^2) + O(n^2) drop constant, coefficients, and smaller complexity
# O(n^2) ==> O(n^3) still represented as O(n^2)

# 10 * 10 = 100
# 100 * 100 = 1000

# can we do better?


