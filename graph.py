
import pandas as pd
import matplotlib.pyplot as plt
top_loc = pd.read_csv('modified-loc_data.csv')
top_loc.drop('Unnamed: 0',1, inplace=True)
top_ten = top_loc.head(10)

#create bar graphs for top 10 locations 
top_ten.plot(x='Location', y='Members', kind = 'barh')
plt.xlabel('Locations')
plt.ylabel('Number of Members')
plt.title('Members by Top 10 Locations', fontsize=15)

#create bar graphs for top topics 
sum_loc = pd.read_csv('summary_all_locations.csv')
top_sum = sum_loc.head(10)
top_sum.plot(x='Topics', y='Num_Replies', kind = 'barh')
plt.xlabel('Number of Replies')
plt.ylabel('Topics')
plt.title('Popular Topics more than 5 years ago', fontsize=15)