import pandas as pd

df = pd.read_csv('../working_data/ticket_type_by_movie.csv')

events = {'Event': df.EventName.unique()}

df2 = pd.DataFrame(events)
df2 = df2.sort_values(by=['Event'])
df2 = df2.set_index('Event')

for index, row in df.iterrows():
	idx = df2.index.get_loc(row['EventName'])
	ticket_type = row['TicketType']
	ticket_q  = row['Quantity']
	df2.ix[idx, ticket_type] = ticket_q
df2 = df2.fillna(0)
df2.to_csv('demographics.csv')