import time

from Crawler.crawler_tushare import CrawlStockData

if __name__ == '__main__':
    t1 = time.time()
    # Initiate
    Obj = CrawlStockData(IP="localhost", PORT=27017)
    # Get basic infos of stocks
    Obj.getStockBasicFromTushare("Stock", "Basic_Info")
    # Extract stocks' code
    Code = Obj.extractData('Stock', 'Basic_Info', ['code'])[0]
    # Get stock price from Tushare
    for stock_code in Code:
        Obj.getStockDayHistory('Stock', stock_code)
        print(' [*] ' + stock_code + ' has finished storing ... ')
    t2 = time.time()
    print(' running time:', t2 - t1)
