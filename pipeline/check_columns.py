import pandas as pd
df = pd.read_csv('final_adaptation_dataset.csv')
print("These are the columns present in your CSV:")
print(df.columns.tolist())
