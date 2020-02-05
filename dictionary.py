import pandas as pd

# df=pd.read_csv("SampleData1.csv")
SampleData = {
    "OrderDate": ["1/6/18 ", "1/23/18", "2/9/18  ", "2/26/18"],
    "Region": [" East", "Central", "Central", "Central"],
    "Rep": ["Jones", "kivell", "Jardine", "Gill"]
}
df = pd.DataFrame(SampleData)
# rows,columns=df.shape
# print(rows)
# print(columns)
# print(df.head(2))
# print(df.tail(1))
# print(df[1:3])
# print(df.columns)
print(df['Region'])
# print(df.Region)
print(df[["Region", "Rep"]])
