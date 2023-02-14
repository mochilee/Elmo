# basic
# numpy as np
#import pandas as pd
# get data
import pandas_datareader as pdr
# visual
import matplotlib.pyplot as plt
#import mplfinance as mpf
from scipy.stats import linregress
#import seaborn as sns
#time
import datetime as datetime
from stock_package import xlstest as xls
#import xlstest as xls
def stock_data(stock_id,start,end = 0):
    start_time = datetime.datetime.strptime( str(start) , '%Y%m%d' ) 
    print(stock_id)
    print(start_time)
    print(end)
    if end == 0:     
        try:
            stock = f'{stock_id}.TW'
            df_n = pdr.DataReader(stock, 'yahoo', start=start_time)
            df_n = df_n.reset_index()
            print("test1")
        except:
            stock = f'{stock_id}.TWO'
            df_n = pdr.DataReader(stock, 'yahoo', start=start_time)
            df_n = df_n.reset_index()
            print("test2")
    else:
        try:
            stock = f'{stock_id}.TW'
            end_time = datetime.datetime.strptime( str(end) , '%Y%m%d' )
            df_n = pdr.DataReader(stock, 'yahoo', start=start_time,end = end_time)
            df_n = df_n.reset_index()
            print("test3")
        except:
            stock = f'{stock_id}.TWO'
            end_time = datetime.datetime.strptime( str(end) , '%Y%m%d' )
            df_n = pdr.DataReader(stock, 'yahoo', start=start_time,end = end_time)
            df_n = df_n.reset_index()
            print("test4")
    print(df_n)
    return df_n

def line(df_n,stock_id):
    stock_name = xls.stock_search(stock_id)
    print(stock_id)
    print(df_n)
    reg_up = linregress(x = df_n.index,y = df_n.Close)
    up_line = reg_up[1] + reg_up[0] * df_n.index
    df_uptemp = df_n[df_n["Close"] < up_line]
    df_uptemp.head()
    
    while len(df_uptemp) >= 2 :
        reg = linregress(x = df_uptemp.index,y = df_uptemp.Close)
        up_line = reg[1] + reg[0] * df_n.index
        df_uptemp = df_n[df_n["Close"] < up_line]
    df_n["low_Trend"] = reg[1] + reg[0] * df_n.index    
    df_downtemp = df_n[df_n["Close"] > up_line]
    df_downtemp.head()
    while len(df_downtemp) >= 2 :
        reg = linregress(x = df_downtemp.index,y = df_downtemp.Close)
        up_line = reg[1] + reg[0] * df_n.index
        df_downtemp = df_n[df_n["Close"] > up_line]
    df_n["Up_Trend"] = reg[1] + reg[0] * df_n.index
    df_n.Close.plot()
    plt.plot(df_n.low_Trend,color=(255/255,100/255,100/255))
    plt.plot(df_n.Up_Trend,color=(100/255,100/255,255/255))
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.title(f"{stock_id}  {stock_name}",fontsize=20)
    #plt.title(f"{stock_id}",fontsize=20)
    plt.legend(['收盤價','上升趨勢線','下降趨勢線'])
    plt.savefig("stock.png")
    plt.clf()
    
if __name__ == "__main__":
    df_n = stock_data('2330',"20211001","20211121")
    temp = line(df_n,'2330')


