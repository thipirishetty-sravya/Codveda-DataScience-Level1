import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, None, 30, 22, 200],
    "Salary": [50000, 60000, None, 45000, 700000],
    "City": ["Hyderabad", "Chennai", "Hyderabad", None, "Delhi"]

}
df = pd.DataFrame(data)
print(df)
print("\nMissing Values:\n")
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")
print("\nAfter Filling Missing Values:\n")
print(df)
df = df[df["Age"] < 100]
print("\nAfter Removing Outlier:\n")
print(df)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df["City"] = encoder.fit_transform(df["City"])
print("\nAfter Encoding City:\n")
print(df)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df["Salary"] = scaler.fit_transform(df[["Salary"]])
print("\nAfter Normalization:\n")
print(df)
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved as cleaned_data.csv")