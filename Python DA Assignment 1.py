#Python DA Assignment 1: Data Analysis using NumPy and Pandas

import numpy as np
import pandas as pd
#Numpy Array Operations

# 1. Create a 1D NumPy Array for Week 1
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("===== WEEK 1 TEMPERATURE DATA =====")
print("Temperatures:", temperatures_w1)

# 2. Inspection and Properties
print("\n===== ARRAY PROPERTIES =====")
print("Shape:", temperatures_w1.shape)
print("Data Type:", temperatures_w1.dtype)
print("Number of Elements:", temperatures_w1.size)

# 3. Array Operations

print("\n===== TEMPERATURE OPERATIONS =====")
temperatures_fahrenheit = (temperatures_w1 * 9/5) + 32

print("Temperature in Fahrenheit:", temperatures_fahrenheit)
print("Maximum Temperature:", np.max(temperatures_w1))
print("Minimum Temperature:", np.min(temperatures_w1))
print("Mean Temperature:", np.mean(temperatures_w1))

# 4. Array Slicing and Indexing
print("\n===== ARRAY SLICING =====")

first_three_days = temperatures_w1[:3]
print("First Three Days:", first_three_days)
weekend = temperatures_w1[-2:]
print("Weekend (Last Two Days):", weekend)
middle_three_days = temperatures_w1[2:5]
print("Middle Three Days:", middle_three_days)

#5. Create a 2D Array
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   # Week 2
])
print("\n\n===== 2D TEMPERATURE ARRAY =====")
print(temperatures)

# 6. Inspect the 2D Array
print("\n===== 2D ARRAY PROPERTIES =====")

print("Shape:", temperatures.shape)
print("Data Type:", temperatures.dtype)
print("Total Number of Elements:", temperatures.size)

print("\n===== WEEK-WISE TEMPERATURES =====")
week1 = temperatures[0]
week2 = temperatures[1]
print("Week 1:", week1)
print("Week 2:", week2)

print("\n===== WEEKEND TEMPERATURES =====")
week1_weekend = temperatures[0, -2:]
week2_weekend = temperatures[1, -2:]
print("Week 1 Weekend:", week1_weekend)
print("Week 2 Weekend:", week2_weekend)


#Pandas Series

#1. Creating Pandas Series
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"]
)

print("\n\n===== PANDAS SERIES =====")
print(marks)

# 2. Indexing and Slicing
print("\n===== SERIES INDEXING =====")

print("Mark of 1st Rank Student:", marks.iloc[0])

print("\nTop 3 Rank Students:")
print(marks.loc[["Rank1", "Rank2", "Rank3"]])

print("\nMark of 3rd Rank Student:", marks.iloc[2])

print("\nStudents with Marks Greater Than 90:")
print(marks[marks > 90])

#3. Manipulating Series
print("\n===== SERIES MANIPULATION =====")

marks.loc["Rank1"] = 100
print("After modifying Rank1 mark:")
print(marks)

marks = marks.drop("Rank5")
print("\nAfter removing Rank5:")
print(marks)

cgpa = marks / 10
print("\nCGPA:")
print(cgpa)


#Pandas DataFrame

#1. Creating Pandas DataFrame
transactions = pd.DataFrame({
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "ProductCategory": ["Electronics","Clothing","Electronics","Furniture","Clothing","Electronics","Furniture", "Clothing", "Furniture","Electronics"],

    "Region": ["North","South", "North","East","West","North","East","West","South","North"],

    "Amount": [200,150,300,450,200,250,300,180,350,400]
})
print("\n\n===== TRANSACTIONS DATAFRAME =====")
print(transactions)

#2. Data Exploration
print("\n===== HEAD =====")
print(transactions.head())

print("\n===== TAIL =====")
print(transactions.tail())

print("\n===== SHAPE =====")
print(transactions.shape)

print("\n===== COLUMN NAMES =====")
print(transactions.columns)

print("\n===== DATA TYPES =====")
print(transactions.dtypes)


print("\n===== PRODUCT CATEGORY AND AMOUNT =====")
print(transactions[["ProductCategory", "Amount"]])

print("\n===== LAST 3 COLUMNS =====")
print(transactions.iloc[:, -3:])


print("\n===== NORTH REGION WITH AMOUNT > 200 =====")
north_high_amount = transactions[(transactions["Region"] == "North") &(transactions["Amount"] > 200)]
print(north_high_amount)


print("\n===== PRODUCT CATEGORY VALUE COUNTS =====")
print(transactions["ProductCategory"].value_counts())

print("\n===== UNIQUE REGIONS =====")
print(transactions["Region"].unique())

print("\n===== MEAN AMOUNT BY REGION =====")
region_mean = transactions.groupby("Region")["Amount"].mean()
print(region_mean)

#3. Manipulating the DataFrame
transactions.loc[transactions["TransactionID"] == 102,"Amount"] = 165
print("\n===== AFTER MODIFYING TRANSACTION 102 =====")
print(transactions)

transactions["Discount"] = transactions["Amount"] * 0.10
print("\n===== AFTER ADDING DISCOUNT COLUMN =====")
print(transactions)

transactions = transactions[transactions["TransactionID"] != 109]
print("\n===== AFTER REMOVING TRANSACTION 109 =====")
print(transactions)

transactions = transactions.drop(columns=["Discount"])
print("\n===== FINAL DATAFRAME =====")
print(transactions)

