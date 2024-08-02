from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover

import talib


class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
        print(talib.RSI(self.data.Close, self.rsi_window))

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()


bt = Backtest(GOOG, RsiOscillator, cash=10_000)
stats = bt.run()
print(stats)
bt.plot()

# lower_bound = stats['_strategy'].lower_bound
# bt.plot(filename=f'plots/{lower_bound}.html')
