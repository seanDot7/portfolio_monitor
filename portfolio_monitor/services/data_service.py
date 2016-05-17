# -*- coding: utf-8 -*-
'''
An interface to get data.
The upper layer should be the controllers and the lower layer should be the interface related to database, files(e.g. csv and excel) and data APIs.
'''
import os
import pandas as pd

def getDataframe(accountId, date):
    filename = 'position_stock.20160512'
    filepath = os.path.join(os.path.dirname(__file__), '../resources/%s.csv' % filename)
    data = None
    if os.path.isfile(filepath):
        try:
            data = pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            data = pd.read_csv(filepath, encoding='gb2312')
        except:
            return None

    return data

def getCsvData(accountId, date):
    data = getDataframe(accountId, date)
    if not data.empty:
        return data.to_json(force_ascii=False, orient='split')
    else:
        return None

def getStats(accountId, date):
    data = getDataframe(accountId, date)
    if not data.empty:
        return {
            'marketValue': data[u'市值'].sum()
        }
    else:
        return None

