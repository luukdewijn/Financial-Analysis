import yfinance as yf

# Get the data for the stock

stock = 'AAPL'
start_time = '2018-01-01'
end_time = '2024-01-01'
data = yf.download(stock, start=start_time, end=end_time)


# Plot the close prices
import matplotlib.pyplot as plt
data.Close.plot()
plt.show()