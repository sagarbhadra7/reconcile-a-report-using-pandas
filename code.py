# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)

df['state']=df['state'].str.lower()
df['total']=df['Jan']+df['Feb']+df['Mar']
sum_row=df[['Jan','Feb','Mar','total']].sum()
#sum_row=[sum(df[:]['Jan']),sum(df[:]['Feb']),sum(df[:]['Mar']),sum(df[:]['total'])]
print(sum_row)
#pd.DataFrame(data=sum_row).T
df_final=df.append(sum_row,ignore_index=True)
print(df_final)

# Code ends here


# --------------
import requests 


# Code starts here
url="https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response=requests.get(url)
#print(response)
df1=pd.read_html(response.content)[0]
#df1=response.content
df1=df1[11:]
df1=df1.rename(columns=df1.iloc[0,:]).iloc[1:,:]
df1['United States of America']=df1['United States of America'].str.replace(' ', '')
print(df1)


# Code ends here


# --------------





df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
#print(df1.head())
mapping=df1.set_index('United States of America')['US'].to_dict()
#print(mapping)
print(df1.columns)
#df_final=df1
df_final.insert(loc=6,column='abbr',value='Nan')
df_final['abbr']=df_final['state'].map(mapping)
print(df_final.head())


# Code ends here


# --------------
# Code stars here
import numpy as np
#print(df_final.head())
df_final.loc[(df_final.state=='mississipi'),'abbr']='MS'
#replace(to_replace=np.nan,value='MS',inplace=True)
df_final.loc[(df_final.state=='tenessee'),'abbr']='TN'
#replace(to_replace=np.nan,value='TN',inplace=True)

#df_final
print(df_final.loc[(df_final.state=='mississipi'),'abbr'])
print(df_final.loc[(df_final.state=='tenessee'),'abbr'])
# Code ends here


# --------------
# Code starts here
df_sub=df_final[['abbr','Jan','Feb','Mar','total']].groupby('abbr').sum()
print(df_sub.head())
formatted_df=df_sub.applymap(lambda x: '$'+str(x))
print(formatted_df.head())
# Code ends here


# --------------
# Code starts here
sum_row=pd.DataFrame(df_final[['Jan','Feb','Mar','total']].sum())
#print(type(sum_row))
df_sub_sum=sum_row.T
df_sub_sum=df_sub_sum.applymap(lambda x: '$'+str(x))
final_table=formatted_df.append(df_sub_sum)
print(final_table)


# Code ends here


# --------------
# Code starts here
import matplotlib.pyplot as plt
#print(df_sub)
#df_sub.set_index('abbr')


df_sub['total'].plot.pie(subplots=True, figsize=(6, 6))  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
# Code ends here


