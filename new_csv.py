import pandas as pd

df = pd.read_csv("SampleData1.csv")
# df.to_csv("new.csv",index=False)

df.to_csv("new.csv", columns=["OrderDate", "Region"])
print(df)
