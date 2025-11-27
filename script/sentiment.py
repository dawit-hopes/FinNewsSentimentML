from textblob import TextBlob
import pandas as pd

class SentimentAnalyzer:
    def analyze_sentiment(self, text: str) -> dict:
        """
        Analyzes the sentiment of the given text.

        Parameters:
        text (str): The text to analyze.

        Returns:
        dict: A dictionary containing polarity and subjectivity scores.
        """
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return {
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        }
    

    def perform_analysis(self, stock: str, df: pd.DataFrame) -> float:
        """
        Performs sentiment analysis on a predefined text related to the given stock.

        Parameters:
        stock (str): The stock symbol.

        Returns:
        str: A formatted string with the sentiment analysis results.
        """
        stock_df = pd.read_csv(f"../data/yfinance_data/Data/{stock}.csv")
        stock_df = stock_df.rename(columns={'Date': 'date'})
        stock_df['date'] = pd.to_datetime(stock_df['date'], format="ISO8601")
        stock_df['date']= stock_df['date'].dt.date
        stock_df = stock_df.set_index("date")

        stock_df['daily_returns'] = stock_df['Close'].pct_change()
        df = df[df['stock'] == stock].copy()
        if df.empty:
            print(f"No data available for stock: {stock}")
            return 0.0
        
        df['sentiment_score'] =  df['headline'].apply(
            lambda x: self.analyze_sentiment(x)['polarity']
        )


        daily_sentiment_df = df.groupby("date")['sentiment_score'].mean().reset_index()
        daily_sentiment_df.columns = ['date', 'average_sentiment']


        correlation_df = pd.merge(  stock_df,  daily_sentiment_df,  on='date',  how='inner'   , validate="many_to_many")
        correlation_coefficient = correlation_df['average_sentiment'].corr(
                    correlation_df['daily_returns']
                        )
        
        return correlation_coefficient