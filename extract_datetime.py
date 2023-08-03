'''
Written by: Jinsha Babu George
Aim: To extract date and time fields
'''

import pandas as pd
import numpy as np

df = pd.read_csv("new.csv", low_memory = False)
datetime_df = df[["date","time"]]
datetime_df = datetime_df.drop_duplicates()
datetime_df['DateID'] = np.arange(len(datetime_df))
datetime_df = datetime_df[["DateID","date","time"]]
print(datetime_df)
datetime_df.to_csv("Dimension3_date.csv")
