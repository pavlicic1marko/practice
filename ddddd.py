#git practice
import pandas as pd
pd.core.common.is_list_like= pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from scipy.stats import pearsonr

stock1=input("enter stock symbol(example: AMZN)")
stock2=input("enter stock symbol(example: AAPL)")
stock_symbol_list=[stock1,stock2]
time1=[int(x) for x in input("enter the start time: year moth date(example: 2008 6 1)",).split()]
time2=[int(x) for x in input("enter the end time: year moth date(example: 2009 3 31)",).split()]
start_date=datetime.datetime(*time1)
end_date=datetime.datetime(*time2)

def get_price_history(stock_symbol,start_date,end_date):
    dff = web.DataReader(stock_symbol, 'quandl', start_date, end_date)
    dff.reset_index(inplace=True)
    dff.set_index("Date", inplace=True)
    dff["of_first_value"]=dff["AdjClose"]/dff.iloc[-1]["AdjClose"]*100
    return dff

object1=[]
for stock in stock_symbol_list:
    object1.append(get_price_history(stock,start_date,end_date))

plt.plot(object1[0].index, object1[0].of_first_value, label=stock_symbol_list[0])
plt.plot(object1[1].index, object1[1].of_first_value, label=stock_symbol_list[1])
plt.ylabel("% of starting value")
plt.xlabel("vreme")
plt.title("promena")
plt.legend()
plt.xticks(rotation='30')


x1,x2=pearsonr(list(object1[0].AdjClose),list(object1[1].AdjClose))
print("Pearson's correlation coefficient for",stock_symbol_list[0],"and",stock_symbol_list[1],  "is",x1 ,",and the 2-tailed p-value is", x2 )
plt.show()

from sqlalchemy import create_engine

engine5 = create_engine('sqlite:///newstocks.db')
table_name1=stock1+str(time1[0])
table_name2=stock2+str(time2[0])
object1[0][["AdjClose","of_first_value","Volume"]].to_sql(
    name=table_name1,
    con=engine5,
    index=True,
)
object1[1][["AdjClose","of_first_value","Volume"]].to_sql(
    name=table_name2,
    con=engine5,
    index=True,
)

df1 = pd.read_sql_query('select min(of_first_value),Date from '+table_name1,engine5)
df2 = pd.read_sql_query('select min(of_first_value),Date from '+table_name2,engine5)

print("the minimum value for {} was {}% of its starting valueand it was reached on {}".format(stock1,round(list(df1.iloc[0])[0],2),list(df1.iloc[0])[1].split()[0]))
print("the minimum value for {} was {}% of its starting valueand it was reached on {}".format(stock2,round(list(df2.iloc[0])[0],2),list(df2.iloc[0])[1].split()[0]))
