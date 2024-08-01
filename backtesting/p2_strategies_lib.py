from backtesting.test import SMA, GOOG
import pandas as pd
from backtesting.lib import SignalStrategy, TrailingStrategy
from backtesting import Backtest


class SmaCross(SignalStrategy, TrailingStrategy):
    n1 = 10
    n2 = 25

    def init(self):
        super().init()

        sma1 = self.I(SMA, self.data.Close, self.n1)
        sma2 = self.I(SMA, self.data.Close, self.n2)

        signal = (pd.Series(sma1) > sma2).astype(int).diff().fillna(0)
        signal = signal.replace(-1, 0)

        entry_size = signal * .95
        self.set_signal(entry_size=entry_size)
        self.set_trailing_sl(2)


bt = Backtest(GOOG, SmaCross, commission=0.002)
bt.run()
bt.plot()
