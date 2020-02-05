import pandas as pd

df = pd.read_csv("SampleData1.csv", nrows=3)
# print(df)
# df=pd.read_csv("SampleData1.csv",header=None,names=["punu","sunu","kd"])
# print(df)
df = pd.read_csv("SampleData1.csv", na_values={
    "Region": ["East"]

})
print(df)
