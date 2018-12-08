#!/usr/bin/env python
# coding: utf-8

# In[16]:


import csv
import sys


# In[17]:


with open('budget_data.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    datalist=list(data)


# In[18]:


print(datalist)


# In[24]:


moneysum = 0
months = 0
monthlychanges = []
previousRevenue = 0


datalist.pop(0)
for entry in datalist:
    months = months + 1
    moneysum = moneysum + int(entry[1])
    monthlychanges.append((entry[0], (int(entry[1]) - previousRevenue)))
    previousRevenue = int(entry[1])
    
sumOfChanges = 0
minimum = monthlychanges[0]
maximum = monthlychanges[0]

for change in monthlychanges:
    sumOfChanges += change[1]
    if change[1] < minimum[1]:
        minimum = change
    if change[1] > maximum[1]:
        maximum = change
    
avgChange = sumOfChanges / months

import sys
sys.stdout = open('log.txt', 'w')
print("Financial analysis")

print("Financial analysis")
print("----------------------------------------")
print("Total Months: "+ str(months))
print("Toal: $" + str(moneysum))
print("The average change in profit is: $" + str(avgChange))
print("The greatest increase in profits is: " + maximum[0]+" ($" + str(maximum[1])+")")
print("The smallest increase in profits is: " + minimum[0]+" ($" + str(minimum[1])+")")


# In[ ]:





# In[ ]:




