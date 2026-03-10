import yfinance as yf
print("--- SCRIPT 2: TECH CORE ---")
data = yf.download("MSFT", period="1d", progress=False)
print(f"MSFT: {data['Close'].iloc[-1]:.2f}")
