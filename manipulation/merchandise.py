import pandas as pd

df = pd.read_csv('../datasets/merchandise_sales.csv', parse_dates=['Order Date'])
df2 = pd.read_csv('../working_data/tickets_by_movie.csv', parse_dates=['EventDate'])
df2 = df2.loc[~df2.EventDate.duplicated(keep='first')]
df2 = df2.sort_values(by=['EventDate'])
df2 = df2.set_index('EventDate')
df['Price_Num'] = df['Price'].replace('[^.0-9]', '', regex=True).astype(float)

df = df[df['Price Type'] != 'Series Pass']

df2['Merchandise_Sales'] = 0

for index, row in df.iterrows():
	idx = df2.index.get_loc(row['Order Date'], method='nearest')
	new_price = df2.iloc[idx]['Merchandise_Sales'] + row['Price_Num']
	df2.ix[idx, 'Merchandise_Sales'] = new_price


df = pd.read_csv('../datasets/ConcessionsSales_Anonymized.csv', parse_dates=['Order Date'])
df['Price_Num'] = df['Price'].replace('[^.0-9]', '', regex=True).astype(float)

df = df[df['Price Type'] != 'Series Pass']

df2['Concession_Sales'] = 0

for index, row in df.iterrows():
	idx = df2.index.get_loc(row['Order Date'], method='nearest')
	new_price = df2.iloc[idx]['Concession_Sales'] + row['Price_Num']
	df2.ix[idx, 'Concession_Sales'] = new_price



df2.to_csv('testststa.csv')
