import tushare as ts
import json

def init_dict():
    df1 = ts.get_concept_classified()
    dict = {}
    for row in df1.itertuples():
        key = str(row[1])
        if key in dict:
            dict[key].append(row[3])
        else:
            dict[key] = []
    # print json.dumps(dict).decode("unicode-escape")
    return dict

def init():
    pass

