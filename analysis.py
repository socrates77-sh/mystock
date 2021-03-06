import pandas as pd
import numpy as np
import warnings

warnings.simplefilter('ignore')


def calculat_average(stock_data):
    # 5d: week average
    # 20d: month average
    # 60d: quarter average
    # 120d: half year average
    # 250d: year average

    sd = stock_data.copy()
    # sd['week'] = pd.rolling_mean(sd['前复权'], window=5)
    # sd['month'] = pd.rolling_mean(sd['前复权'], window=20)
    # sd['quarter'] = pd.rolling_mean(sd['前复权'], window=60)
    # sd['half-year'] = pd.rolling_mean(sd['前复权'], window=120)
    # sd['year'] = pd.rolling_mean(sd['前复权'], window=250)

    sd['week'] = pd.Series.rolling(sd['前复权'], window=5, center=False).mean()
    sd['month'] = pd.Series.rolling(sd['前复权'], window=20, center=False).mean()
    sd['quarter'] = pd.Series.rolling(
        sd['前复权'], window=60, center=False).mean()
    sd['half-year'] = pd.Series.rolling(sd['前复权'],
                                        window=120, center=False).mean()
    sd['year'] = pd.Series.rolling(sd['前复权'], window=250, center=False).mean()

    return sd
