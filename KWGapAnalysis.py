import pandas as pd
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from functools import reduce

HLDF = pd.read_csv('~/__HOMELIGHT/HomeLight/SEO_Keywords_HL_9_10_2022.csv')

HLrent=HLDF.loc[HLDF['Keyword'].str.contains(fr'\brent',regex=True)]

text = " ".join(i for i in HLrent['Keyword'])

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

plt.figure( figsize=(30,20))
plt.imshow(wordcloud, interpolation='bilinear')


# ----------------------------------------------------------
# 
# MS1 = pd.read_csv("/home/barca/__HOMELIGHT/KWGapData/1-Missing.csv")
# 
# 
# MS1.head()
# 
# 
# KWGaps['Missing']
# 
# 
# # dictionary loop
# for k in KWGaps:
#     print(KWGaps[k])
# 
# 
# # dict loops keys
# for k in KWGaps.keys():
#     print(k)
# 
# for i in range(1,7):
#     print(i)
# 
# for k,v in KWGaps.items():
#     print(k,v)
# 
# 
# 
# for i in range(1,7):
#     for k, v in KWGaps.items():
#         print(dirpath+str(i)+'-'+k+'.csv')
#         #print(str(i)+'-'+k+'.csv'+'  :::  '+v+str(i))
# 
# import csv's as dataframes
dirpath = '/home/barca/__HOMELIGHT/KWGapData/'

KWGaps = {'Missing':'MS',
            'Weak':'WK',
            'Strong':'SG',
            'Untapped':'UT',
            'Unique':'UQ'
}

sitepages = ['homelight.com (pages)',
'zillow.com (pages)',
'realtor.com (pages)',
'rocketmortgage.com (pages)',
'rockethomes.com (pages)',
'forsalebyowner.com (pages)',
'listwithclever.com (pages)',
'opendoor.com (pages)',
'redfin.com (pages)',
'trulia.com (pages)',
'remax.com (pages)',
'compass.com (pages)',
'homes.com (pages)',
'century21.com (pages)',
'coldwellbanker.com (pages)',
'sothebysrealty.com (pages)',
'themortgagereports.com (pages)',
'quickenloans.com (pages)',
'bhhs.com (pages)',
'upnest.com (pages)',
]


sites = ['homelight.com',
'zillow.com',
'realtor.com',
'rocketmortgage.com',
'rockethomes.com',
'forsalebyowner.com',
'listwithclever.com',
'opendoor.com',
'redfin.com',
'trulia.com',
'remax.com',
'compass.com',
'homes.com',
'century21.com',
'coldwellbanker.com',
'sothebysrealty.com',
'themortgagereports.com',
'quickenloans.com',
'bhhs.com',
'upnest.com',
]


"""  TEST SCRIPTS
for i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
        print(dfname)


# MS2.head()
# UQ1.head()

for i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
        print((dirpath+str(i)+'-'+k+'.csv'))
        print(dfname)
"""


# Create list of pandas dataframes
data_frames=[]
for i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
        colname = v+str(i)
        dfname = pd.read_csv(dirpath+str(i)+'-'+k+'.csv')
        dfname['source'] = colname
        #dfname.head()
        dfname = dfname.drop(sitepages, axis=1, errors='ignore')
        dfname = dfname.drop(sites, axis=1, errors='ignore')
        data_frames.append(dfname)

# test loop to get each dataframe
# for i in range(30):
#     dfname='df'+str(i)
#     print(dfname)
#     dfname = data_frames[0]
       
df1= data_frames[0]
df2= data_frames[1]
df3= data_frames[2]
df4= data_frames[3]
df5= data_frames[4]
df6= data_frames[5]
df7= data_frames[6]
df8= data_frames[7]
df9= data_frames[8]
df10= data_frames[9]
df11= data_frames[10]
df12= data_frames[11]
df13= data_frames[12]
df14= data_frames[13]
df15= data_frames[14]
df16= data_frames[15]
df17= data_frames[16]
df18= data_frames[17]
df19= data_frames[18]
df20= data_frames[19]
df21= data_frames[20]
df22= data_frames[21]
df23= data_frames[22]
df24= data_frames[23]
df25= data_frames[24]
df26= data_frames[25]
df27= data_frames[26]
df28= data_frames[27]
df29= data_frames[28]
df30= data_frames[29]
        
df15.head()

merge1 = pd.merge(df1, df2, on=['Keyword'],how='outer')
merge1.head()

# merge all KWs and KW data 
#df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='outer'), data_frames).fillna('void')
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='outer'), data_frames)

len(df_merged)
df_merged[:10].to_csv('~/df_merged_test.csv')



# GET the average for all columns
SearchVol = [col for col in df_merged.columns if 'Search Volume' in col]
len(SearchVol)
df_merged2 = df_merged.copy()
df_merged2['FinalSearchVol'] = df_merged2[SearchVol].mean()
df_merged2[SearchVol]
df_merged2.columns.get_loc[SearchVol]

import numpy as np
def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols,query_cols,sorter=sidx)]

df_merged3 = df_merged[['Keyword','Search Volume_x','Search Volume_y']]
df_merged3
df_merged3.shape

SearchColNames = ['SearchVol1',
'SearchVol2',
'SearchVol3',
'SearchVol4',
'SearchVol5',
'SearchVol6',
'SearchVol7',
'SearchVol8',
'SearchVol9',
'SearchVol10',
'SearchVol11',
'SearchVol12',
'SearchVol13',
'SearchVol14',
'SearchVol15',
'SearchVol16',
'SearchVol17',
'SearchVol18',
'SearchVol19',
'SearchVol20',
'SearchVol21',
'SearchVol22',
'SearchVol23',
'SearchVol24',
'SearchVol25',
'SearchVol26',
'SearchVol27',
'SearchVol28',
'SearchVol29',
'SearchVol30'
]


df_merged3.columns.values[1:31] = SearchColNames
df_merged3.head()
df_merged3['FinalSearchVolume']=df_merged3[SearchColNames].mean(skipna=True)
df_merged3[['Keyword','FinalSearchVolume']]

column_index(df_merged2, SearchVol)
SearchVol


KWData = df_merged['Keyword']
KWData



AllKW = df_merged[['Keyword','Search Volume_x']]
AllKW = AllKW.iloc[:,:2]
AllKW.head()
AllKW.rename(columns={'Search Volume_x':'Search Volume'},inplace=True)


AllKW.head()
data_frames.insert(0,AllKW)

df_vol = reduce(lambda  left,right: pd.merge(left,right[['Keyword','Search Volume']],on=['Keyword'], how='left'), data_frames)

df_vol.head()

len(df_vol)

t1 = pd.merge(MS1,MS2)

MS2.head()





# create list of DFNames
for  i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
data_frames



a=0
for  i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
        a=a+1
        print(str(a),'- '+dfname)




dflist = ['James','Armida',"Dominic"]

dflist
dflist.pop(2)

dflist[]


