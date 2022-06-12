import pandas as pd

ds0 = pd.read_csv('./data/daily_sales_data_0.csv')
ds1 = pd.read_csv('./data/daily_sales_data_1.csv')
ds2 = pd.read_csv('./data/daily_sales_data_2.csv')

ds = pd.concat([ds0, ds1, ds2], ignore_index=True)

ds.drop(ds[ds['product'] != "pink morsel"].index, inplace=True)

ds['price'] = ds['price'].str.split('$')[1][1]

ds['sales'] = ds['price'].astype('float') * ds['quantity'].astype('int')

ds.drop(['price', 'quantity', 'product'], axis=1, inplace=True)

ds.to_csv('data/output.csv', index=False)