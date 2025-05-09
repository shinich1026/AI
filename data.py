import yfinance as yf

data = yf.download("AAPL", start="2023-12-31", end="2024-12-31")
print(data.head())