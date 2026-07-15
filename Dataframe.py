
import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7,8,9]])

print(df.head())
#print(df)


# 3x3 data matrix with custom row (index) and column names
df = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
    index=['row1', 'row2', 'row3'], 
    columns=['col1', 'col2', 'col3']
)

print(df)

print(df.head(2))
print(df.tail(2))

print("\n")
print("\n")

print("Describe:")
print(df.describe())
print("\n")
print("\n")

print("Info:")
print(df.info())

print("\n")
print("\n")

print("Shape:")
print(df.shape)

print("\n")
print("\n")
print("Columns:")
print(df.columns)