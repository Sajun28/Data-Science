import pandas as pd
Df=pd.read_csv(r"C:\Users\Sachin m\Downloads\sales - pandas 1.csv")
Df["Total"] = Df["Quantity"] * Df["Price"]
print(Df.to_string())
print(Df.info())
print(Df== Df.fillna(method='ffill'))
print(Df==Df.drop_duplicates)
print(Df.groupby("Price")["Total"].sum())
#Top name 
print(Df.groupby("Customer Name")["Total"].sum().nlargest())
#top Product
print(Df.groupby("Product")["Total"].sum().nlargest())
print(Df.sort_values("Total",ascending = False))
print(Df.query("Total > 500"))
print((Df.assign(Discount = Df["Total"] * 0.90))["Discount"])
