## Installations:
The installation file is a Jupyter notebook containing commands to run all the libraries needed to run Case Studies 1-7 successfully.
<h2>

## Libraries and Self Impementation
This is a guide to using the yfinance and Ta-lib libraries that are extremely useful in pulling data on stocks and calculating measures such as moving averages. 
 
## Case Study 1-7: 
These case studies are Jupyter notebooks containing applied strategies on stock data trends to get higher cummulative returns or ways to successfully visualiz those trends.

### Case Study 1 & sp500_forecasts:
* Link: https://medium.com/analytics-vidhya/a-step-by-step-implementation-of-a-trading-strategy-in-python-using-arima-garch-models-b622e5b3aa39
* Implementation Method: Python implementation of ARIMA + Garch which is the improvement on Arima And Garch applied in R
* Data: S&P Index from 1950-December 2020
* Summary: Uses Arima model to fit the log of the closing statement each day and then uses GARCH to fit the residuals from ARIMA. Takes the sum of those to then compare against cumulative gains which is calculative through a cumulative sum of the log of closing values.
* The sp500_forecasts file is used as a signal from the baseline strategy to compare cummulative returns to the new applied strategy by case study 1.
<h3>

### Case Study 2:
**Intrinsic Valuation of Stocks Using Python**
* Link: https://medium.com/swlh/intrinsic-valuation-of-stocks-using-python-5d902a34b1a0
* Summary: Purpose of this article is to help create a discounted cash flow model in python to calculate intrinsic value of a company. This helps to see whether or not a company is overvalued which can give help information for trading. Not exactly a trading strategy but good exploration of things that are impactful for stock market.
<h3>
 
### Case Study 3:
**Python For Trading: An Introduction**
* Link: https://blog.quantinsti.com/python-trading/
* Method: Moving Average Convergence Divergence (MACD)
* Summary: Has a good explanation from libraries to download to moving averages. Simple strategy to follow and how to check its performance. Good introduction for someone who is new to this but has basic python knowledge.
<h3>
 
### Case Study 4:
**Building a Technical Analysis Chart with Python**
* Link: https://medium.com/analytics-vidhya/building-a-technical-analysis-chart-with-python-17107b78b297
* Method: Building MACD, MA10,MA30 and RSI charts
* Summary: Used talib library to get MACD, MA10,MA30 and RSI. Easy and Useful resource for pulling data and plotting it using common trading strategies such as MACD.
<h3>  

### Case Study 5:
**Trading Dashboard Pt.2 — Yfinance & Python.**
* Link: https://medium.com/analytics-vidhya/trading-dashboard-pt-2-yfinance-python-d482678b498d
* Summary/Finding: good for how to pull live data, calculate key indicators such as returns, sharpe ratio and annual volatility and display to compare stocks interested in.
<h3>
 
### Case Study 6:
**Crash Course — Python & Pandas for Trading and Investing (Part 1)**
* Link: https://mitchellrosenthalofficial.medium.com/crash-course-python-pandas-for-trading-and-investing-part-1-714b77dfdc21
* Summary/Findings: Helpful for imports, creating time series and using moving average to create signals and evaluate returns on investment. This case study uses random number generation for stock prices instead of a real one.
<h3>

### Case Study 7:
**Making a Stock Screener with Python!**
* Link: https://towardsdatascience.com/making-a-stock-screener-with-python-4f591b198261
* Summary: Used 7 different conidtions on stocks current values to return a dataframe which shows all the stocks that passed or meet the requirements.
Note: Helpful if you have some criteria to screen stocks out in your mind.

<h3>
<h2>


 
