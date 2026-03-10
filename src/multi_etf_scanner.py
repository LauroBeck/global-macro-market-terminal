import yfinance as yf
import pandas as pd

# ETFs to analyze
tickers = ["SPY","QQQ","IWM","GLD"]

results = []

for ticker in tickers:

    etf = yf.Ticker(ticker)

    data = etf.history(period="1mo")

    start = data["Close"].iloc[0]
    end = data["Close"].iloc[-1]

    return_pct = ((end - start) / start) * 100

    results.append({
        "ETF": ticker,
        "Start Price": round(start,2),
        "End Price": round(end,2),
        "Monthly Return %": round(return_pct,2)
    })

df = pd.DataFrame(results)

# Rank by performance
df = df.sort_values(by="Monthly Return %", ascending=False)

print("\nETF PERFORMANCE RANKING\n")
print(df.to_string(index=False))
