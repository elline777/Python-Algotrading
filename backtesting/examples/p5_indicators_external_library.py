from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import pandas_ta as ta


def indicator(data):
    # Data is going to be our OHLCV
    bbands = ta.bbands(close=data.Close.s, std=1)
    return bbands.to_numpy().T[:3]


class BBStrategy(Strategy):
    def init(self):
        self.bbands = self.I(indicator, self.data)

    def next(self):
        lower_band = self.bbands[0]
        upper_band = self.bbands[2]

        if self.position:
            if self.data.Close[-1] > upper_band[-1]:
                self.position.close()
        else:
            if self.data.Close[-1] < lower_band[-1]:
                self.buy()


# print(help(ta.bbands))
bt = Backtest(GOOG, BBStrategy, cash=10_000)
stats = bt.run()
print(stats)
bt.plot()
