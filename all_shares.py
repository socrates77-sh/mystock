from market_data import stock_data_reader
from analysis import calculat_average
from strategy import average_strategy
from gain import *
import pandas as pd
import numpy as np
import csv
import msvcrt
# import getch


def one_period_index(period):
    index = []
    index.append('avg-' + period)
    index.append('max-' + period)
    index.append('strategy-' + period)
    index.append('bs-' + period)
    for ast in avg_strategys:
        index.append(ast + '-' + period)
    return index


def gen_index():
    index = ['name']
    index += one_period_index('250d')
    index += one_period_index('500d')
    index += one_period_index('all')
    return index


def fill_result_by_period(result, all_gain, strategy_data, period):
    for ast in avg_strategys:
        result[ast + '-' + period][0] = all_gain.loc[ast][period]
    result['avg-' + period] = all_gain.mean()[period]
    result['max-' + period] = all_gain.max()[period]
    strategy = all_gain[period].argmax()
    result['strategy-' + period] = strategy
    bs = 'B' if strategy_data[strategy][-1] == 1 else 'S'
    result['bs-' + period] = bs


def print_result(code, result):
    print('%s\t%10s\t%0.3f\t%0.3f\t%s\t%s' %
          (code, result['name'][0],
           result['avg-250d'][0], result['max-250d'][0],
           result['strategy-250d'][0], result['bs-250d'][0]))


def get_share_result(code):
    stock_data = stock_data_reader(code)
    if stock_data is None:
        print('%06s no enough data [1]' % code)
        return

    analysis_data = calculat_average(stock_data)
    strategy_data = average_strategy(analysis_data)

    if(strategy_data['前复权'].count() < 500):
        print('%06s no enough data [2]' % code)
        return

    all_gain = get_all_gain(strategy_data)
    result = pd.DataFrame(index=["'" + code], columns=gen_index())
    result['name'][0] = stock_data['名称'][-1]
    fill_result_by_period(result, all_gain, strategy_data, '250d')
    fill_result_by_period(result, all_gain, strategy_data, '500d')
    fill_result_by_period(result, all_gain, strategy_data, 'all')
    # analysis_data.to_csv('a.csv')
    # strategy_data.to_csv('s.csv')
    # all_gain.to_csv('g.csv')
    print_result(code, result)
    return result


def read_code_list(list_file):
    csv_reader = csv.reader(open(list_file, 'r'))
    codes = []
    for code in csv_reader:
        codes.append(code[0])
    return codes


def get_choice():
    print('Choose:')
    print('[1]: position')
    print('[2]: concern')
    print('[3]: all')
    print('press other key to quit')
    return msvcrt.getch()


def main():
    key = get_choice()
    if key == b'1':
        kind = 'position'
    elif key == b'2':
        kind = 'concern'
    elif key == b'3':
        kind = 'all'
    else:
        return

    print('=' * 50)
    print(kind)
    print('=' * 50)

    list_file = kind + '.csv'

    results = pd.DataFrame()
    share_codes = read_code_list(list_file)
    for sc in share_codes:
        result = get_share_result(sc)
        results = results.append(result)
    results.to_csv('result_' + kind + '.csv')

if __name__ == '__main__':
    main()
