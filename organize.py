import csv
import re
import time
import pandas as pd 

with open('loc_data.csv', 'r') as f2:
    data = f2.read()
    new_data = data.splitlines()
    loc_lst = []
    num_disc_lst = []

for i in range(0, 51):
    element = new_data[i].split(',')[0].replace(' ', '-').lower()
    loc_lst.append(element)
    element2 = new_data[i].split(',')[2]
    num_disc_lst.append(element2)

for i in range(0, 51):
    file1 = open('%s.csv'%(loc_lst[i]), "r") 
    temp = file1.readlines()
    col1 = []
    col2 = []
    for j in temp:
        j = j.strip()
        element1 = j.split(',')[0:-1]
        str1 = ''.join(element1)
        element2 = int(j.split(',')[-1])
        col1.append(str1)
        col2.append(element2)
   
    df = pd.DataFrame({'Topic':col1, 'Replies':col2})
    sorted_df = df.sort_values(by=['Replies'], ascending=False)

#     for i in range(0,2):
    file2 = open('modified-%s.csv' %(loc_lst[i]), "a")
    sorted_df.to_csv(file2, header=True)
    file2.close()


### Organize the information by time (most recent) and the number of replies (ascending)
with open('all_locations.csv', 'r') as f2:
    data = f2.read()
    new_data = data.splitlines()
    topic_lst = []
    num_disc_lst = []
    time_lst = []

    file1 = open('all_locations.csv', "r") 
    temp = file1.readlines()
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    for j in temp:
        j = j.strip()
        element1 = j.split(',')[0:1] #title of the post (topic)
        str1 = ''.join(element1)
        element2 = int(j.split(',')[1]) #number of replies per post

        #last update on the post (ie. the last reply to the corresponding post)
        element3 = j.split(',')[-1].replace('Last updated ', "")
        element3 = element3.split(" ago - ", 1)[0]
        element3_day = int(element3.split(' ')[0]) 
        element3_unit = element3.split(' ')[-1] #time of last update: minutes, hours, weeks, months, years
        col1.append(str1)
        col2.append(element2)
        col3.append(element3_day)
        col4.append(element3_unit)
   #sort the data from most recent to the oldest and then the number of replies per post 
    df = pd.DataFrame({'Topic':col1, 'Num_Replies':col2, 'Last Update':col3, 'Unit':col4})
    sorted_df = df.sort_values(by=['Unit', 'Last Update', 'Num_Replies'], ascending=True)

    file2 = open('modified_all_locations.csv', "a")
    sorted_df.to_csv(file2, header=True)
    file2.close()