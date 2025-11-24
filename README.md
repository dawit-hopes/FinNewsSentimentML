# FinNewsSentimentML

I worked on analyzing the impact of financial news headlines on stock price movements. The project combines **sentiment analysis** on news with **technical indicators** on stock data to explore correlations between news sentiment and daily returns.

---

## Features

- Sentiment analysis of financial news headlines using NLP  
- Stock data analysis with technical indicators (MA, RSI, MACD)  
- Alignment of news and stock dates to compute daily returns  
- Unit tests for reproducible results  

---

## Setup

### Using Conda

```bash
conda create -n finnews python=3.13
conda activate finnews
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
````

### Run Tests

```bash
python -m unittest discover -s tests -p "*.py"
```

---

## Structure

```
├── src/        # Core scripts
├── notebooks/  # EDA & experiments
├── scripts/    # Utility scripts
├── tests/      # Unit tests
├── requirements.txt
└── README.md
```

---

This project helped me practice integrating **financial data analysis**, **NLP**, and **Python testing workflows** in a reproducible setup.

```

If you want, I can also make an **even shorter “one-page” version** perfect for GitHub front page without sections, just a few sentences and commands. Do you want me to do that?
```
