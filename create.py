import pandas as pd

df_stocks = pd.DataFrame({
    "tickers": ["google", "wmt", "msft"],
    "price": [845, 65, 64],
    "pe": [10, 20, 30],

})
df_weather = pd.DataFrame({
    "day": ["1/1/2017", "2/2/17", "3/1/18"],
    "tempreture": [32, 35, 28],
    "event": ["rain", "sunny", "snow"]
})
with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
