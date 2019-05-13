import pandas as pd 
# from random import *
import os
import pyphen

BABYNAMEFILE = r'./temp/baby.csv'

dirname = os.getcwd()
filename = os.path.join(dirname, BABYNAMEFILE)
print (filename)

mybaby = pd.read_csv(filename, names=['Name', 'Sex', 'Frequency'])

mybaby['Sex'] = mybaby['Sex'].astype('category')
mybaby.dtypes

# REMOVE DUPLICATES 
mybaby.shape


# mybaby = pd.read_csv('./data/yob2016.txt', names=['Name', 'Sex', 'Frequency'])

# # sorting by first name 
mybaby.sort_values("Name", inplace = True) 
  
# # dropping ALL duplicte values keep only first
mybaby.drop_duplicates(subset ="Name", keep = "first", inplace = True)
mybaby.shape
mybaby.dtypes


# ###############  SAVING TO FILE    ############

# save as paraquet (smallest size)
mybaby.to_parquet('./mybaby.paraquet', engine='pyarrow')

# # save as pickle 
# mybaby.to_pickle('./mybaby.pickle')

# # save as HDF (large size)
# mybaby.to_hdf('./mybaby.hd5', key='mybaby', format="table")

# # to csv file 
# mybaby.to_csv('./mybaby.csv')


# ###############  READING FROM FILE  ##############
mybaby = pd.read_parquet('./mybaby.paraquet')


mybaby.head()
# mybaby.columns['index','name', 'sex', 'freq']
mybaby.tail()
mybaby.shape
mybaby.dtypes


# Filter males 
male = mybaby [mybaby['Sex'] =='M']
male.head()
# Filter females 
female = mybaby [mybaby['Sex'] =='F']
female.head()


## TESTING PURPOSES 
# sample father and mother from names 
father = male[male['Frequency'] >5000].sample(1).iloc[0]['Name']
mother = female[female['Frequency'] >15000].sample(1).iloc[0]['Name']
#mother = female.sample(1).iloc[0]['Name']
print (father, mother)

# female['Frequency'].describe()

 #father = 'Narendra'
# mother = 'Lena'



# f = father.iloc[0]['Name']

# mothmer = mother.iloc[0]['Name']

dic = pyphen.Pyphen(lang='en')
# print (dic.inserted('Nancy'))

# father
sMale = dic.inserted(str(father))
sFemale =  dic.inserted(str(mother))
print (sMale, sFemale)

syll = (sMale+'-'+sFemale).split('-')
syll
#syll = ['Dani', 'el', 'so', 'ia']
# syll = ['Jer', 'ami', 'Adre', 'reana', 'rina']

final = pd.DataFrame( columns=['Name', 'Sex', 'Frequency'] )
final
mybaby.head()
mybaby.columns

for item in syll: 
    if (len(item) >= 3): 
        p = (mybaby[mybaby['Name'].str.contains(item)]).copy()
        print ('syllable ==>', item)
        # sort and show top 10
        print ( p.sort_values(by=['Frequency'],
            ascending=False)[:10]) 
        # final.append(p)

final 
pd.concat(final, axis=1)
final 

final = pd.DataFrame(final)

final

final.sort_values('Name', inplace = True)   
final.drop_duplicates(subset ="Name", keep = "first", inplace = True)

print ((p[p['Sex']=='F']).sort_values(by=['Frequency'],ascending=False)[:10])
print ((p[p['Sex']=='M']).sort_values(by=['Frequency'],ascending=False)[:10])