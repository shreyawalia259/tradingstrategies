# Import libraries and dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
import yfinance as yf
import holoviews as hv

hv.extension('bokeh')
from bokeh.plotting import show


## CHIPOTLE DATA - (3 year data)
cmg = yf.Ticker("CMG")
cmg_historical = cmg.history(start="2018-1-5", end="2021-1-5", interval="1d")
cmg_df = cmg_historical.drop(columns=['Open', 'High', 'Low', 'Dividends', 'Stock Splits', 'Volume'])
## Rename the 'Close' column to the ticker for that company.
cmg_df.rename(columns= {'Close':'CMG'}, inplace=True)
## SHOPIFY DATA
shop = yf.Ticker("shop")
shop_historical = shop.history(start="2018-1-5", end="2021-1-5", interval="1d")
shop_df = shop_historical.drop(columns=['Open', 'High', 'Low', 'Dividends', 'Stock Splits', 'Volume'])
## Rename the 'Close' column to mirror ticker symbol
shop_df.rename(columns= {'Close':'SHOP'}, inplace=True)

shop_daily = shop_df.pct_change()
cmg_daily = cmg_df.pct_change()

## CONCAT into one portfolio with all the daily returns
portfolio_df = pd.concat([shop_daily, cmg_daily], axis="columns", join="inner")
daily_portfolio = portfolio_df
daily_portfolio.dropna()

import mplcyberpunk
from matplotlib import style
style.use('cyberpunk')

daily_portfolio.plot(figsize=(18, 10), title="Daily Returns")

cumulative_returns = (1 + daily_portfolio).cumprod()
cumulative_returns.plot(figsize=(16, 10), title="Cumulative Returns")

# Daily Standard Deviations
# Calculate the standard deviation for each portfolio. 
daily_portfolio.std()

# Calculate the annualized standard deviation (252 trading days)
daily_portfolio.std() * np.sqrt(252)

# Construct a correlation table
corr_df = daily_portfolio.corr()
corr_df.style.background_gradient(cmap="summer")

# Calculate a rolling window using the Exponentially Weighted Moving Average. 
daily_portfolio.ewm(halflife=21).std().plot(figsize=(20, 10), title="Exponentially Weighted Average")

# Calculate annualized Sharpe Ratios
sharpe_ratios = (daily_portfolio.mean() * 252) / (daily_portfolio.std() * np.sqrt(252))
# Visualize the sharpe ratios as a bar plot
x=sharpe_ratios.hvplot.barh(figsize=(15, 8), title="Sharpe Ratios", color= 'red')
show(hv.render(x))

# Prepare DataFrame for metrics
metrics = ['SHOP Annual Return', 'CMG Annual Return', 'SHOP Annual Volatility','CMG Annual Volatility','SHOP Sharpe Ratio','CMG Sharpe Ratio']
columns = ['Backtest']
# Initialize the DataFrame with index set to evaluation metrics and column as `Backtest`.

portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)
portfolio_evaluation_df

# Calculate annualized return
portfolio_evaluation_df.loc['SHOP Annual Return'] = daily_portfolio['SHOP'].std() * np.sqrt(252)
portfolio_evaluation_df.loc['CMG Annual Return'] = daily_portfolio['CMG'].std() * np.sqrt(252)
# Calculate annual volatility
portfolio_evaluation_df.loc['SHOP Annual Volatility'] = daily_portfolio['SHOP'].std() * np.sqrt(252)
portfolio_evaluation_df.loc['CMG Annual Volatility'] = daily_portfolio['CMG'].std() * np.sqrt(252)
# Calculate Sharpe Ratio
portfolio_evaluation_df.loc['SHOP Sharpe Ratio'] = sharpe_ratios['SHOP']
portfolio_evaluation_df.loc['CMG Sharpe Ratio'] = sharpe_ratios['CMG']
portfolio_evaluation_df.head(18)

portfolio_evaluation_df.reset_index(inplace=True)
portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table()


show(hv.render(portfolio_evaluation_table))