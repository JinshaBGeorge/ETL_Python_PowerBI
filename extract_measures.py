'''
Written by: Jinsha Babu George
Aim: To extract page related facts
'''


import pandas as pd

df = pd.read_csv("new.csv",low_memory = False)

measure_df = df[["date","time","c-ip","cs-uri-stem","cs-method","sc-status","time-taken"]]
measure_df = measure_df.rename({"date":"Date","time":"Time","c-ip":"UserIP","cs-uri-stem":"FileName" , "cs-method":"FileRequestType", "sc-status":"PageStatus","time-taken":"ProcessingTime"}, axis = "columns")
measure_df = measure_df.drop_duplicates()
print(measure_df)

measure_df.to_csv("measure1_denormalized.csv",header = True)