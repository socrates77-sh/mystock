from market_data import stock_data_reader
import matplotlib.pyplot as plt
import pandas as pd


def main():
    code = '002253'
    code = '600708'
    start = '1998/5/5'
    end = '2018/1/20'
    sd = stock_data_reader(code, start, end)
    sd1 = sd[sd['收盘价'] > 0]
    # sd1.to_csv('a.csv')
    SD = 0.3
    sd1['42d'] = pd.rolling_mean(sd1['收盘价'], window=42)
    sd1['252d'] = pd.rolling_mean(sd1['收盘价'], window=252)
    print(sd1)
    sd1[['收盘价', '42d', '252d']].plot(grid=True, figsize=(12, 6))
    plt.show()


if __name__ == '__main__':
    main()
