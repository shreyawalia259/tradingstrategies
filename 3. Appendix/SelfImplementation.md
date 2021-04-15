# Implement Trading strategies/ Data Visualization

## Moving Average Convergence Divergence (MACD)

* This average is one of the most commonly used trading strategies because it is easy to implement and works fairly well. The MACD is calculated by taking the difference of the 12-day exponential moving average and 26-day exponential moving average. 
*	Finally, a 9-day exponential moving average is taken from the MACD series and counted as the signal for the MACD series. Whenever MACD values are larger than the signal, you should buy the stock and whenever it dips below, you sell it. 

*	They way this is checked in python is by creating a signal of 1 whenever MACD is greater than its signal and -1 otherwise.

* MACD can be calculated using functions in pandas or the Technical analysis Library(ta-lib).

*	An implementation of pandas can be found in the MACD strategy file and ta-lib in the technical analysis visualization file. 

<h2>
<h1>