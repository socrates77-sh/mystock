from market_data import stock_data_reader
from analysis import calculat_average
from strategy import average_strategy
from gain import gain_by_strategy, get_all_gain
import pandas as pd
import numpy as np


def get_share_result(code):
    stock_data = stock_data_reader(code)
    analysis_data = calculat_average(stock_data)
    strategy_data = average_strategy(analysis_data)
    return (get_all_gain(strategy_data), stock_data['名称'][-1])


# def gen_all_fields()


def main():
    code = '600708'
    one_share_result, name = get_share_result(code)
    print(one_share_result)
    print(name)

if __name__ == '__main__':
    main()
