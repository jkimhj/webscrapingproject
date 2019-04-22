import csv
import re
import time
import pandas as pd 
#Organize collected data of all locations 
with open('loc_data.csv', 'r') as f2:
    data = f2.read()
    new_data = data.splitlines()
    loc_lst = [] #locations list
    num_members = [] #number of members per location 
    num_disc_lst = [] #number of discussions per location 

for i in range(0, 51):
    element1 = new_data[i].split(',')[0].replace(' ', '-').lower() #location 
    loc_lst.append(element1)

    element2 = new_data[i].split(',')[1] #Number of members (if contains 'K', change to integers)
    if element2[-1]=='K':
        element2 = element2.replace('K', '')
        element2 = float(element2) * 1000
    else:
        element2 = float(element2)
    num_members.append(element2)

    element3 = new_data[i].split(',')[2]
    num_disc_lst.append(element3)

df = pd.DataFrame({'Location':loc_lst, 'Members':num_members, 'Num_Topics':num_disc_lst})
sorted_df = df.sort_values(by=['Members'], ascending=False)

file2 = open('modified-loc_data.csv' , "a")
sorted_df.to_csv(file2, header=True)
file2.close()