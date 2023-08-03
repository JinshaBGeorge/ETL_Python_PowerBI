'''
Written by: Jinsha Babu George
Aim: To extract file and tile type fields
'''

import pandas as pd
import numpy as np

df = pd.read_csv("new.csv", low_memory = False)
file_list = df["cs-uri-stem"].unique().tolist()

files_dict_list =[]
for filename in file_list:
    file_type = filename.split(".")
    if(len(file_type)>1):
        filetype = "."+file_type[len(file_type)-1]
    else:
        filetype = "."
    files = [filename,filetype]
    files_dict_list.append(files)

fn_ft_df = pd.DataFrame(files_dict_list, columns=["FileName","FileType"])
fn_ft_df = fn_ft_df.drop_duplicates(ignore_index= True)
fn_ft_df['FileID'] = np.arange(len(fn_ft_df))
fn_ft_df = fn_ft_df[["FileID","FileName","FileType"]]
print(fn_ft_df)
fn_ft_df.to_csv("Dimension2_File.csv",header = True)