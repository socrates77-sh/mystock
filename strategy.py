import pandas as pd
import numpy as np


def average_strategy(analysis_data):
    sd = analysis_data.copy()
    sd['wm'] = np.where(sd['week'] > sd['month'], 1, 0)
    sd['wq'] = np.where(sd['week'] > sd['quarter'], 1, 0)
    sd['wh'] = np.where(sd['week'] > sd['half-year'], 1, 0)
    sd['wy'] = np.where(sd['week'] > sd['year'], 1, 0)

    sd['mq'] = np.where(sd['month'] > sd['quarter'], 1, 0)
    sd['mh'] = np.where(sd['month'] > sd['half-year'], 1, 0)
    sd['my'] = np.where(sd['month'] > sd['year'], 1, 0)

    sd['qh'] = np.where(sd['quarter'] > sd['half-year'], 1, 0)
    sd['qy'] = np.where(sd['quarter'] > sd['year'], 1, 0)

    sd['hy'] = np.where(sd['half-year'] > sd['year'], 1, 0)

    sd['wmq'] = np.where(sd['wm'] * sd['mq'] == 1, 1, 0)
    sd['wmqh'] = np.where(sd['wm'] * sd['mq'] * sd['qh'] == 1, 1, 0)
    sd['wmqhy'] = np.where(sd['wm'] * sd['mq'] *
                           sd['qh'] * sd['hy'] == 1, 1, 0)

    sd['mqh'] = np.where(sd['mq'] * sd['qh'] == 1, 1, 0)
    sd['mqhy'] = np.where(sd['mq'] * sd['qh'] * sd['hy'] == 1, 1, 0)

    sd['qhy'] = np.where(sd['qh'] * sd['hy'] == 1, 1, 0)

    return sd
