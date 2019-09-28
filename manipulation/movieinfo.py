import pandas as pd
from collections import Counter

df = pd.read_csv('../working_data/movie_with_data_API.csv')
df = df[df.Source == 0]



df2 = df[df['Genre'].notnull()]
df3 = df[df['Released'].notnull()]

genres = df2['Genre'].tolist()
year = df3['Released'].tolist()
years = []
for date in year:
	years.append(date[-2:-1] + '0')

def splitlist(splitter):
	flat = []
	for sublist in splitter:
		for sub in sublist.split(", "):
			flat.append(sub)
	return(Counter(flat))

genres = splitlist(genres)
print(genres.keys())
print(genres.values())

years = Counter(years)
print(years.keys())
print(years.values())




