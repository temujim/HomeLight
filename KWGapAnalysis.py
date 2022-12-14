import pandas as pd
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np

HLDF = pd.read_csv('~/__HOMELIGHT/HomeLight/SEO_Keywords_HL_9_10_2022.csv')

HLrent=HLDF.loc[HLDF['Keyword'].str.contains(fr'\brent',regex=True)]

text = " ".join(i for i in HLDF['Keyword'])

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

plt.figure( figsize=(30,20))
plt.imshow(wordcloud, interpolation='bilinear')


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
FullDF.to_csv('~/20220915fulldf.csv')
###############################################

FDF = FullDF.copy()
FD = FDF.copy()

# create a competitor list, by taking out homelight from sites
compsites = sites.copy()
compsites.remove('homelight.com')


# get the rank count and the quantile rankings data of competitors
FD[compsites]
FD['Quantile'] = FD[compsites].quantile(q=0.25, axis=1, numeric_only=True, interpolation='linear')
FD['AvgRank']= FD[compsites].mean(axis=1,numeric_only=True,skipna=True)
FD['Competitors'] = FD[compsites].count(axis=1,numeric_only=True)
FD['WordCount'] = FD['Keyword'].str.count(' ') + 1
FD['KWValue'] = FD['Search Volume'] * FD['CPC']
#FD.drop('CompRankCount', axis=1, inplace=True)

# move kw value after CPC column
KWValCol = FD.pop("KWValue")
FD.insert(4, "KWValue", KWValCol)
FD.head()

def df_column_switch(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df

#FD = df_column_switch(FD,'Competitors','WordCount')


FD.to_csv('~/__HOMELIGHT/20220915FullDataV2.csv')

QKW = FD[FD['Keyword'].str.contains(r"\b(how|what|why|when|who|whose|which|where|can)\b")]
#QKW.to_csv('~/__HOMELIGHT/BlogKWs.csv')

# exclude 2 words
QKW = QKW[~(QKW['WordCount']<=2)]

# further clean up Blog Keywords (QKW)
# exclude rent keywords without "own"
rent=QKW['Keyword'].str.contains('rent')
own=~QKW['Keyword'].str.contains('own')
QKW=QKW[~(rent&own)]

# QKW.to_csv('~/__HOMELIGHT/BlogKWs.csv')


# Exclude finance only relevant keywords
QKW['FinanceKW']=QKW[['rocketmortgage.com','themortgagereports.com','quickenloans.com']].count(axis=1,numeric_only=True)
A = QKW[~(QKW['FinanceKW']==QKW['Competitors'])]
A.to_csv('~/__HOMELIGHT/FINALBLOG.csv') ## requires slight manual cleaning and keyword selection
 

FD[:][['Keyword','rockethomes.com','homes.com','coldwellbanker.com']].sample(20)

 