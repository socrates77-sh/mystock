import pandas as pd
import numpy as np

avg_strategys = ['wm', 'wq', 'wh', 'wy', 'mq', 'mh', 'my', 'qh', 'qy', 'hy',
                 'wmq', 'wmqh', 'wmqhy', 'mqh', 'mqhy', 'qhy']


def gain_by_strategy(strategy_data, stategy, days=0):
    sd = strategy_data.copy()
    sd['gain'] = np.where(sd[stategy] == 0, 1, sd['变动率']).cumprod()
    if days == 0:
        return sd['gain'][-1]
    else:
        return sd['gain'][-1] / sd['gain'][-days]


def get_all_gain(strategy_data):
    gain_result = pd.DataFrame(index=avg_strategys,
                               columns=['all', '500d', '250d'])

    for ast in avg_strategys:
        gain_result['all'][ast] = gain_by_strategy(strategy_data, ast, 0)
        gain_result['500d'][ast] = gain_by_strategy(strategy_data, ast, 500)
        gain_result['250d'][ast] = gain_by_strategy(strategy_data, ast, 250)

    return gain_result
