import yfinance as yf
import pandas as pd

tickers = {
    "Oil": "CL=F",
    "Nasdaq": "^IXIC",
    "SP500": "^GSPC",
    "Gold": "GC=F",
    "USD": "DX-Y.NYB"
}

def fetch_market():
    data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, period="5d")
        data[name] = df["Close"].iloc[-1]
    return data

if __name__ == "__main__":
    market = fetch_market()
    print("GLOBAL MACRO MARKET")
    for k,v in market.items():
        print(k, v)
