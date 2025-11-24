import talib

class TalibCalculator:
    def __init__(self, data):
        self.data = data
        self.close_prices = data['Close'].values

    def calculate_sma(self, period):
        return talib.SMA(self.close_prices, timeperiod=period)

    def calculate_ema(self, period):
        return talib.EMA(self.close_prices, timeperiod=period)

    def calculate_rsi(self, period):
        return talib.RSI(self.close_prices, timeperiod=period)

    def calculate_macd(self, fastperiod=12, slowperiod=26, signalperiod=9):
        macd, macdsignal, macdhist = talib.MACD(self.close_prices, 
                                                 fastperiod=fastperiod, 
                                                 slowperiod=slowperiod, 
                                                 signalperiod=signalperiod)
        return macd, macdsignal, macdhist
    
    