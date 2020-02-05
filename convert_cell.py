import pandas as pd


def convert_Region_cell(cell):
    if cell == "East":
        return "west"
    return cell


df = pd.read_excel("sampledataa.xlsx", converters={"Region": convert_Region_cell})
print(df)
