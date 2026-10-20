
import pandas as pd

# 1. Create a DataFrame
data = {
    "Name": ["Raj", "Amit", "Neha", "Riya"],
    "Marks": [85, 90, 78, 95],
    "Age": [19, 20, 18, 19]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# 2. Display first two rows
print("\nFirst Two Rows:\n", df.head(2))

# 3. Display column names
print("\nColumns:", df.columns.tolist())

# 4. Find average marks
print("\nAverage Marks:", df["Marks"].mean())

# 5. Find highest marks
print("\nHighest Marks:", df["Marks"].max())

# 6. Filter students scoring above 85
print("\nStudents scoring above 85:\n",
      df[df["Marks"] > 85])

# 7. Sort by marks
print("\nSorted Data:\n",
      df.sort_values(by="Marks"))

# 8. Display information
print("\nData Information:")
df.info()
