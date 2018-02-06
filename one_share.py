from market_data import stock_data_reader
from analysis import calculat_average
from strategy import average_strategy
from gain import gain_by_strategy, get_all_gain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    code = '002830'
    # code = '600029'
    stock_data = stock_data_reader(code)
    analysis_data = calculat_average(stock_data)
    strategy_data = average_strategy(analysis_data)
    # if(strategy_data['year'].isnull()[-1]):
    if(strategy_data['前复权'].count() < 500):
        print('%06s is a new share without enough data' % code)
        return

    analysis_data.to_csv('a.csv')
    strategy_data.to_csv('s.csv')
    print(strategy_data['前复权'].count())

    gain_result = get_all_gain(strategy_data)

    # all_gain.to_csv('g.csv')

    gain_result[['500d', '250d']].plot(kind='barh')
    plt.show()


if __name__ == '__main__':
    main()
