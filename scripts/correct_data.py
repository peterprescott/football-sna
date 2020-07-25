import pandas as pd

# Correct data for De Bruyne's goal vs Chelsea (not an inaccurate pass!)

england_events = pd.read_csv('../data/processed/England.csv')

england_events.at[102730,'eventName'] = 'Shot'
england_events.at[102730,'subEventName'] = 'Goal'
england_events.at[102730,'accurate'] = 1
england_events.at[102730,'to_team'] = 'Away Goal'
england_events.at[102730,'target'] = 'Goal'
england_events.at[102730,'target_y'] = 50

england_events.to_csv('../data/processed/England.csv',index=False)
