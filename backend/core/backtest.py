from backtesting import Backtest
import yfinance as yf
import pandas as pd
from .strategies import sample, moving_average
import json

def load_data(ticker, start_date, end_date, interval_period):
    return yf.Ticker(ticker).history(start=start_date, end=end_date, interval=interval_period)

def get_metrics(stock, sDate, eDate, useStrategy, interval):

    data = load_data(ticker=stock, start_date=sDate, end_date=eDate, interval_period=interval)
    strategy = ''

    match useStrategy:
        case 'SMA':
            strategy = moving_average.SMACrossover
        case 'EMA':
            strategy = moving_average.EMACrossover
        case _:
            strategy = sample.BuyAndHold

    bt = Backtest(data, strategy, cash=10000, commission=0.002)

    results = bt.run(short_window=12, long_window=24)
    metrics = results[:20]

    bt.plot(filename='frontend/templates/graph.html', open_browser=False)

    return metrics


def main():

    data = load_data(ticker='AAPL', start_date='2000-01-01', end_date='2020-12-31', interval_period='1d')
    
    bt = Backtest(data, moving_average.EMACrossover, cash=10000, commission=0.002)

    bt_metrics = bt.run(short_window=12, long_window=24)
    #bt_metrics = bt_metrics.to_json()

    bt.plot(filename='frontend/templates/graph.html', open_browser=False)

    #print(bt_metrics)
    result = bt._results
    test_res = result.__repr__()
    print(test_res)
    print(json.dumps(test_res))
    #print(json.dumps(result))

if __name__ == "__main__":
    main()
    