import util
import config
import stock as s
import json
import tushare as ts
import operator

dict = util.init_dict()
count_stock = {}
count_category = {}

for i in dict:
    print "Query for", i
    try:
        for row in ts.get_hist_data(i, start=config.start, end=config.end).itertuples():
            stock = s.Stock(i, "N/A", row[0], row[1], row[2], row[3], row[4], row[5], row[6], dict)
            if float(stock.p_change) >= config.THRESHOLD:
                if stock.code in count_stock:
                    count_stock[stock.code] = count_stock[stock.code] + 1
                else:
                    count_stock[stock.code] = 1
                print i, count_stock[stock.code]
                for c_name in stock.c_name:
                    if c_name in count_category:
                        count_category[c_name] = count_category[c_name] + 1
                    else:
                        count_category[c_name] = 1
    except:
        pass
sorted_count_stock = sorted(count_stock.items(), key=operator.itemgetter(1), reverse=True)
sorted_count_category = sorted(count_category.items(), key=operator.itemgetter(1), reverse=True)
count_json = json.dumps(sorted_count_stock)
category_json = json.dumps(sorted_count_category).decode("unicode-escape")

print count_json
print category_json




