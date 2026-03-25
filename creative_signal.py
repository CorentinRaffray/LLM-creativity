import pandas as pd

data_votes = pd.read_parquet('../data/7651fd0b-f222-43b3-8db8-ed6ae660d313')

print(data_votes.head(5))
print(data_votes.columns)
print(data_votes.shape)