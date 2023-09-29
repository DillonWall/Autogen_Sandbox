# filename: stock_price_plot.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Downloading the stock data
nvda_data = yf.download('NVDA', start='2022-01-01')
tesla_data = yf.download('TESLA', start='2022-01-01')

# Calculating the daily percentage change
nvda_data['Pct Change'] = nvda_data['Adj Close'].pct_change()
tesla_data['Pct Change'] = tesla_data['Adj Close'].pct_change()

plt.figure(figsize=(14,7))

# Plotting NVDA data
plt.plot(nvda_data.index, nvda_data['Pct Change'], label='NVDA')

# Plotting TESLA data
plt.plot(tesla_data.index, tesla_data['Pct Change'], label='TESLA')

plt.title('NVDA vs TESLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.legend()

plt.show()