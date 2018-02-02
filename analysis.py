from market_data import stock_data_reader
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.simplefilter('ignore')


def main():
    code = '002253'
    code = '600708'
    start = '1900/1/1'
    end = datetime.now().strftime('%Y%m%d')
    sd = stock_data_reader(code, start, end)
    sd1 = sd[sd['收盘价'] > 0]
    print(sd1.head())
    sd1['涨跌幅'] = sd1['涨跌幅'].apply(lambda x: float(x) / 100 + 1)
    sd1['涨跌幅'][0] = 1.0
    print(sd1.head())

    sd1['累计涨跌幅'] = sd1['涨跌幅'].cumprod()
    last_close_price = sd1['收盘价'][-1]
    last_cum_change_ratio = sd1['累计涨跌幅'][-1]
    print(sd1.head())
    print(last_close_price, last_cum_change_ratio)

    sd1['前复权'] = sd1['累计涨跌幅'].apply(
        lambda x: last_close_price * x / last_cum_change_ratio)
    print(sd1.head())
    print(sd1.tail())

    # sd1['累计涨跌幅'] = np.log(1 + sd1['涨跌幅'] / 100.0)
    # print(sd1.head())
    # sd1['前复权'] = 0.0
    # sd1['前复权'][0] = sd1['收盘价'][0]
    # print(sd1.head())
    # sd1['前复权'] = sd1['收盘价'].shift(1) / (sd1['涨跌幅'] / 100 + 1)
    # sd1['前复权'] = sd1['收盘价'].shift(1)
    # print(sd1.head())

    # sd1.to_csv('a.csv')
    SD = 0.3
    sd1['42d'] = pd.rolling_mean(sd1['前复权'], window=42)
    sd1['252d'] = pd.rolling_mean(sd1['前复权'], window=252)
    # print(sd1)
    sd1[['收盘价', '前复权', '42d', '252d']].plot(grid=True, figsize=(12, 6))
    plt.show()

    print(datetime.now())


if __name__ == '__main__':
    main()
