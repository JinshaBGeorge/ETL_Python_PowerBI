'''
Written by: Jinsha Babu George
Aim: To convert ip address to location details via online database
'''

import requests
import pandas as pd
import json

df = pd.read_csv("new.csv", low_memory = False)
url = 'https://geolocation-db.com/jsonp/'
ip_list = df["c-ip"].unique().tolist()
ip_out_list = [] 
for ip in range(0,len(ip_list)):
    resp = requests.get(url + str(ip_list[ip]))
    result = resp.content.decode()
    result = result.split("(")[1].strip(")")
    result = json.loads(result)
    ip_out_list.append(result)

ip_out_df = pd.DataFrame(ip_out_list,columns = ['IPv4','country_code','country_name','state','city','postal','latitude','longitude'])
ip_out_df = ip_out_df.drop_duplicates(ignore_index = True)
print(ip_out_df)
ip_out_df.to_csv('Dimension1_UserIP.csv',header=True)


    
    