from backtesting import Strategy
import pandas as pd
import talib as ta

class BuyAndHold(Strategy):

    def init(self):
        pass

    def next(self):

        if not self.position:
            self.buy()

class BuyAndSellSwitch(Strategy):

    def init(self):
        pass

    def next(self):
        
        if not self.position:
            self.position.close()
            self.buy(size=10)
        else:
            self.position.close()
            self.sell(size=10)