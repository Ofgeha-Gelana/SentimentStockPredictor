# Analyzing Financial News and Stock Prices

## Overview
This project aims to analyze financial news data and its correlation with stock price movements. By combining sentiment analysis, technical analysis, and correlation analysis.

## Data
- **News Data** and **Stock Price Data** of (AAPL, AMZN, GOOG, MSFT, META, and TSLA)

## Methodology

### Data Cleaning and Preparation:
1. Clean and preprocess the news data to remove noise, inconsistencies, and irrelevant information.
2. Load stock price data into a Pandas DataFrame.

![Publishing Time Analysis](https://raw.githubusercontent.com/Ofgeha-Gelana/SentimentStockPredictor/refs/heads/task-2/src/output2.png)

This plot shows the publishing times of financial news articles. It visualizes when news is most commonly released, which can be crucial for traders and automated trading systems.

### Sentiment Analysis:
1. Conduct sentiment analysis on news headlines using **TextBlob**.
2. Calculate sentiment scores for each article.

### Technical Analysis:
1. Apply technical indicators (e.g., RSI, SMA, EMA, MACD) to the stock price data.
2. Analyze trends, patterns, and potential trading signals.

### Correlation Analysis:
1. Aggregate sentiment scores by date.
2. Calculate the correlation between sentiment scores and daily stock returns.

## Libraries and Tools
- **Python**: The primary programming language used for the analysis.
- **Pandas**: For data manipulation and analysis.
- **NLTK or TextBlob**: For natural language processing and sentiment analysis.
- **TA-Lib**: For technical analysis calculations.
- **Matplotlib or Seaborn**: For data visualization.

## Future Work
1. **Expand the dataset**: Include a larger dataset with more diverse news sources and stock tickers.
2. **Explore other factors**: Analyze the impact of other factors (e.g., economic indicators, company-specific news) on stock prices.
3. **Develop predictive models**: Build machine learning models to predict stock price movements based on news sentiment and other factors.
