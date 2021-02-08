import pandas as pd
import numpy as np
import yfinance as yf

# Load the forecasts
forecasts = pd.read_csv('sp500_forecasts_new.csv', header=None).rename(columns={0: 'Date', 1: 'Signal'})
forecasts.set_index('Date', inplace=True)
forecasts.index = pd.to_datetime(forecasts.index)

# load the SP500 df
df = yf.Ticker('^GSPC').history(period='max')
df = df[(df.index > '1952-01-03') & (df.index < '2020-12-30')]

# save the strategy signal
df['Signal'] = forecasts['Signal']
df.head()

df['LogRets'] = np.log(df['Close'] / df['Close'].shift(1))
df['StratLogRets'] = df['LogRets'] * df['Signal']

df['BuyHold_Log_Returns'] = df['LogRets'].cumsum()
df['Strategy_Log_Returns'] = df['StratLogRets'].cumsum()

df['BuyHold_Returns'] = np.exp(df['BuyHold_Log_Returns'])
df['Strategy_Returns'] = np.exp(df['Strategy_Log_Returns'])

_ = df[['BuyHold_Returns', 'Strategy_Returns']].plot(figsize=(15, 7), logy=True)

import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


class Stock:
    def __init__(self, ticker, start=None, end=None):
        self.ticker = ticker

        try:
            self._ticker = yf.Ticker(self.ticker)

            if not (start or end):
                self.df = self.df_ = self._ticker.history(period='max')

            else:
                self.df = self.df_ = self._ticker.history(start=start, end=end)

        except Exception as err:
            print(err)

    def change_date_range(self, start=None, end=None):
        """Change the start and end dates of the visible dataframe. The property df_ is kept under the
        hoods to avoid reloading from yahoo all the time"""
        start = self.start_date if start is None else start
        end = self.end_date if end is None else end

        self.df = self.df_[(self.df_.index >= start) & (self.df_.index <= end)]

    def get_value_by_index(self, index, column):
        """When the date index does not exist, get the following date"""
        index = pd.to_datetime(index)
        if index in self.df.index:
            return self.df.loc[index, column]
        else:
            return self.df.loc[self.df.index > index].iloc[0][column]

    def calc_return(self, start=None, end=None):
        """Calc the simple return of the portfolio within a given date range.
        If no range is specified, calc it using the full visible period"""
        start = self.start_date if start is None else start
        end = self.end_date if end is None else end

        first = self.get_value_by_index(start, 'Close')
        last = self.get_value_by_index(end, 'Close')

        return (last-first)/first

    def add_signal_strategy(self, df_signal, column_name='Signal'):
        df_signal.index = pd.to_datetime(df_signal.index)
        self.df.loc[self.df.index, 'StratSignal'] = df_signal.loc[self.df.index, column_name]

        self.df['StratLogRets'] = self.df['LogRets'] * self.df['StratSignal']
        self.df.loc[self.df.index, 'CumStratLogRets'] = self.df['StratLogRets'].cumsum()
        self.df.loc[self.df.index, 'CumStratRets'] = np.exp(self.df['CumStratLogRets'])

    def compare_strategy(self, start=None, end=None, log=False, **kwargs):
        start = self.start_date if start is None else pd.to_datetime(start)
        end = self.end_date if end is None else pd.to_datetime(end)

        # create a copy of the period of interest
        df = self.df.loc[(self.df.index > start) & (self.df.index < end),
                         ['Close', 'LogRets', 'StratLogRets']].copy()

        df['CumLogRets'] = df['LogRets'].cumsum()
        df['CumRets'] = 100*(np.exp(df['CumLogRets'])-1)

        df['CumStratLogRets'] = df['StratLogRets'].cumsum()
        df['CumStratRets'] = 100*(np.exp(df['CumStratLogRets'])-1)

        buy_hold = self.calc_return(start=start, end=end)
        strategy = np.exp(df.loc[df.index[-1], 'CumStratLogRets'])-1

        pct_pos_returns = (df['LogRets'] > 0).mean() * 100
        pct_strat_pos_returns = (df['StratLogRets'] > 0).mean() * 100



        if log:
            columns = ['CumLogRets', 'CumStratLogRets']
            rename = {'CumLogRets': 'Buy and Hold Cumulative Log Returns',
                      'CumStratLogRets': 'Strategy Cumulative Log Returns'}
        else:
            columns = ['CumRets', 'CumStratRets']
            rename = {'CumRets': 'Buy and Hold Returns',
                      'CumStratRets': 'Strategy Returns'}

        df[columns].rename(columns=rename).plot(**kwargs)
        return df

    # ************* PROPERTIES ***************
    @property
    def is_filled(self): return len(self.df) != 0

    @property
    def start_date(self): return str(self.df.index[0])
    @start_date.setter
    def start_date(self, value): self.change_date_range(start=value)

    @property
    def end_date(self): return str(self.df.index[-1])
    @end_date.setter
    def end_date(self, value): self.change_date_range(end=value)

    # ************* INDICATORS ***************
    def add_volatility(self, period=10):
        self.df['volatility'] = self.df['Close'].rolling(period).std() / \
                                self.df['Close'].rolling(period).mean()

    def add_sma(self, period=10):
        self.df[f"sma-{period}"] = self.df['Close'].rolling(period).mean()

    def add_ema(self, period=10):
        self.df[f'ema-{period}'] = self.df['Close'].ewm(span=period).mean()

    def add_log_return(self):
        self.df.loc[self.df.index, 'LogRets'] = np.log(self.df['Close'] / self.df['Close'].shift(1))
        self.df.loc[self.df.index[0], 'LogRets'] = 0
        self.df.loc[self.df.index, 'CumLogRets'] = self.df['LogRets'].cumsum()
        self.df.loc[self.df.index, 'CumRets'] = np.exp(self.df['CumLogRets'])

    # ************* GRAPHS ***************
    def plot(self, columns=['Close'], start=None, end=None, figsize=(20,10)):

        # convert the columns to a list
        columns = [columns] if not isinstance(columns, list) else columns

        start = self.start_date if start is None else start
        end = self.end_date if end is None else end

        df = self.df[(self.df.index >= start) & (self.df.index <= end)]

        plt.figure(figsize=figsize)

        for column in columns:
            plt.plot(df.index, df[column], label=column)

        plt.legend()

    def __len__(self):
        return len(self.df)

    def __repr__(self):
        if self.is_filled:
            s = f'Stock: {self.ticker} - start: {self.start_date[:10]} end: {self.end_date[:10]}'
        else:
            s = f'Stock {self.ticker} as no history'
        return s




