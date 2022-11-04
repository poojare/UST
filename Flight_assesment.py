#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')


# In[5]:


import pandas as pd


# In[63]:


get_ipython().system('pip install numpy')


# In[15]:


get_ipython().system('pip install pymongo')
        


# In[67]:


#a)Create collections “flights” inside database “airline_delayDB”

from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns


def mongoimport(csv_path):
        flight_df = pd.read_csv(csv_path)
        payload = json.loads(flight_df.to_json(orient = 'records'))
        collection.delete_many({})
        collection.insert_many(payload)
        
    
if __name__ =="__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client['airline_delayDB']
    collection = db['flights']
    
    mongoimport('E:/USTpython/pymongo1/Flights_Delay.csv')


# In[75]:


#b) Average arrival dealy caused by airlines

a=collection.aggregate([{'$group':{'_id':'null','averagedealy':{'$avg':'$ARRIVAL_DELAY'}}},{'$project':{'_id':0}}])
for item in a:
    print(item)


# In[86]:


#c)Days of months with respect to average of arrival delay
a=collection.aggregate([{'$group':{'_id':'$MONTH','averagedealy':{'$avg':'$ARRIVAL_DELAY'}}}])

df=pd.DataFrame(a)
display(df)
plt.bar(df['_id'], df['averagedealy'],color="green")
plt.xlabel('Month')
plt.ylabel('Averagedelay')
plt.show()



# In[92]:


#d)  Arrange weekdays with respect to average of arrival delay  
a=collection.aggregate([{'$group':{'_id':'$DAY_OF_WEEK','averagedealy':{'$avg':'$ARRIVAL_DELAY'}}}])
df=pd.DataFrame(a)
display(df)
plt.bar(df['_id'],df['averagedealy'],color='pink')
plt.title('Weekdays v/s average of arrival delays')
plt.xlabel('Day_of_week')
plt.ylabel('Avg Arrival delay')
plt.show()


# In[93]:


#e)Arrange Days of month as per cancellation done in descending order
allDocuments = collection.aggregate([{'$match':{'DAY':1}},{'$group':{'_id':'$CANCELLED','totalcount':{'$count':{}}}},{'$sort':{'totalcount':-1}}])
for item in allDocuments:
              print(item)
         


# In[95]:


#f)Find the busiest airports with respect to day of week
allDocuments = collection.aggregate([{'$match':{'DAY_OF_WEEK':2}},{'$group':{'_id':'null','busiestairport':{'$max':'$ORIGIN_AIRPORT'}}},{'$project':{'_id':0}}])
for item in allDocuments:
   print(item)
        


# In[113]:


#g)Find top 10 airlines of us
allDocuments = collection.aggregate([{'$match':{'AIRLINE':"US"}},{'$sort':{'AIRLINE':-1}},{'$limit':10}])
for item in allDocuments:
    print(item)


# In[114]:


#h)Finding airlines that make the maximum, minimum number of cancellations.
allDocuments = collection.aggregate([{'$group':{'_id':'null','maxcancel':{'$max':'$CANCELLED'},'mincancel':{'$min':'$CANCELLED'}}},{'$project':{'_id':0}}])
for item in allDocuments:
    print(item)


# In[117]:


#i)Find and show airlines names in descending that make the most number of diversions made         
s = collection.aggregate([{'$match':{'DIVERTED':1}},{'$group':{'_id':'$AIRLINE','totalcount':{'$count':{}}}},{'$sort':{'totalcount':-1}}])
for item in s:
    print(item)
    


# In[119]:


#j)Finding days of month that see the most number of diversion
d = collection.aggregate([{'$group':{'_id':'$MONTH','Diviton':{'$sum':'$DIVERTED'}}},{'$sort':{'Diviton':-1}},{'$limit':1}])
for item in d:
    print(item)


# In[120]:


#k)Calculating mean and standard deviation of departure delay for all flights in minutes
e = collection.aggregate([{'$group':{'_id':'null', 'depardelay':{'$stdDevSamp':'$DEPARTURE_DELAY'}}}])
for item in e:
    print(item)


# In[121]:


#l)Calculating mean and standard deviation of arrival delay for all flights in minutes
f = collection.aggregate([{'$group':{'_id':'null', 'arrivaldelay':{'$stdDevSamp':'$ARRIVAL_DELAY'}}}])
for item in f:
    print(item)


# In[ ]:




