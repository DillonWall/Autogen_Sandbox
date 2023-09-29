# filename: stock_price_plot.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Downloading the stock data
nvda_data = yf.download('NVDA', start='2022-01-01')
tesla_data = yf.download('TSLA', start='2022-01-01')  # Corrected the ticker symbol here

# Calculating the daily percentage change
nvda_data['Pct Change'] = nvda_data['Adj Close'].pct_change()
tesla_data['Pct Change'] = tesla_data['Adj Close'].pct_change()

plt.figure(figsize=(14,7))

# Plotting NVDA data
plt.plot(nvda_data.index, nvda_data['Pct Change'], label='NVDA')

# Plotting TSLA data
plt.plot(tesla_data.index, tesla_data['Pct Change'], label='TSLA')  # Corrected the label here

plt.title('NVDA vs TSLA Stock Price Change YTD')  # Corrected the title here
plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.legend()

plt.show()
