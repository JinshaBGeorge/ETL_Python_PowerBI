'''
Written by: Jinsha Babu George
Aim: To extract client browser and OS using httpagentparser library
'''


import pandas as pd
import numpy as np
import httpagentparser

df = pd.read_csv("new.csv", low_memory = False)
ip_out_df = pd.read_csv("Dimension1_UserIP.csv", low_memory = False)

op_list =[]
ip_ua_df = df[["c-ip","cs(User-Agent)"]]
ip_ua_df = ip_ua_df.drop_duplicates()

list1 = []
for s in ip_ua_df["cs(User-Agent)"]:
    tup = httpagentparser.simple_detect(s)
    l = list(tup)
    l.append(s)
    os_dict = {"OS":l[0],"Browser":l[1],"cs(User-Agent)": l[2]}
    list1.append(os_dict)

os_br_df = pd.DataFrame(list1)

ip_os_br_df = ip_ua_df.merge(os_br_df[['OS','Browser','cs(User-Agent)']])
ip_os_br_df = ip_os_br_df.drop_duplicates()


ip_list3 = ip_os_br_df['c-ip'].unique().tolist()

value1 = ip_os_br_df["OS"]
OS = {key:value for key,value in zip(ip_list3,value1)}
ip_out_df['OS'] = ip_out_df['IPv4'].map(OS)

value2 = ip_os_br_df["Browser"]
browser = {key:value for key,value in zip(ip_list3,value2)}
ip_out_df['browser'] = ip_out_df['IPv4'].map(browser)

print(ip_out_df.columns)
ip_out_df1 = ip_out_df[['IPv4','country_code','country_name',
       'state', 'city', 'postal', 'latitude', 'longitude', 'webcrawlers', 'OS',
       'browser']]
ip_out_df1 = ip_out_df1.drop_duplicates(ignore_index = True)
ip_out_df1['UserID'] = np.arange(len(ip_out_df1))
ip_out_df1 = ip_out_df1[['UserID','IPv4','country_code','country_name',
       'state', 'city', 'postal', 'latitude', 'longitude', 'webcrawlers', 'OS',
       'browser']]
print(ip_out_df1)
ip_out_df1.to_csv('Dimension1_UserIP.csv',header=True)