import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
# We dont Probably need the Gridlines. Do we? If yes comment this line
sns.set(style="ticks")
player_df = pd.read_csv("../input/data.csv")
numcols = [
'Overall',
'Potential',
'Crossing','Finishing', 'ShortPassing', 'Dribbling','LongPassing', 'BallControl', 'Acceleration',
'SprintSpeed', 'Agility', 'Stamina',
'Value','Wage']
catcols = ['Name','Club','Nationality','Preferred Foot','Position','Body Type']
# Subset the columns
player_df = player_df[numcols+ catcols]
# Few rows of data
player_df.head(5)

def wage_split(x):
try:
return int(x.split("K")[0][1:])
except:
return 0
player_df['Wage'] = player_df['Wage'].apply(lambda x : wage_split(x))
def value_split(x):
try:
if 'M' in x:
return float(x.split("M")[0][1:])
elif 'K' in x:
return float(x.split("K")[0][1:])/1000
except:
return 0
player_df['Value'] = player_df['Value'].apply(lambda x : value_split(x))

corr = player_df.corr()
g = sns.heatmap(corr, vmax=.3, center=0,
square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt='.2f', cmap='coolwarm')
sns.despine()
g.figure.set_size_inches(14,10)
plt.show()

filtered_player_df = player_df[(player_df['Club'].isin(['FC Barcelona', 'Paris Saint-Germain',
'Manchester United', 'Manchester City', 'Chelsea', 'Real Madrid','FC Porto','FC Bayern München'])) &
(player_df['Nationality'].isin(['England', 'Brazil', 'Argentina',
'Brazil', 'Italy','Spain','Germany']))
]
# Single line to create pairplot
g = sns.pairplot(filtered_player_df[['Value','SprintSpeed','Potential','Wage']])
g = sns.pairplot(filtered_player_df[['Value','SprintSpeed','Potential','Wage','Club']],hue = 'Club')
g = sns.swarmplot(y = "Club",x = 'Wage',data = filtered_player_df,size = 7)
# remove the top and right line in graph
sns.despine()
g.figure.set_size_inches(14,10)
plt.show()

g = sns.boxplot(y = "Club",
x = 'Wage',
data = filtered_player_df, whis=np.inf)
g = sns.swarmplot(y = "Club",
x = 'Wage',
data = filtered_player_df,
# Decrease the size of the points to avoid crowding
size = 7,color = 'black')
# remove the top and right line in graph
sns.despine()
g.figure.set_size_inches(12,8)
plt.show()