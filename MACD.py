# Import yfinance
import yfinance as yf

#Download the data for the Apple stock from 2017-04-01 to 2019-04-30 using yfinance
data = yf.download('AAPL', start="2017-04-01", end="2019-04-30")

# Print the first five rows of the data
data.head()


# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

data.index = pd.to_datetime(data.index, dayfirst=True)

# Visualise the data
plt.figure(figsize=(10,5))
data['Close'].plot(figsize=(10,5))
plt.legend()
plt.show()

# Calculate exponential moving average using exponential weighted function in pandas. Since we are taking exponential moving average, 
#we can take exponential weighted mean using ewm(span=x).mean() where span is the time period of moving average. 
data['12d_EMA'] = data.Close.ewm(span=12, adjust=False).mean()
data['26d_EMA'] = data.Close.ewm(span=26, adjust=False).mean()

#Plotting the closing value of stock price along with the 12 day and 26day moving average
data[['Close','12d_EMA','26d_EMA']].plot(figsize=(10,5))
plt.show()

# Calculating MACD 
data['macd'] = data['12d_EMA']- data['26d_EMA'] 

# Calculate Signal
data['macdsignal'] = data.macd.ewm(span=9, adjust=False).mean()

data[['macd','macdsignal']].plot(figsize=(10,5))
plt.show()

# Import numpy
import numpy as np

# Define Signal
data['trading_signal'] = np.where(data['macd'] > data['macdsignal'], 1, -1)

# Calculate Returns
data['returns'] = data.Close.pct_change()

# Calculate Strategy Returns
data['strategy_returns'] = data.returns * data.trading_signal.shift(1)

# Calculate Cumulative Returns
cumulative_strategy_returns = (data.strategy_returns + 1).cumprod()

# Plot Strategy Returns
cumulative_strategy_returns.plot(figsize=(10,5))
plt.legend()
plt.show()

#Performance Measures 
#CAGR = [(Final value of investment /Initial value of investment)^(1/number of years)] - 1

# Total number of trading days
days = len(cumulative_strategy_returns)

# Calculate compounded annual growth rate
annual_returns = (cumulative_strategy_returns.iloc[-1]**(252/days) - 1)*100

print('The CAGR is %.2f%%' % annual_returns)

# Calculate the annualised volatility
annual_volatility = data.strategy_returns.std() * np.sqrt(252) * 100

'The annualised volatility is %.2f%%' % annual_volatility


# Assume the annual risk-free rate is 6%
risk_free_rate = 0.06
daily_risk_free_return = risk_free_rate/252

# Calculate the excess returns by subtracting the daily returns by daily risk-free return
excess_daily_returns = data.strategy_returns - daily_risk_free_return

# Calculate the sharpe ratio using the given formula
sharpe_ratio = (excess_daily_returns.mean() /
                excess_daily_returns.std()) * np.sqrt(252)

'The Sharpe ratio is %.2f' % sharpe_ratio


