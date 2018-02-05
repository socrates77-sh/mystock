from market_data import stock_data_reader
from analysis import calculat_average
from strategy import average_strategy
from gain import gain_by_strategy, get_all_gain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_gain():

    # gain_result[['all']].plot(kind='barh')
    gain_result[['500d', '250d']].plot(kind='barh')
    plt.show()


def main():
    code = '600708'
    # code = '600029'
    stock_data = stock_data_reader(code)
    analysis_data = calculat_average(stock_data)
    strategy_data = average_strategy(analysis_data)

    gain_result = get_all_gain(strategy_data)

    plot_gain()


if __name__ == '__main__':
    main()
