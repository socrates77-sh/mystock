import requests
import pandas as pd
from dateutil.parser import parse
import os

# 网易股票数据下载链接如下
# http://quotes.money.163.com/service/chddata.html?code=1002253&start=19900606&end=20180331&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP
# code: 第一位代表沪市0, 深市1；后6位是股票代码
# start: 起始日期，可以设为比最早的数据更早
# end: 截止日期，可以设为比最晚的数据更晚
# fields: TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP
# 对应为 收盘价,最高价,最低价,开盘价,前收盘,涨跌额,涨跌幅,换手率,成交量,成交金额,总市值,流通市值


def code_prefix(stock_code):
    if stock_code.startswith('6'):
        return '0'
    else:
        return '1'


def regulate_date(date_string):
    dt = parse(date_string)
    return dt.strftime('%Y%m%d')


def get_useful_feilds(original_df):
    df = original_df[original_df['收盘价'] > 0]
    df = df.replace('None', 0)
    df['变动率'] = df['涨跌幅'].apply(lambda x: float(x) / 100 + 1)
    df['变动率'][0] = 1.0
    df['累计变动率'] = df['变动率'].cumprod()
    last_close_price = df['收盘价'][-1]
    last_cum_change_ratio = df['累计变动率'][-1]
    df['前复权'] = df['累计变动率'].apply(
        lambda x: last_close_price * x / last_cum_change_ratio)
    return df


def stock_data_reader(stock_code, start='19000101', end='21001231'):
    url = 'http://quotes.money.163.com/service/chddata.html'
    fields = 'TCLOSE;PCHG'
    code_with_prefix = code_prefix(stock_code) + stock_code
    down_url = '%s?code=%s&start=%s&end=%s&fields=%s' % \
        (url, code_with_prefix, regulate_date(start), regulate_date(end),
         fields)
    res = requests.get(down_url, timeout=60)
    file_name = 'tmp.csv'
    file_size = open(file_name, 'wb').write(res.content)
    # return pd.read_csv(file_name,  index_col=0, encoding='gb2312')
    original_df = pd.read_csv(file_name,  index_col=0,
                              encoding='gb2312').sort_index()
    os.remove(file_name)
    return get_useful_feilds(original_df)
