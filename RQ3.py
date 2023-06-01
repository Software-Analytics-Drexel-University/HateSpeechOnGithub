import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/dymonmoore/Downloads/replication_package_msr_2022/datasets/sentence_level.csv.csv', header=0)
df

print("Number of civil sentences incorrectly classified:")

# In[1616]:


df_new = df[['quotation_code', 'quotation', 'comment_code']]
civilThreats = []
UncivilAppreciationExcitement = []

print("Uncivil Appreciation and Excitement statements:\n\n")
for row in df_new.itertuples():    
    if "uncivil" in row.comment_code:
        if "Appreciation and Excitement" in row.quotation_code:
            print(row.quotation)


# In[1618]:


print("\n\nCivil Threats statements:\n")
for row in df_new.itertuples():    
    if "civil" in row.comment_code:
        if "Threat" in row.quotation_code:
             print(row.quotation)
            
            
