from pynance import portfolio_optimizer as po

class PortfolioManager:
    def __init__(self, tickers):
        self.tickers = tickers

    def optimize_portfolio(self):
        portfolio = po.PortfolioCalculations(self.tickers)

        print("Max Sharpe Portfolio (risk/return):")
        print(portfolio.max_sharpe_portfolio("rr"))

        print("\nMax Sharpe Portfolio Weights:")
        print(portfolio.max_sharpe_portfolio("df").head())

        print("\nMinimum Variance Portfolio (risk/return):")
        print(portfolio.min_var_portfolio("rr"))

        print("\nMinimum Variance Portfolio Weights:")
        print(portfolio.min_var_portfolio("df").head())
