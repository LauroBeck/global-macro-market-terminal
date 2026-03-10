import yfinance as yf
print("--- SCRIPT 4: EU ENERGY ---")
for t in ["BP", "SHEL"]:
    data = yf.download(t, period="1d", progress=False)
    print(f"{t}: {data['Close'].iloc[-1]:.2f}")
