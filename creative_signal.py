import pandas as pd

data_votes = pd.read_parquet('../data/7651fd0b-f222-43b3-8db8-ed6ae660d313')
data_reactions = pd.read_parquet('../data/4ffc86e1-84a4-4fdc-9726-66408e596fef')

print(data_votes.head(5))
print(data_votes.columns)
print(data_votes.shape)

print(data_reactions.head(5))
print(data_reactions.columns)
print(data_reactions.shape)