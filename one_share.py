from market_data import stock_data_reader
from analysis import calculat_average
from strategy import average_strategy
from gain import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_position_days(strategy_data, days=0):
    pos_days = pd.DataFrame(index=avg_strategys, columns=['B', 'S'])
    for ast in avg_strategys:
        if days == 0:
            pos_days['B'][ast] = strategy_data[ast].value_counts(1)[1]
            pos_days['S'][ast] = strategy_data[ast].value_counts(1)[0]
        else:
            pos_days['B'][ast] = strategy_data[ast][-days:].value_counts(1)[1]
            pos_days['S'][ast] = strategy_data[ast][-days:].value_counts(1)[0]
    return pos_days


def main():
    code = '600349'
    # code = '600029'
    stock_data = stock_data_reader(code)
    if stock_data is None:
        print('%06s is a new share without data' % code)
        return

    analysis_data = calculat_average(stock_data)
    strategy_data = average_strategy(analysis_data)
    # if(strategy_data['year'].isnull()[-1]):
    if(strategy_data['前复权'].count() < 500):
        print('%06s is a new share without enough data' % code)
        return

    # analysis_data.to_csv('a.csv')
    # strategy_data.to_csv('s.csv')

    gain_result = get_all_gain(strategy_data)
    # print(get_position_days(strategy_data, 250))

    # all_gain.to_csv('g.csv')

    # gain_result[['500d', '250d']].plot(kind='barh')
    # plt.show()


if __name__ == '__main__':
    main()
