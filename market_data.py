import requests
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

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


def stock_data_reader(stock_code, start='19000000', end='20171231'):
    url = 'http://quotes.money.163.com/service/chddata.html'
    fields = 'TCLOSE;PCHG'
    code_with_prefix = code_prefix(stock_code) + stock_code
    down_url = '%s?code=%s&start=%s&end=%s&fields=%s' % \
        (url, code_with_prefix, regulate_date(start), regulate_date(end),
         fields)
    res = requests.get(down_url, timeout=60)
    file_name = '%s.csv' % stock_code
    file_size = open(file_name, 'wb').write(res.content)
    # return pd.read_csv(file_name,  index_col=0, encoding='gb2312')
    return pd.read_csv(file_name,  index_col=0, encoding='gb2312').sort_index()


def main():
    code = '002253'
    code = '600708'
    start = '1998/5/5'
    end = '2018/1/20'
    print(stock_data_reader(code, start, end))


if __name__ == '__main__':
    main()
