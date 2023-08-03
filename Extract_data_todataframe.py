'''
Written by: Jinsha Babu George
Aim: To extract log files, clean it and load it as dataframe and save csv
'''
#Import library funtions
import os
import pandas as pd


#Defining variables
filepath = r"C:\Users\jinsh\Documents\Eclipse Projects\ETLAssignment_BusinessIntelligence\W3SVC1"
file_names=os.listdir(filepath)
columns = ["date", 
"time",
"s-ip", 
"cs-method", 
"cs-uri-stem", 
"cs-uri-query",
"s-port",
"cs-username", 
"c-ip", 
"cs(User-Agent)",
"sc-status",
"sc-substatus", 
"sc-win32-status",
"time-taken"]

data =[]
for i in file_names:
    if (i[-4:]== ".log"):
        for line in open(filepath+"\\" +i):
            li=line.strip()
            if not (li.startswith("#") or li.startswith("/")) :
                details = line.split(" ")
                details = [x.strip() for x in details]
                structure = {key:value for key, value in zip(columns, details)}
                data.append(structure)
            
    df = pd.DataFrame(data)
    replace_dict = {'-':''}
    df["cs-uri-query"] = df["cs-uri-query"].map(replace_dict)
    df["cs-username"] = df["cs-username"].map(replace_dict)
    df["cs(User-Agent)"] = df["cs(User-Agent)"].map(replace_dict)
    df.to_csv('new.csv',header=True)




        