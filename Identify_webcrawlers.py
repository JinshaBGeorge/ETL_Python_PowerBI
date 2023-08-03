'''
Written by: Jinsha Babu George
Aim: To identify the ip of bots
'''


import pandas as pd


df = pd.read_csv("new.csv", low_memory = False)
ip_out_df = pd.read_csv("Dimension1_UserIP.csv", low_memory = False)

robots_df = df[df["cs-uri-stem"].str.contains("/robots.txt", regex = False)]
ip_list2 = robots_df['c-ip'].unique().tolist()
value = "Y"
webcrawlers = {key:value for key in ip_list2}
ip_out_df['webcrawlers'] = ip_out_df['IPv4'].map(webcrawlers)

print(ip_out_df)
ip_out_df.to_csv('Dimension1_UserIP.csv',header=True)
