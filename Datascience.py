import pandas as pd
#Load and inspect the data
Df=pd.read_csv(r"C:\Users\Sachin m\Downloads\sales - pandas 1.csv")
Df["Total"] = Df["Quantity"] * Df["Price"]
print(Df.to_string())
print(Df.info())
#Data Cleaning and Transformation
print(Df== Df.fillna(method='ffill'))

print(Df==Df.drop_duplicates)
#Calculate total price
print(Df.groupby("Price")["Total"].sum())
#Find top customers & products
print(Df.groupby("Customer Name")["Total"].sum().nlargest())
#top Product
print(Df.groupby("Product")["Total"].sum().nlargest())
#Group data for insights
print(Df.sort_values("Total",ascending = False))
#Filter with query()
print(Df.query("Total > 500"))
#Apply custom functions
print((Df.assign(Discount = Df["Total"] * 0.90))["Discount"])
