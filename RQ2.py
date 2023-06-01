import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/dymonmoore/Downloads/replication_package_msr_2022/datasets/sentence_level.csv.csv', header=0)
df

print("Number of sentences from each sentiment category")

# In[1615]:


dict = {'names':[], 'count':[]}

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0

df_new = df[['quotation_code', 'quotation']]
for row in df_new.itertuples():
    if row.quotation_code not in dict['names']:
        dict['names'].append(row.quotation_code)      

    if "Dissatisfaction" in row.quotation_code:
        count0 +=1
    if "Sadness" in row.quotation_code:
        count1 +=1
    if "Name calling" in row.quotation_code:
        count2 +=1
    if "Mocking" in row.quotation_code:
        count3 +=1
    if "Annoyance and Bitter frustration" in row.quotation_code:
        count4 +=1
    if "Commanding" in row.quotation_code:
        count5 +=1
    if "Vulgarity" in row.quotation_code:
        count6 +=1
    if "Appreciation and Excitement" in row.quotation_code:
        count7 +=1
    if "Considerateness" in row.quotation_code:
        count8 +=1
    if "Sincere apologies" in row.quotation_code:
        count9 +=1
    if "Expectation" in row.quotation_code:
        count10 +=1
    if "Oppression" in row.quotation_code:
        count11 +=1
    if "Humility" in row.quotation_code:
        count12 +=1
    if "Impatience" in row.quotation_code:
        count13 +=1
    if "Criticizing oppression" in row.quotation_code:
        count14 +=1
    if "Confusion" in row.quotation_code:
        count15 +=1
    if "Irony" in row.quotation_code:
        count16 +=1
    if "Threat" in row.quotation_code:
        count17 +=1
    if "Hope to get feedback" in row.quotation_code:
        count18 +=1      
    if "Friendly joke" in row.quotation_code:
        count19 +=1       

dict['count'].append(count0)        
dict['count'].append(count1)
dict['count'].append(count2)
dict['count'].append(count3)
dict['count'].append(count4)
dict['count'].append(count5) 
dict['count'].append(count6)
dict['count'].append(count7)
dict['count'].append(count8)
dict['count'].append(count9)
dict['count'].append(count10)
dict['count'].append(count11)
dict['count'].append(count12)
dict['count'].append(count13)
dict['count'].append(count14)
dict['count'].append(count15)
dict['count'].append(count15)
dict['count'].append(count17)
dict['count'].append(count18)
dict['count'].append(count19)


plot = pd.DataFrame(dict)
print(plot)
