import pandas as pd
# s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
# print(s)
# data ={'a':10 ,'b':20 , 'c':30}
# print(pd.Series(data))
# Data FRAME
data ={ 
    "Food item" :["litti chokha"," samosa","jalebi","kachori"],
    "price(Rs)":[30,10,20,25],
    "Sold_quantity":[50,100,150,180]
}
print(pd.DataFrame(data))