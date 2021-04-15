# Installing and using Yfinance and Ta-LIB

## Installing Jupyter Notebooks
* **Step 1:** Installing Anaconda on your device, Python version 3+ : https://www.anaconda.com/products/individual. Go on the link and scroll to the bottom where you will find installers for Windows, MacOS, Linux systems. 

* **Step 2:** Open Jupyter notebooks to install some basic libraries like yfinance and ta-lib
<h2>

## Installing Yfinance (Yahoo Finance)

* **Why it is useful:** Helps download data on stock price and other important information easily for chosen periods of time.

* **How to install:** Insert 'conda install -c ranaroussi yfinance' into a cell in a jupyter notebook and click run 

### Using the Library

Now that you have it installed, start of by importing yfinance->

*	Import yfinance as yf

To intitialize the stock you want to download data for, use the ticker function in yfinance like this->

*	msft=yf.ticker(“MSFT”)

To download data from a certain time interval in days, use the history function->
*	msfthistory=msft.history(start=”yyyy-mm-dd”, end=”yyyy-mm-dd”, interval=”xx”)
*	msfthistory=mfst.history(period=”xxx”)

For the history function you can use either period or start and end dates to pull data.
*	If you use period, then valid inputs include= “1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”. 
*	D represents day, mo represents month, y represents year, ytd is year to date where you will get data from the beginning of the current year to current day. Max will download all the data that is available for that stock. 
*	If you use start and end dates then your dates should be in the format of year-month-day
*	You can also use interval of data that you want. This interval ranges from “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
*	The m represents minutes, h represents hour and wk represents week. 
*	Restrictions to intervals:
*	You can only get minute to minute data for a time period of 7 days.
*	You can have an interval of lesser than one day for only a time period of 60 days or less. 

You can also download data for multiple stocks at once using->
*	T=yf.download(“APPL MSFT”, start=”yyyy-mm-dd”, end=yyyy-mm-dd”)

To view all the information you can get about the stock->

*	Print(msft.info) 
Or 
* Print(msft.info.keys())

These will let you see the dictionary or different keys in the dictionary so you can pull helpful data calling print(msft.info[“xxx”]) if needed. 
<h2>
  
## Install ta-lib (Technical Analysis Library)

* **Why is it useful:** can calculate values like MACD, RSI etc easily which are widely used for simple trading strategies. 

* **How to install:**  insert 'conda install -c conda-forge ta-lib' into a cell in a jupyter notebook and click run

* **Import it:** Import talib

### Using the Library
*	Download stock data using yfinance
* Create a dataframe using downloaded data. Ex: df=msft.history(start=, end=)

Once the dataframe is created, we can calculate different moving averages and store them by creating a new column. 

Example 1: Simple moving average 
*	df['MA'] = ta.SMA(df['Close'],20)
* Here close represents the closing price of stock at whatever time interval data is downloaded and 20 represents the time period of averages. So in this average of
past 20 intervals is taken. 


You can even plot it using->
*	df[['Close','MA']].plot(figsize=(12,12)) 
*	plt.show()

Other indicators:
*	Exponential Moving Average using: ta.EMA 
*	Relative strength Index: ta.RSI
*	MACD->
*	data["macd"], data["macd_signal"], data["macd_hist"] = talib.MACD(data['Close'])

Here MACD is the moving average convergence divergence. The MACD signal is the 9-day EMA and the MACD histogram which graphs the distance between MACD and its signal line.

To see an example of the libraries being installed look at installations.ipynb or run it on your laptop for easy installation.
<h2>
<h1>
