import yfinance as yf
import time
from datetime import datetime

from rich.live import Live
from rich.table import Table
from rich.console import Console

console = Console()

tickers = {
    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",
    "DOW": "^DJI",
    "RUSSELL2000": "^RUT",
    "OIL": "CL=F",
    "GOLD": "GC=F",
    "USD_INDEX": "DX=F",
    "VIX": "^VIX",
    "BITCOIN": "BTC-USD",
}

def fetch_data():

    rows = []

    for name, symbol in tickers.items():

        try:

            ticker = yf.Ticker(symbol)

            hist = ticker.history(period="5d")

            closes = hist["Close"].dropna()

            last = float(closes.iloc[-1])
            prev = float(closes.iloc[-2]) if len(closes) > 1 else last

            change = ((last - prev) / prev) * 100

            rows.append((name, round(last,2), round(change,2)))

        except Exception:

            rows.append((name, None, None))

    return rows


def build_table():

    table = Table(title="GLOBAL MACRO MARKET TERMINAL")

    table.add_column("Asset")
    table.add_column("Price")
    table.add_column("Change %")

    rows = fetch_data()

    for asset, price, change in rows:

        if price is None:

            table.add_row(asset, "N/A", "N/A")

        else:

            color = "green" if change > 0 else "red"

            table.add_row(asset, str(price), f"[{color}]{change}%[/{color}]")

    table.caption = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return table


with Live(build_table(), refresh_per_second=1, console=console) as live:

    while True:

        time.sleep(15)

        live.update(build_table())
