from backtesting import Backtest
import yfinance as yf
import pandas as pd
from strategies import sample, moving_average

def load_data(ticker, start_date, end_date, interval_period):
    return yf.Ticker(ticker).history(start=start_date, end=end_date, interval=interval_period)

def main():

    data = load_data(ticker='AAPL', start_date='2000-01-01', end_date='2020-12-31', interval_period='1d')
    
    bt = Backtest(data, moving_average.EMACrossover, cash=10000, commission=0.002)
    bt2 = Backtest(data, moving_average.SMACrossover, cash=10000, commission=0.002)

    bt_metrics = bt.run(short_window=12, long_window=24)
    bt2_metrics = bt2.run(short_window=12, long_window=24)

    bt.plot()
    bt2.plot()

    print(bt_metrics)
    print(bt2_metrics)

if __name__ == "__main__":
    main()
    