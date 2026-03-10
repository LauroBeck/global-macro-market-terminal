import yfinance as yf
import pandas as pd

ticker = yf.Ticker("SPY")

print("ETF Info:")
print(ticker.info["longName"])

data = ticker.history(period="1mo")

# Remove columns that contain only zeros or NaN
clean_data = data.loc[:, (data != 0).any(axis=0)]
clean_data = clean_data.dropna(axis=1, how="all")

print("\nClean Market Data:")
print(clean_data.tail())

start = clean_data["Close"].iloc[0]
end = clean_data["Close"].iloc[-1]

return_pct = ((end - start) / start) * 100

print("\nMonthly Return:", round(return_pct,2), "%")
