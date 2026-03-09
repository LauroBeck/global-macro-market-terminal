![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# Global Macro Market Terminal

A Python terminal dashboard that displays live global market data including equities, commodities, volatility, and crypto.

## Features

- Live market dashboard in the terminal
- Automatic refresh every few seconds
- Color-coded price changes
- Tracks major global assets

Markets included:

- S&P 500
- NASDAQ
- Dow Jones
- Russell 2000
- Oil
- Gold
- USD Dollar Index
- VIX Volatility Index
- Bitcoin

## Example Output

GLOBAL MACRO MARKET TERMINAL

Asset        Price    Change %
SP500        6710     -0.44%
NASDAQ      22361     -0.12%
DOW         47114     -0.82%
RUSSELL2000  2509     -0.64%
OIL           94.69    4.17%
GOLD        5111.80   -0.67%
USD_INDEX     99.09    0.10%
VIX           17.90    2.10%
BITCOIN    118420      1.75%

## Technologies Used

- Python
- yfinance
- rich

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/global-macro-market-terminal.git

Navigate to the project:

cd global-macro-market-terminal

Install dependencies:

pip install -r requirements.txt

## Run the Terminal

python src/global_index_tracker.py

## Project Structure

global-macro-market-terminal
¦
+-- src
¦   +-- global_index_tracker.py
¦
+-- requirements.txt
+-- README.md
+-- .gitignore

## Future Improvements

- Add live charts
- Add more global indices
- Add bond market tracking
- Add crypto market panel

## License

MIT License

