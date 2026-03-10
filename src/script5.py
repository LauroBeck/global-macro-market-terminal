import yfinance as yf
print("--- SCRIPT 5: MIDDLE EAST PIVOT ---")
data = yf.download("2222.SR", period="1d", progress=False)
print(f"ARAMCO (2222.SR): {data['Close'].iloc[-1]:.2f} SAR")
