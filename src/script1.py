import yfinance as yf
print("--- SCRIPT 1: MACRO INDICES ---")
for t in ["^IXIC", "^GSPC", "^FTSE"]:
    data = yf.download(t, period="1d", progress=False)
    if not data.empty:
        val = data['Close'].iloc[-1]
        if hasattr(val, 'iloc'): val = val.iloc[0] # Handle Series
        print(f"{t}: {float(val):.2f}")
