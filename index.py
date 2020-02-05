import pandas as pd

df = pd.read_csv("SampleData1.csv")
print(df.index)
# print(df.set_index("Region"))
df.reset_index(inplace=True)
print(df)
