import yfinance as yf

print("Macro Market Test")

data = yf.download("^IXIC", period="5d")
print(data.tail())
