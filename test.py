import pandas as pd

df = pd.read_csv("SampleData1.csv")
# print(df)
# print(df["Units"].max())
# print(df[df.Units>=10])
# print(df["Total"][df["Region"]=="East"])
print(df[["Region", "Total"]][df.Region == "East"])
# print(df["Unit Cost"].mean())
