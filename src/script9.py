import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# March 2026 Strategy Data
data = {
    "Ticker": ["MSFT", "XOM", "CVX", "COP", "BP", "SHEL", "2222.SR"],
    "Yield": [0.89, 2.72, 3.75, 3.40, 5.70, 3.90, 5.10],
    "Proj_Gains": [15.0, 8.5, 9.2, 10.5, 4.0, 11.0, 6.5]
}
df = pd.DataFrame(data)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 7))

# Clustered Bar Chart
x = np.arange(len(df['Ticker']))
width = 0.4

ax.bar(x - width/2, df['Yield'], width, label='Div. Yield (%)', color='#00d4ff')
ax.bar(x + width/2, df['Proj_Gains'], width, label='Proj. Capital Gains (%)', color='#39ff14')

ax.set_title("MSF Strategy: Yield vs. Appreciation (2026 Baseline)", fontsize=16, color='lawngreen')
ax.set_xticks(x)
ax.set_xticklabels(df['Ticker'])
ax.set_ylabel("Percentage (%)")
ax.legend()

# Annotate Total Return
for i in range(len(df)):
    total = df['Yield'][i] + df['Proj_Gains'][i]
    ax.text(i, max(df['Yield'][i], df['Proj_Gains'][i]) + 0.5, f"TSR: {total}%", 
            ha='center', color='white', weight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('src/total_return_matrix.png')
print("Strategic Matrix saved to src/total_return_matrix.png")
