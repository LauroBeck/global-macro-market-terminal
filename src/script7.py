import yfinance as yf
import pandas as pd

# March 2026 Consensus Projections (Yields & 5Y Growth)
projections = {
    "MSFT": {"yield": 0.0089, "growth": "10.2%", "outlook": "AI Neutral/Azure Growth"},
    "XOM":  {"yield": 0.0272, "growth": "3.1%",  "outlook": "43yr Dividend Aristocrat"},
    "CVX":  {"yield": 0.0375, "growth": "5.2%",  "outlook": "High FCF/Strategic Resilience"},
    "COP":  {"yield": 0.0340, "growth": "8.0%",  "outlook": "Lower 48 Efficiency Focus"},
    "BP":   {"yield": 0.0570, "growth": "N/A",   "outlook": "Buybacks Suspended/Debt Cut"},
    "SHEL": {"yield": 0.0390, "growth": "10.0%", "outlook": "LNG Volume Expansion"},
    "2222.SR": {"yield": 0.0510, "growth": "N/A", "outlook": "Hormuz Regime Surge"}
}

print(f"{'--- DIVIDEND & GROWTH PROJECTIONS (MAR 2026) ---':^65}")
print(f"{'TICKER':<10} | {'PRICE':>9} | {'YIELD':>7} | {'GROWTH':>7} | {'EST. ANUAL'}")
print("-" * 65)

for t, proj in projections.items():
    try:
        d = yf.download(t, period="1d", progress=False)
        if not d.empty:
            val = d['Close'].iloc[-1]
            price = float(val.iloc[0]) if hasattr(val, 'iloc') else float(val)
            annual_div = price * proj['yield']
            
            print(f"{t:<10} | {price:>9.2f} | {proj['yield']*100:>6.2f}% | {proj['growth']:>7} | ")
    except:
        print(f"{t:<10} | Data Fetch Error")

print("\n[STRATEGIC NOTES]")
print("* MSFT: Targeting  by year-end (15% growth expectation).")
print("* XOM/CVX: Providing the primary yield hedge against supply-chain shocks.")
print("* SHEL: 17 consecutive quarters of buybacks supporting a 10.5% total return.")
