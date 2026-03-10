import yfinance as yf
print("--- SCRIPT 3: US ENERGY ---")
for t in ["XOM", "CVX", "COP"]:
    data = yf.download(t, period="1d", progress=False)
    print(f"{t}: {data['Close'].iloc[-1]:.2f}")
