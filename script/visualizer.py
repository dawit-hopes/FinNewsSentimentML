import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data, ticker):
        self.data = data
        self.ticker  = ticker

    def plot_sma_ema_close(self,):
        """
        Plots the closing prices along with SMA and EMA on the same graph.
        Assumes that 'SMA' and 'EMA' columns are already present in self.data.
        """

        _, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.data.index, self.data['Close'], label='Close Price', color='blue',)
        ax.plot(self.data.index, self.data['SMA_20'], label='SMA', color='orange', linestyle='--')
        ax.plot(self.data.index, self.data['EMA_20'], label='EMA', color='green', linestyle='-')
        ax.set_title(f'Closing Prices with SMA and EMA {self.ticker}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend()
        plt.show()
      
    def plot_rsi(self):
        """
        Plots the RSI values.
        Assumes that 'RSI' column is already present in self.data.
        """

        _, ax = plt.subplots(figsize=(12, 4))
        ax.plot(self.data.index, self.data['RSI'], label='RSI', color='purple')
        ax.axhline(70, color='red', linestyle='--', label='Overbought (70)')
        ax.axhline(30, color='green', linestyle='--', label='Oversold (30)')
        ax.set_title(f'Relative Strength Index (RSI) {self.ticker}')
        ax.set_xlabel('Date')
        ax.set_ylabel('RSI Value')
        ax.legend()
        plt.show()

    def plot_macd(self):
        """
        Plots the MACD line, signal line, and MACD histogram.
        Assumes that 'MACD', 'MACD_Signal', and 'MACD_Hist' columns are already present in self.data.
        """

        _, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.data.index, self.data['MACD'], label='MACD', color='blue')
        ax.plot(self.data.index, self.data['MACD_Signal'], label='Signal Line', color='orange')
        ax.bar(self.data.index, self.data['MACD_Hist'], label='MACD Histogram', color='gray')
        ax.set_title(f'MACD Indicator {self.ticker}')
        ax.set_xlabel('Date')
        ax.set_ylabel('MACD Value')
        ax.legend()
        plt.show()

        print("\n\n") 


        # AMZN, META, MSFT, NVDA