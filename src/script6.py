import yfinance as yf
tickers = ["^IXIC", "^GSPC", "MSFT", "XOM", "CVX", "COP", "BP", "SHEL", "2222.SR"]
print(f"{'--- SCRIPT 6: INTEGRATED MSF DASHBOARD ---':^40}")
print(f"{'TICKER':<10} | {'PRICE':>10}")
print("-" * 25)
for t in tickers:
    try:
        d = yf.download(t, period="1d", progress=False)
        if not d.empty:
            val = d['Close'].iloc[-1]
            # Strip potential multi-index or series formatting
            price = float(val.iloc[0]) if hasattr(val, 'iloc') else float(val)
            print(f"{t:<10} | {price:>10.2f}")
    except Exception as e:
        print(f"{t:<10} | Error")
