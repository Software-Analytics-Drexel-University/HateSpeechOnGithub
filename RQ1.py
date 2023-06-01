#!/usr/bin/env python
# coding: utf-8

# In[1603]:


import pandas as pd
import matplotlib.pyplot as plt
##df = pd.read_csv('/Users/dymonmoore/Downloads/replication_package_msr_2022/datasets/sentence_level.csv.csv', header=0)
##df


# In[1604]:

print("The dataset")
df = pd.read_csv('/Users/dymonmoore/Downloads/replication_package_msr_2022/datasets/sentence_level.csv.csv', header=0,
        usecols=["comment_id", "quotation", "quotation_code", 'comment_code', 'sentiment_quotation'])
print(df)


print("Common Phrases or Symbol Analysis")

print("Appreciation & Excitement")

# In[1607]:


count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
otherWords = []

totalCount = 0
for x in df.loc[:,"quotation_code"]:
    print
    if "Appreciation and Excitement" in x:
        totalCount+=1

df_new = df[['quotation_code', 'quotation']]

for row in df_new.itertuples():    
    if "Appreciation and Excitement" in row.quotation_code:    
        if "thanks" in row.quotation: 
            count1 +=1;
        elif "Thanks" in row.quotation: 
            count2 +=1;
        elif "thank you" in row.quotation:
            count3 +=1;
        elif "Thank you" in row.quotation:
            count4 +=1;
        elif "appreciate" in row.quotation:
            count5 +=1;
        elif "!" in row.quotation:
            count6 +=1;
        else:
            #print(row.quotation)
            otherWords.append(row.quotation);
    
    
dict = {'Appreciation & Excitement': ["thanks", "thank you", "Thank you", "appreciate", "Thanks","!"],
        'count': []}

dict['count'].append(count1)
dict['count'].append(count2)
dict['count'].append(count3)
dict['count'].append(count4)
dict['count'].append(count5)
dict['count'].append(count6)

##print({count1, count2, count3, count4 + count5, count6})
sum = count1 + count2 + count3 + count4 + count5 + count6


# scatter plot
plot = pd.DataFrame(dict)
print(plot)
ax = plot.plot(x="Appreciation & Excitement", y="count", kind="bar")


# In[1608]:


precent = sum / totalCount * 100 
print(precent)

otherWordsDf = pd.DataFrame(otherWords)
print("Other Words DataFrame: ")
print(otherWordsDf)

print("Expectation")

# In[1609]:


totalCount = 0
for x in df.loc[:,"quotation_code"]:
    if "Expectation" in x:
        totalCount+=1
print(totalCount)


# In[1610]:


count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
otherWords = []

df_new = df[['quotation_code', 'quotation']]

for row in df_new.itertuples():    
    if "Expectation" in row.quotation_code:    
        if "It would be" in row.quotation: 
            count1 +=1;
        elif "it would be" in row.quotation: 
            count2 +=1;
        elif "I would" in row.quotation: 
            count3 +=1;
        elif "appreciate" in row.quotation: 
            count4 +=1;
        elif "hope" in row.quotation: 
            count5 +=1;
        else:
            otherWords.append(row.quotation);
    
    
dict = {'Expectation': ["it would be", "It would be", "I would", "appreciate", "hope"],
        'count': []}

dict['count'].append(count1)
dict['count'].append(count2)
dict['count'].append(count3)
dict['count'].append(count4)
dict['count'].append(count5)

sum = count1 + count2 + count3 + count4 + count5

# scatter plot
plot = pd.DataFrame(dict)
print(plot)
ax = plot.plot(x="Expectation", y="count", kind="bar")


# In[1611]:


precent = sum / totalCount * 100 
print(precent)

otherWordsDf = pd.DataFrame(otherWords)
print("Other Words DataFrame: ")
print(otherWordsDf)


print("Annoyance and Bitter frustration")

# In[1612]:


totalCount = 0
for x in df.loc[:,"quotation_code"]:
    if "Annoyance and Bitter frustration" in x:
        totalCount+=1
print(totalCount)


# In[1613]:


count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
otherWords = []

df_new = df[['quotation_code', 'quotation']]

for row in df_new.itertuples():    
    if "Annoyance and Bitter frustration" in row.quotation_code:    
        if "I don't" in row.quotation:
            count1+=1
        elif "You" in row.quotation:
            count2+=1
        elif "annoy" in row.quotation:
            count3 +=1
        elif "I have" in row.quotation:
            count4 +=1
        elif "This" in row.quotation:
            count5 +=1
        else:
            otherWords.append(row.quotation);
            
dict = {'Annoyance and Bitter frustration': ["I don't", "You", "annouy", "I have", "This"],
        'count': []}

dict['count'].append(count1)
dict['count'].append(count2)
dict['count'].append(count3)
dict['count'].append(count4)
dict['count'].append(count5)

sum = count1 + count2 + count3 + count4 + count5

# scatter plot
plot = pd.DataFrame(dict)
print(plot)
ax = plot.plot(x="Annoyance and Bitter frustration", y="count", kind="bar")


# In[1614]:


precent = sum / totalCount * 100 
print(precent)

otherWordsDf = pd.DataFrame(otherWords)
print("Other Words DataFrame: ")
print(otherWordsDf)
