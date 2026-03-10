import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sectors = {
    "Technology": "XLK",
    "Financials": "XLF",
    "Healthcare": "XLV",
    "Energy": "XLE",
    "Industrials": "XLI",
    "Consumer Disc": "XLY",
    "Consumer Staples": "XLP",
    "Utilities": "XLU",
    "Materials": "XLB",
    "Real Estate": "XLRE",
    "Communication": "XLC"
}

tickers = list(sectors.values())

data = yf.download(
    tickers,
    period="1mo",
    group_by="ticker",
    progress=False
)

prices = pd.DataFrame()

for sector, ticker in sectors.items():

    try:
        prices[sector] = data[ticker]["Close"]
    except:
        pass

if prices.empty:
    print("Download failed — check internet or yfinance.")
    exit()

returns = prices.pct_change().dropna()

latest_returns = returns.iloc[-1]

heatmap_data = latest_returns.to_frame(name="Return").T

plt.figure(figsize=(12,3))

sns.heatmap(
    heatmap_data,
    cmap="RdYlGn",
    annot=True,
    fmt=".2%",
    linewidths=0.5
)

plt.title("S&P 500 Sector Rotation Heatmap (1-Day Return)")
plt.tight_layout()

plt.savefig("src/sector_rotation_heatmap.png")

plt.show()