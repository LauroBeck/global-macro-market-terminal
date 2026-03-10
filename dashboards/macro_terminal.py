import time
import yfinance as yf

ticker = "^GSPC"

while True:

    data = yf.download(ticker, period="1d", interval="1m")

    last = data["Close"].iloc[-1]

    print("SP500 LIVE:", last)

    time.sleep(10)
