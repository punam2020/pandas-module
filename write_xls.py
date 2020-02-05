import pandas as pd

df = pd.read_excel("sampledataa.xlsx")
print(df.to_excel("new.xlsx"))

# print(df)
