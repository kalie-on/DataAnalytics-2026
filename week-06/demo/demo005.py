matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[1][2])

cube = [
    [
        [1, 2],
        [3, 4]
    ],

    [
        [5, 6],
        [7, 8]
    ]
]



import numpy as np

# =====================================================
# 1D ARRAY (One-Dimensional Array)
# =====================================================
# A 1D array is like a simple list of elements.

arr_1d = np.array([10, 20, 30, 40, 50])

print("=== 1D Array ===")
print(arr_1d)

# Accessing elements in 1D array using index
print("First element:", arr_1d[0])   # index 0
print("Third element:", arr_1d[2])   # index 2
print("Last element:", arr_1d[-1])   # negative indexing (last item)

print("\n")