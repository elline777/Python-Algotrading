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

        if crossover(self.daily_rsi, self.upper_bound):
            self.position.close()

        # elif crossover(self.lower_bound, self.daily_rsi):
        #     self.buy(size=0.1) # 10% of balance

        elif self.lower_bound > self.daily_rsi[-1]:
            self.buy(size=1) # buy 1 share


bt = Backtest(GOOG, RsiOscillator, cash=10_000)
stats = bt.run()
bt.plot()
print(stats['_trades'].to_string())

