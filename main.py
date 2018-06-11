import util
import config
import stock as s
import json
import tushare as ts
import operator
import pickle

dict = util.init_dict()
count_stock = {}
count_category = {}
count = 1
list = []
filename = "./data/list"

# filehandler = open(filename, 'r')
# list = pickle.load(filehandler)
# print list

for i in dict:
    print "In progress: ", count, "/", len(dict)
    count += 1
    if count == 20:
        break
    try:
        for row in ts.get_hist_data(i, start=config.START, end=config.END).itertuples():
            stock = s.Stock(i, "N/A", row[0], row[1], row[2], row[3], row[4], row[5], row[6], dict)
            # print row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            list.append(stock)
            if float(stock.p_change) >= config.THRESHOLD:
                if stock.code in count_stock:
                    count_stock[stock.code] = count_stock[stock.code] + 1
                else:
                    count_stock[stock.code] = 1
                for c_name in stock.c_name:
                    if c_name in count_category:
                        count_category[c_name] = count_category[c_name] + 1
                    else:
                        count_category[c_name] = 1
    except:
        pass
filehandler = open("./data/list", 'w')
pickle.dump(list, filehandler)

sorted_count_stock = sorted(count_stock.items(), key=operator.itemgetter(1), reverse=True)
sorted_count_category = sorted(count_category.items(), key=operator.itemgetter(1), reverse=True)
count_json = json.dumps(sorted_count_stock)
category_json = json.dumps(sorted_count_category).decode("unicode-escape")

print count_json
print category_json
