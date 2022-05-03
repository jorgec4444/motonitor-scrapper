import pandas as pd

df = pd.read_csv('motoDatasetFinal.csv')

dict = {}
for index, row in df.iterrows():
  b = row['Brand']
  m = row['Model']
  if (b in dict):
    dict.get(b).add(m)
  else:
    dict[b] = {m}

for key, value in dict.items():
  dict[key] = list(sorted(value))
print(dict)