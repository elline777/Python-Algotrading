from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from yfinance_helper import get_data

import pandas_ta as pta

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    def init(self):
        self.rsi = self.I(pta.rsi, self.data.Close, 14)

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()



# Get the data
data = get_data('GOOG')

data.reset_index(inplace=True)
data['RSI'] = pta.rsi(data.Close, length=14)
print(data)

# bt = Backtest(data, RsiOscillator, cash = 10_000)
# stats = bt.run()
# print(stats)


# print(data.tail())
# print(data.info())
# data.reset_index(inplace=True)
# #data.index = pd.DatetimeIndex(data['Date'])
# data['Date'] = pd.to_datetime(data['Date'])
# data.set_index("Date", inplace=True)
#
# print(data.tail())
# print(data.info())


