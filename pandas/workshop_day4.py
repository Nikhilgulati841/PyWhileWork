import pandas as pd

df=pd.read_csv("pandas/AmazonSalesData.csv")
# print(df.head())
# print(df.tail())

# print(df.columns)
# print(df.dtypes)
print(len(df))
print(df["Total Revenue"].sum())
print(df["Unit Price"].mean())
print(df["Total Revenue"].max())
print(df["Region"].value_counts())

print(df[df["Unit Price"]==df["Unit Price"].min()])
print(df["Unit Price"].min())
print(df.loc[df["Unit Price"].idxmin()],"Region")
