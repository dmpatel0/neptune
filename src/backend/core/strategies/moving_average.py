from backtesting import Strategy
from backtesting.lib import crossover
import talib as ta

class SMACrossover(Strategy):

    short_window = 10
    long_window = 20

    def init(self):

        short_window = self.short_window
        long_window = self.long_window

        self.sma = self.I(self.SMA, self.data.Close, short_window)
        self.lma = self.I(self.SMA, self.data.Close, long_window)

    def next(self):

        if crossover(self.sma, self.lma):
            self.position.close()
            self.buy()
        elif crossover(self.lma, self.sma):
            self.position.close()
            self.sell()
    
    def SMA(self, values, n):
        return ta.MA(values, timeperiod=n)

class EMACrossover(Strategy):

    short_window = 10
    long_window = 20

    def init(self):
        
        short_window = self.short_window
        long_window = self.long_window

        self.sema = self.I(self.EMA, self.data.Close, short_window)
        self.lema = self.I(self.EMA, self.data.Close, long_window)

    def next(self):

        if crossover(self.sema, self.lema):
            self.position.close()
            self.buy()
        elif crossover(self.lema, self.sema):
            self.position.close()
            self.sell()
    
    def EMA(self, values, n):
        return ta.EMA(values, timeperiod=n)