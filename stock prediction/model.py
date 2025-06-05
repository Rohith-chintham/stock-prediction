import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import timedelta

def get_stock_data(ticker):
    df = yf.download(ticker, period="1y")
    df.reset_index(inplace=True)
    return df

def predict_next_7_days(df):
    df = df[['Date', 'Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days

    model = LinearRegression()
    model.fit(df[['Days']], df['Close'])

    future_days = np.array([df['Days'].max() + i for i in range(1, 8)]).reshape(-1, 1)
    predictions = model.predict(future_days)

    future_dates = [df['Date'].max() + timedelta(days=i) for i in range(1, 8)]
    return list(zip(future_dates, predictions))
