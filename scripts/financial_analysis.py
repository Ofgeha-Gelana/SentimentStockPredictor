import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob
# import talib as tl


def load_historical_data(ticker):
    stock_data=pd.read_csv(f'../data/raw/yfinance_data/{ticker}_historical_data.csv')
    return stock_data



def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity


def getSentimentAnalysisOfPublisher(news_data, target_publisher):
    colors = {'positive': 'green', 'negative': 'red', 'neutral': 'blue'}
    # Filter data for the target publisher
    publisher_data = news_data[news_data['publisher'] == target_publisher]
    sentiment_counts = publisher_data['sentiment_score_word'].value_counts().sort_index()

    sentiment_counts.plot(kind="bar", figsize=(10, 4), title=f'Sentiment Analysis of {target_publisher}',
                      xlabel='Sentiment categories', ylabel='Number of Published Articles',
                      color=[colors[category] for category in sentiment_counts.index])



def checkMissingValueOfHistoricalDataset(stock_data_aapl,stock_data_amzn,stock_data_goog,stock_data_meta,stock_data_msft,stock_data_nvda,stock_data_tsla):
    combined_df = pd.concat([stock_data_aapl.isnull().sum(),
                            stock_data_goog.isnull().sum(),
                            stock_data_amzn.isnull().sum(),
                            stock_data_msft.isnull().sum(),
                            stock_data_meta.isnull().sum(),
                            stock_data_nvda.isnull().sum(),
                            stock_data_tsla.isnull().sum()],
                            axis=0)
    combined_df.head()