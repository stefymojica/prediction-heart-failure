import pandas as pd

df = pd.read_csv('./heart-failure.csv', sep=',', index_col=False)
print(df)
