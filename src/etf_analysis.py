import yfinance as yf

ticker = yf.Ticker("SPY")

print("ETF Info:")
print(ticker.info["longName"])

data = ticker.history(period="1mo")

print("\nLast Prices:")
print(data.tail())

start = data["Close"].iloc[0]
end = data["Close"].iloc[-1]

return_pct = ((end - start) / start) * 100

print("\nMonthly Return:", round(return_pct,2), "%")
