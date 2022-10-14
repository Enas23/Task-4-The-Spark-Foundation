#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[3]:


df=pd.read_csv('D:/The Spark foundation/Tourism.csv',encoding='Latin-1')


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


#to show all coloumns
pd.set_option('display.max_rows',None)
df.dtypes


# In[8]:


df.isnull().sum()


# In[9]:


df.nunique()


# In[10]:


df.describe()


# In[11]:


df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','provstate':'states','region_txt':'Region','country_txt': 'Country',
                      'attacktype1_txt':'AttackType','nkill':'Killed','target1':'Target','nwound':'Wounded','gname':'GroupName',
                      'targtype1_txt':'Target_type','weaptype1_txt':'Weapontype','motive':'Motive'},inplace =True)


# In[12]:


df.head(5)


# In[13]:


dataf =df[['Year','Month','Day','Country','states','city','Region','AttackType','latitude','longitude','Killed','Wounded','Target','summary',
             'GroupName','Target_type','Weapontype','Motive']]
dataf.head(5)


# In[14]:


dataf.shape


# In[23]:


dataf.isnull().sum()


# In[15]:


count = 0
for i in dataf['Day']:
  if i==0:
    count+=1
  else:
    count=count
print("Total Number Of Days Entred as 0 :",count)


# In[16]:


count2 = 0
for i in dataf['Month']:
  if i==0:
    count2+=1
  else:
    count=count
print("Total Number Of Days Entred as 0 :",count2)


# In[17]:


dataf['Day']= dataf['Day'].apply(lambda x: np.random.randint(1,32) if x == 0 else x)
dataf['Month'] = dataf['Month'].apply(lambda x: np.random.randint(1,13) if x == 0 else x)


# In[18]:


count = 0
for i in dataf['Day']:
  if i==0:
    count+=1
  else:
    count=count
print("Total Number Of Days Entred as 0 :",count)


# In[19]:


count2 = 0
for i in dataf['Month']:
  if i==0:
    count2+=1
  else:
    count=count
print("Total Number Of Days Entred as 0 :",count2)


# In[20]:


def null_val(dataf):
    null_val = dataf.isnull().sum()
    null_val_p = 100 * dataf.isnull().sum()/len(dataf)
    null_val_ = pd.concat([null_val, null_val_p], axis =1)
    null_val_last = null_val_.rename(columns={0:'Null Values',1:'Percentage'})
    return null_val_last
null_val(dataf)


# In[21]:


dataf.isnull().sum()


# In[22]:


dataf['Motive'].fillna(value='NA',inplace=True)
dataf['summary'].fillna(value='NA',inplace=True)
dataf['city'].fillna(value='NA',inplace=True)
dataf['states'].fillna(value='NA',inplace=True)
dataf['longitude'].fillna(value='NA',inplace=True)
dataf['latitude'].fillna(value='NA',inplace=True)
dataf['Wounded'].fillna(value='NA',inplace=True)
dataf['Killed'].fillna(value='NA',inplace=True)
dataf['Target'].fillna(value='NA',inplace =True)


# In[23]:


dataf.isnull().sum()


# In[24]:


style ={'family':'Times New Roman','color':'black', 'size': 15}
dict = {'AttackType':1,'Target_type':2,'Region':3,'Weapontype':4}
plt.figure(figsize=(10,40))

for value, i in dict.items():
  plt.subplot(4,1,i)
  sns.boxplot(x="Year",y=value, data=dataf, whis=[0,100],palette="YlGnBu")
  plt.title(value,fontdict=style)
plt.show()


# In[26]:


plt.figure(figsize=(10,7))
sns.heatmap(dataf.corr(),cmap="GnBu",annot = True, xticklabels ='auto', yticklabels='auto',linewidth=0.8)


# In[27]:


plt.subplots(figsize=(15,6))
sns.countplot('Year',data=dataf,palette="Reds")
plt.xticks(rotation=50)
plt.xlabel('Years',size='18',color='black')
plt.ylabel('Terrorism Activities',size ='18',color = 'black')
plt.title('Track Number of Terrorist Activities as Year',size = '20',color = 'black')
plt.show()


# In[28]:


pd.crosstab(dataf.Year, dataf.Region).plot(kind='area',figsize=(15,6))
plt.title('Terrorist Activities as Per Region',size = '20',color = 'black')
plt.xlabel('Years',size='18',color='black')
plt.ylabel('Number of Attacks',size ='18',color = 'black')
plt.show()


# In[29]:


plt.subplots(figsize=(18,6))
plt.title('Top 10 Countries affected by Terro Attacks',size = '25', color='black')
sns.barplot(dataf['Country'].value_counts()[:10].index, dataf['Country'].value_counts()[:10].values,palette="Paired")
plt.xlabel('Countries',size ='20',color ='blue')
plt.ylabel('Attack Rate',size ='20',color ='blue')
plt.show()


# In[ ]:





# In[31]:


print("Country with the Most Terrorist Attacks:",dataf['Country'].value_counts().idxmax())
print("Region with the Most Terrorist Attacks:",dataf['Region'].value_counts().idxmax())
print("City Have the Most Terrorist Attacks:",dataf['city'].value_counts().index[1])
print("Year with the Most Terrorist Attacks:",dataf['Year'].value_counts().idxmax())
print("Month with the Most Terrorist Attacks:",dataf['Month'].value_counts().idxmax())
print("Group with the Most Terrorist Attacks:",dataf['GroupName'].value_counts().index[1])
print("Most Target Types:",dataf['AttackType'].value_counts().index[1])
print("Most Target Types:",dataf['Target_type'].value_counts().idxmax())


# In[ ]:




