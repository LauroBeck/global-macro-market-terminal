import yfinance as yf
import pandas as pd

# Combined list for your Market Stability Fund (MSF) Dashboard
tickers = {
    "Indices": ["^IXIC", "^GSPC", "^FTSE"],
    "Tech": ["MSFT"],
    "Energy Supermajors": ["CVX", "XOM", "BP", "COP", "SHEL", "2222.SR"]
}

# Mapping names for clear reporting
ticker_names = {
    "^IXIC": "Nasdaq", "^GSPC": "S&P 500", "^FTSE": "FTSE 100",
    "MSFT": "Microsoft", "CVX": "Chevron", "XOM": "Exxon",
    "BP": "BP", "COP": "ConocoPhillips", "SHEL": "Shell", "2222.SR": "Aramco"
}

print(f"{'--- ENERGY & MACRO DIAGNOSTIC ---':^50}")
print(f"{'ASSET':<20} | {'PRICE':>10} | {'% CHANGE'}")
print("-" * 50)

for category, list_of_tickers in tickers.items():
    print(f"\n[{category}]")
    for ticker in list_of_tickers:
        try:
            # Using 2d period to calculate the daily delta accurately
            data = yf.download(ticker, period="2d", progress=False)
            if not data.empty and len(data) >= 2:
                close_today = data['Close'].iloc[-1]
                close_prev = data['Close'].iloc[-2]
                
                # Handling multi-index if returned
                p_today = close_today.values[0] if hasattr(close_today, 'values') else close_today
                p_prev = close_prev.values[0] if hasattr(close_prev, 'values') else close_prev
                
                change = ((p_today - p_prev) / p_prev) * 100
                name = ticker_names.get(ticker, ticker)
                
                print(f"{name:<20} | {p_today:>10.2f} | {change:>+7.2f}%")
            else:
                print(f"{ticker:<20} | {'NO DATA':>10} | {'---'}")
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")

print("-" * 50)
