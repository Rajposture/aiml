
import numpy as np

# 1. Create an array
a = np.array([10, 20, 30, 40, 50])
print("Array:", a)

# 2. Find the sum
print("Sum:", np.sum(a))

# 3. Find the mean
print("Mean:", np.mean(a))

# 4. Find the maximum value
print("Maximum:", np.max(a))

# 5. Find the minimum value
print("Minimum:", np.min(a))

# 6. Sort the array
b = np.array([40, 10, 30, 20, 50])
print("Sorted Array:", np.sort(b))

# 7. Reshape an array
c = np.array([1, 2, 3, 4, 5, 6])
print("Reshaped Array:\n", c.reshape(2, 3))

# 8. Find the square root
print("Square Root:", np.sqrt(a))
