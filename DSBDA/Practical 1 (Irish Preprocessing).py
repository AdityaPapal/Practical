import pandas as pd

df = pd.read_csv("Practical 1/Iris.csv")

print(df.head())
print()

print("Missing values : ")
print(df.isnull().sum())
print()

# Statstics 
print(df.describe())
print()

# check datatypes 
print("Data Types of values in datasets")
print(df.dtypes)


# categorical data to numerical data
print(df['Species'].unique())
print()

df['Species'] = df['Species'].map({"Iris-setosa" : 0, "Iris-versicolor" : 1, "Iris-virginica" : 2})
print(df.head())

print(df['Species'].unique())
print()