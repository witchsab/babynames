import pandas as pd 
# from random import *
import os
import pyphen

BABYNAMEFILE = r'./temp/baby.csv'

dirname = os.getcwd()
filename = os.path.join(dirname, BABYNAMEFILE)
print (filename)

mybaby = pd.read_csv(filename, names=['Name', 'Sex', 'Frequency'])
# mybaby = pd.read_csv('./data/yob2016.txt', names=['Name', 'Sex', 'Frequency'])

# # sorting by first name 
# mybaby.sort_values("Name", inplace = True) 
  
# # dropping ALL duplicte values 
# mybaby.drop_duplicates(subset ="Name", 
#                      keep = False, inplace = True)

mybaby.head()

# mybaby.columns['index','name', 'sex', 'freq']
mybaby.tail()

male = mybaby [mybaby['Sex'] =='M']
male

female = mybaby [mybaby['Sex'] =='F']
female.head()

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
#syll = ['Dani', 'el', 'so', 'ia']
# syll = ['Jer', 'ami', 'Adre', 'reana', 'rina']

for item in syll: 
    if (len(item) >= 3): 
        p = mybaby[mybaby['Name'].str.contains(item)]
        print ('syllable ==>', item)
        print ( p.sort_values(by=['Frequency'],ascending=False)  )