import pandas as pd
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np

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

kwmetrics = ['Search Volume','Keyword Difficulty','CPC','Competition','Results','Keyword Intents']
kwmetricsV2 = ['Search Volume','Keyword Difficulty','CPC','Competition','Results']



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

##################################################
# Create list of pandas dataframes, for KW metrics
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


# create list of dataframes for rankings only
rankingsdf=[]
for i in range(1,7):
    for k, v in KWGaps.items():
        dfname = v+str(i)
        colname = v+str(i)
        dfname = pd.read_csv(dirpath+str(i)+'-'+k+'.csv')
        dfname['source'] = colname
        #dfname.head()
        dfname = dfname.drop(sitepages, axis=1, errors='ignore')
        dfname = dfname.drop(kwmetrics, axis=1, errors='ignore')
        rankingsdf.append(dfname)

###############################################3333

# test loop to get each dataframe
# for i in range(30):
#     dfname='df'+str(i)
#     print(dfname)
#     dfname = data_frames[0]
       
# commented for now to shorted scripts, need to be unfolded
"""
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
"""      

#merge1 = pd.merge(df1, df2, on=['Keyword'],how='outer')
#merge1.head()

#############################################################

# ------------------------
# merge all KWs and KW data
# ------------------------
#df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='outer'), data_frames).fillna('void')
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='outer'), data_frames)


# ------------------------
# merge rankings keywords
# ------------------------
df_rankmerged = reduce(lambda left, right: pd.merge(left,right,on=['Keyword'],how='outer'),rankingsdf)

#------------------------------------------------------------

# GET the average for all columns
# SearchVol = [col for col in df_merged.columns if 'Search Volume' in col]
# len(SearchVol)
# df_merged2 = df_merged.copy()
# df_merged2['FinalSearchVol'] = df_merged2[SearchVol].mean()
# df_merged2[SearchVol]
# df_merged2.columns.get_loc[SearchVol]

#################################################
# Search volume
# Get the Unify the metrics of the columns
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
df_merged3['FinalSearchVolume']=df_merged3[SearchColNames].mean(axis=1,numeric_only=True,skipna=True)

# test if data accurate
df_merged3[['Keyword','FinalSearchVolume']].sample(20)


#############################################################

#- test data for RANKINGS
dftest = df_rankmerged.copy()
dft = dftest.copy()


#- test data for Metrics
dfmetrics = df_merged.copy()
dfm = dfmetrics.copy()

def ColCleaner(df,colkw):

    colt = [col for col in df.columns if colkw in col]
    tolcols = len(colt)+1

    colnames = [colkw+str(i) for i in range(1,tolcols)]

    coldupes = [col for col in df.columns if colkw in col]
    coldupes.insert(0,"Keyword")

    df = df[coldupes]  #include keyword and colkw

    df.columns.values[1:tolcols] = colnames
    #finalcolname = 'Final'+colkw
    df[colkw] = df[colnames].mean(axis=1,numeric_only=True,skipna=True)

    df = df[['Keyword',colkw]]

    return df


def ColQA(df,colkw):

    colt = [col for col in df.columns if colkw in col]
    tolcols = len(colt)+1

    colnames = [colkw+str(i) for i in range(1,tolcols)]

    coldupes = [col for col in df.columns if colkw in col]
    coldupes.insert(0,"Keyword")

    df = df[coldupes]  #include keyword and colkw

#    df.columns.values[1:tolcols] = colnames
#    finalcolname = 'Final'+colkw
#    df[finalcolname] = df[colnames].mean(axis=1,numeric_only=True,skipna=True)
#
#    df = df[['Keyword',finalcolname]]

    return df


# sample data for the calculation
quickendf = ColCleaner(dft,'quickenloans.com')
quickendf.head()


###############################################
# COMPILE ALL DATA

#--------------------------------------------------
# Compile all rankings
ranklistdf = []
for i in sites:
    i = ColCleaner(dft,i)
    ranklistdf.append(i)
len(ranklistdf)

FinalRankMerged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='left'), ranklistdf)
FinalRankMerged = FinalRankMerged.replace(0,np.nan)
FinalRankMerged.head()
FinalRankMerged.info()

#--------------------------------------------------
# Compile all KW Metrics
allkwmetricsdf = []
for i in kwmetricsV2:
    i = ColCleaner(dfm,i)
    allkwmetricsdf.append(i)
len(allkwmetricsdf)

FinalMetricsMerged = reduce(lambda  left,right: pd.merge(left,right,on=['Keyword'], how='left'), allkwmetricsdf)
FinalMetricsMerged = FinalMetricsMerged.replace(0,np.nan)
FinalMetricsMerged.head()
FinalMetricsMerged.info()

###############################################
# FULL MERGED OF DF
##############################################
FullDF = pd.merge(FinalMetricsMerged,FinalRankMerged, how='left', on='Keyword')
FullDF.info()
FullDF.to_csv('~/fulldf.csv')
###############################################

FDF = FullDF.copy()
FD = FDF.copy()

# create a competitor list, by taking out homelight from sites
compsites = sites.copy()
compsites.remove('homelight.com')


FD[compsites]
FD['Quantile'] = FD[compsites].quantile(q=0.25, axis=1, numeric_only=True, interpolation='linear')
FD['AvgRank']= FD[compsites].mean(axis=1,numeric_only=True,skipna=True)
FD['Competitors'] = FD[compsites].count(axis=1,numeric_only=True)
FD['WordCount'] = FD['Keyword'].str.count(' ') + 1
FD.drop('CompRankCount', axis=1, inplace=True)
FD.head()

def df_column_switch(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df

#FD = df_column_switch(FD,'Competitors','WordCount')
FD.head()


FD.to_csv('~/__HOMELIGHT/FullData.csv')


QWords = ['how','what','why','when','who','whose','which','where']


#

#------------------------------------------------------------
# QA result
b = ColQA(dft,'quickenloans.com')
b['total'] = b.sum(axis=1,numeric_only=True,skipna=True)
b['total'].count()


