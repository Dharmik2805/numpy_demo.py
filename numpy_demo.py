# Import NumPy
import numpy as np
import time

# Step 1: Create arrays of different dimensions
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

print("\n--- 1D Array ---")
print(arr1)

print("\n--- 2D Array ---")
print(arr2)

# Step 2: Mathematical operations
print("\n--- Mathematical Operations ---")
print("Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)

# Step 3: Broadcasting
arr3 = np.array([10, 20, 30])
result = arr2 + arr3

print("\n--- Broadcasting Result ---")
print(result)

# Step 4: Statistical functions
print("\n--- Statistical Functions ---")
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))

# Step 5: Compare NumPy vs Python list
python_list = [1, 2, 3, 4, 5]

start = time.time()
for i in range(1000000):
    [x * 2 for x in python_list]
end = time.time()
print("\nPython list time:", end - start)

start = time.time()
for i in range(1000000):
    arr1 * 2
end = time.time()
print("NumPy array time:", end - start)

# Step 6: Generate random data
random_array = np.random.rand(3, 3)

print("\n--- Random Array ---")
print(random_array)

# Step 7: Optimize calculations (vectorization)
large_array = np.arange(1000000)

start = time.time()
result = large_array * 2
end = time.time()

print("\nOptimized calculation time:", end - start)

# Step 8: Array structure
print("\n--- Array Structure ---")
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)