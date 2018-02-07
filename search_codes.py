import re
import requests

url = 'http://quote.eastmoney.com/stocklist.html'


def get_all_codes(url):
    codes = []
    try:
        r = requests.get(url)
    except Exception as e:
        print(e, ' -- Cannot access %s' % url)
        return None
    r.encoding = 'gbk'
    txt = r.text

    # p = re.compile('<a href="(.*?)">.*?</td>')
    p = re.compile(
        '"http://quote.eastmoney.com/.*?\(([036]\d{5})\)</a>', re.S)
    m = re.finditer(p, txt)
    for x in m:
        codes.append(x.group(1).strip())
    return codes


def save_to_csv(codes):
    csv_file = 'all.csv'
    with open(csv_file, 'w') as f:
        for code in codes:
            f.write(code + '\n')


def main():
    codes = get_all_codes(url)
    # print(codes, len(codes))
    # print(codes[0])
    save_to_csv(codes)

if __name__ == '__main__':
    main()