gspc = Stock('^GSPC')
gspc.start_date = '2000-01-01'
gspc.end_date = '2020-12-31'
gspc.add_log_return()
gspc.df

spReturns = gspc.df['LogRets']
windowLength = 500
foreLength = len(spReturns) - windowLength

windowed_ds = []
for d in range(foreLength-1):
    windowed_ds.append(spReturns[d:d + windowLength])

# create the forecasts dataframe initialized with zeros
forecasts = spReturns.iloc[windowLength:].copy() * 0

windowed_ds[0], forecasts, windowed_ds[-1]

import pmdarima
import arch

import warnings
warnings.filterwarnings("ignore")

def fit_arima(series, range_p=range(0, 6), range_q=range(0, 6)):
    final_order = (0, 0, 0)
    best_aic = np.inf
    arima = pmdarima.ARIMA(order=final_order)

    for p in range_p:
        for q in range_q:
            if (p==0) and (q==0):
                next
            arima.order = (p, 0, q)
            arima.fit(series)

            aic = arima.aic()

            if aic < best_aic:
                best_aic = aic
                final_order = (p, 0, q)
                
    arima.order=final_order
    return arima.fit(series)
for i, window in enumerate(windowed_ds):
    # ARIMA model
    arima = fit_arima(window)
    arima_pred = arima.predict(n_periods=1)
    
    # GARCH model
    garch = arch.arch_model(arima.resid())
    garch_fit = garch.fit(disp='off', show_warning=False, )
    garch_pred = garch_fit.forecast(horizon=1).mean.iloc[-1]['h.1']    
    
    forecasts.iloc[i] = arima_pred + garch_pred
    
    print(f'Date {str(forecasts.index[i].date())} : Fitted ARIMA order {arima.order} - Prediction={forecasts.iloc[i]}')
# First, we will save our newly created signals
forecasts.to_csv('new_python_forecasts.csv')

# Get the period of interest
forecasts = forecasts[(forecasts.index>='2002-01-01') & (forecasts.index<='2020-12-31')]

# Get the direction of the predictions
forecasts['Signal'] = np.sign(forecasts['Signal'])

gspc.add_signal_strategy(forecasts, column_name='Signal')

df = gspc.compare_strategy(start='2002-01-02', end='2010-12-01', figsize=(15,7))
plt.ylabel('Strategies Return (%)')

# to add the baseline to the analysis
# Load the baseline forecasts again
baseline = pd.read_csv('sp500_forecasts_new.csv', header=None).rename(columns={0: 'Date', 1: 'Signal'})
baseline.set_index('Date', inplace=True)
baseline.index = pd.to_datetime(baseline.index)

# filter it to the desired period
baseline = baseline[(baseline.index>='2002-01-01') & (baseline.index<='2010-12-31')]

# Create the baseline singal into the output dataframe of our last comparison
df['BaselineSignal'] = baseline['Signal']
df['BaselineLogRets'] = df['LogRets'] * df['BaselineSignal']
df['CumBaselineLogRets'] = df['BaselineLogRets'].cumsum()
df['BaselineRets'] = 100*(np.exp(df['CumBaselineLogRets']) - 1)

# plot the comparison
rename_columns = {'CumRets': 'Buy and Hold Returns',
                  'CumStratRets': 'Strategy Returns', 
                  'BaselineRets': 'Baseline Returns'}

df.loc[df.index>'2000-01-01',['CumRets', 'CumStratRets', 'BaselineRets']].rename(columns=rename_columns).plot(figsize=(15, 7))
