from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover

import talib


class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.daily_rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

    def next(self):
        price = self.data.Close[-1]

        if crossover(self.daily_rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.daily_rsi):
            self.buy(tp=1.15*price, sl=0.95 * price)


bt = Backtest(GOOG, RsiOscillator, cash=10_000)
stats = bt.run()
bt.plot()
print(stats)

