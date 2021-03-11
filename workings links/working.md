# Trading Strategies 
## Article Summaries 


**Title: A Step-by-step Implementation of a Trading Strategy in Python using ARIMA + GARCH models 

Link: https://medium.com/analytics-vidhya/a-step-by-step-implementation-of-a-trading-strategy-in-python-using-arima-garch-models-b622e5b3aa39 
Implementation Method: Python implementation of ARIMA + Garch which is the improvement on Arima And Garch applied in R
Data: S&P Index from 1950-December 2020
Summary: Uses Arima model to fit the log of the closing statement each day and then uses GARCH to fit the residuals from ARIMA. Takes the sum of those to then compare against cumulative gains which is calculative through a cumulative sum of the log of closing values. 
In R and Python, Arima model was fit by looping through several hyper-parameters and choosing lowest AIC. Through the Arima and Garch forecasts, signals are created. Our strategy will simply long the position if the prediction is 1 (up) and short if the prediction is -1 (down). 
Code: Arima+Garch. Sp500_forecasts file needed for the signal


**Title: Python For Trading: An Introduction

Link: https://blog.quantinsti.com/python-trading/
Method: Moving Average Convergence Divergence (MACD)
Performance Evaluation
•	Annualised return,
•	Annualised volatility, and
•	Sharpe ratio.
Has a good explanation from libraries to download to moving averages. Simple strategy to follow and how to check its performance. Good introduction for someone who is new to this but has basic python knowledge. 
**Code: MACD strategy. 

**Link: https://medium.com/analytics-vidhya/python-i-have-tested-a-trading-mathematical-technic-in-realtime-658a80381151

Title: Python for Algorithmic Trading: A to Z test.
Note: About Bollinger Bands 

**Link: https://medium.com/analytics-vidhya/building-a-technical-analysis-chart-with-python-17107b78b297

Title: Building a Technical Analysis Chart with Python
Method: Building MACD, MA10,MA30 and RSI charts
•	Used talib library to get MACD, MA10,MA30 and RSI. Very useful and easy. 
•	Useful resource for pulling data and plotting it using common trading strategies such as MACD. 
•	Good as a starting point. 
Libraries required: Talib, mplfinance 
**Code: Technical Analysis Visualization

**Link: https://medium.com/analytics-vidhya/trading-dashboard-pt-2-yfinance-python-d482678b498d

Title: Trading Dashboard Pt.2 — Yfinance & Python.
Summary/Finding: good for how to pull live data, calculate key indicators such as returns, sharpe ratio and annual volatility and display to compare stocks interested in. 
Libraries: hvplot
**Code:dashboard 


**Link: https://medium.com/dataseries/deepmind-open-sourced-this-new-architecture-to-improve-long-term-memory-in-deep-learning-systems-dab7ed82986f

Title: DeepMind Open Sourced This New Architecture to Improve Long-Term Memory in Deep Learning Systems
Summary/Findings: Talks about deep learning systems and mentions LSTM model and its advantages or disadvantages. Good for people who know about artificial neural networks already. A very brief article though I do not think it has much learning potential.

**Link: https://medium.com/python-in-plain-english/4-python-libraries-to-help-you-make-money-from-webscraping-57ba6d8ce56d

Title: 4 Python Libraries to Help you Make Money from Webscraping
Summary/Findings: It is good for learning basic webscraping using beautiful soup or selenium. However for finance specifically since there is yfinance library that easily pulls data from yahoo, not sure how useful it is. 
Libraries: selenium, bs4
Note: for selenium you need to get the library, get chrome driver and all of that so it is easier to just use bs4. 

**Link: https://medium.com/swlh/automating-your-stock-portfolio-research-with-python-for-beginners-912dc02bf1c2

Title: Automate Your Stock Portfolio Research With Python in 6 Minutes
Summary/Findings: Information on how to pull information on company stocks using APIs
Notes: the code provided had some key errors and errors that other users in comments faced too. 

**Link: https://medium.com/swlh/how-to-create-a-dashboard-to-dominate-the-stock-market-using-python-and-dash-c35a12108c93

Title: How to Create a Dashboard to Dominate the Stock Market Using Python and Dash
Summary/Findings: Helpful for dashboard but very lengthy code to pull live data to create a dashboard. I feel like other resources show easier ways, this is just more visually pleasing. No trading strategies mentioned and uses data from twitter and reddit than calculating any key performance indicators. 
Libraries: Tweepy(twitter), praw(Reddit), dash, dashbootstrap components, flask, plotly


**Link: https://medium.com/swlh/intrinsic-valuation-of-stocks-using-python-5d902a34b1a0

Title: Intrinsic Valuation of Stocks Using Python
Summary/findings: Purpose of this article is to help create a discounted cash flow model in python to calculate intrinsic value of a company. This helps to see whether or not a company is overvalued which can give help information for trading. Not exactly a trading strategy but good exploration of things that are impactful for stock market. 
**Code: Evaluation.

**Link: https://medium.com/swlh/time-series-data-analysis-machine-learning-algorithm-for-stock-trading-2e22a5b3794a

Title: Time-Series Data Analysis & Machine Learning Algorithm for Stock Trading
Summary/Findings: They refer to part 1 about data collection however there is no link to it, so finding data used is tricky. However, this author has several similar articles to look at regarding trading strategies. This part focuses on ML algorithms and hyper -parameter optimization
Financial Factors explored: Variance inflation factor (VIF), Ease of Movement (EVM), Relative Strength Index (RSI), Moving Average (MA)
Notes: Other articles are better sources since they target most of these factors while also including data collection within the same source and better explanation of implementing code. 

**Link: https://mitchellrosenthalofficial.medium.com/crash-course-python-pandas-for-trading-and-investing-part-1-714b77dfdc21

Title: Crash Course — Python & Pandas for Trading and Investing (Part 1)
Summary/Findings: Helpful for imports, creating time series and using moving average to create signals and evaluate returns on investment. 
**Code: Testing moving average

**Link: https://towardsdatascience.com/bollinger-bands-for-stock-trading-theory-and-practice-in-python-7d3e79d30e02
Notes: Uses Bollinger bands


**Link: https://towardsdatascience.com/creating-a-financial-dashboard-with-python-6d8583e38b57

Title: Creating a Financial Dashboard with Python
Summary/Findings: Teaches how to create a dashboard using plotly and dash to view revenue and net income data on any stock entered. 
Looks like link used for API is out of date and the wrong keys are being called. So it makes the dashboard but is not able to load the data. 


**Link:https://towardsdatascience.com/implementation-of-technical-indicators-into-a-machine-learning-framework-for-quantitative-trading-44a05be8e06

Title:Building an ML forecasting tool to predict stock price movement using Technical Indicators on S&P100 companies
Summary/Findings: Uses random forest model to predict stock price movement on S&P100 companies.

**Link: https://towardsdatascience.com/making-a-stock-screener-with-python-4f591b198261

Title:Making a Stock Screener with Python!
Summary/Findings: Used 7 different conidtions on stocks current values to return a dataframe which shows all the stocks that passed or meet the requirements. 
Helpful if you have some criteria in your mind. 
**Code:Screener

**Link:https://towardsdatascience.com/modeling-your-stock-portfolio-performance-with-python-fbba4ef2ef11

Title:Modeling Your Stock Portfolio Performance with Python




<h2> <h1> 



