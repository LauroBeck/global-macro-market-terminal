import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Config
tickers = {
    "^IXIC": "Nasdaq", "MSFT": "Microsoft", 
    "XOM": "Exxon", "CVX": "Chevron", 
    "SHEL": "Shell", "BP": "BP"
}

# 2026 Consensus Yields
yields = {
    "MSFT": 0.89, "XOM": 2.72, "CVX": 3.75, 
    "COP": 3.40, "BP": 5.70, "SHEL": 3.90
}

print("Starting graphical engine...")

# 1. Fetching Data for Momentum Plot
data = yf.download(list(tickers.keys()), period="6mo", progress=False)['Close']
# Normalize to 100
norm = (data / data.iloc[0]) * 100

plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Performance Line Chart
for t in norm.columns:
    label = tickers.get(t, t)
    linewidth = 2.5 if t in ["MSFT", "XOM"] else 1.5
    ax1.plot(norm.index, norm[t], label=label, linewidth=linewidth)

ax1.set_title("Market Stability Fund: Asset Momentum (6-Month)", color='lawngreen', fontsize=14)
ax1.set_ylabel("Normalized Value (Base 100)")
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax1.grid(True, alpha=0.1)

# Plot 2: Dividend Bar Chart
colors = ['#00a4ef' if n == 'MSFT' else '#ff9900' for n in yields.keys()]
ax2.bar(yields.keys(), yields.values(), color=colors, alpha=0.8)
ax2.set_title("Projected Dividend Yields - March 2026", color='lawngreen', fontsize=14)
ax2.set_ylabel("Yield (%)")

# Add value labels
for i, v in enumerate(yields.values()):
    ax2.text(i, v + 0.1, f"{v}%", color='white', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('src/market_analysis_report.png')
print("Report generated: src/market_analysis_report.png")
