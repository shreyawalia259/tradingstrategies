# tradingstrategies


**Title: A Step-by-step Implementation of a Trading Strategy in Python using ARIMA + GARCH models

Link: https://medium.com/analytics-vidhya/a-step-by-step-implementation-of-a-trading-strategy-in-python-using-arima-garch-models-b622e5b3aa39 

Implementation Method: Python implementation of ARIMA + Garch which is the improvement on Arima And Garch applied in R

Data: S&P Index from 1950-December 2020

Summary: Uses Arima model to fit the log of the closing statement each day and then uses GARCH to fit the residuals from ARIMA. Takes the sum of those to then compare against cumulative gains which is calculative through a cumulative sum of the log of closing values. 
In R and Python, Arima model was fit by looping through several hyper-parameters and choosing lowest AIC. Through the Arima and Garch forecasts, signals are created. Our strategy will simply long the position if the prediction is 1 (up) and short if the prediction is -1 (down). 

**Reproducibility: All the code in R and python is reproducible and is in the arima+garch R/python files. Sp500_forecasts file needed for the signal


**Title: Python For Trading: An Introduction
Link: https://blog.quantinsti.com/python-trading/

Method: Moving Average Convergence Divergence (MACD)

Performance Evlauation
•	Annualised return,
•	Annualised volatility, and
•	Sharpe ratio.

Has a good explanation from libraries to download to moving averages. Simple strategy to follow and how to check its performance. Good introduction for someone who is new to this but has basic python knowledge. **All code is reproducibile in the MACD file. 

**Title:




