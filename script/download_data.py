import yfinance as yf
import pandas as pd

class DataDownloader:
    """
    A class to download financial data using yfinance library.
    """
    def download_stock_data(self, ticker: str, start_date: str, end_date: str, interval='1y') -> pd.DataFrame:
        """
        Downloads historical stock data for a given ticker symbol.

        Parameters:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date for the data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data in 'YYYY-MM-DD' format.
        interval (str): The data interval (e.g., '1d', '1wk', '1mo', '1y').

        Returns:
        pandas.DataFrame: A DataFrame containing the historical stock data.
        """
        data = yf.download(ticker, start=start_date, end=end_date, interval=interval, auto_adjust=False)
        return data
    
    def download_multiple_stocks(self, tickers: list, start_date:str, end_date:str, interval='1d') -> dict:
        """
        Downloads historical stock data for multiple ticker symbols.

        Parameters:
        tickers (list): A list of stock ticker symbols.
        start_date (str): The start date for the data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data in 'YYYY-MM-DD' format.
        interval (str): The data interval (e.g., '1d', '1wk', '1mo', '1y').

        Returns:
        dict: A dictionary with ticker symbols as keys and their corresponding
              historical stock data as pandas DataFrames.
        """
        data_dict = {}
        for ticker in tickers:
            data_dict[ticker] = self.download_stock_data(ticker, start_date, end_date, interval)
        return data_dict
    

        
        
    