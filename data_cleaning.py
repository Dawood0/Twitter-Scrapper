import pandas as pd
import re

files=[r'gender_tweets.csv',r'gender_tweets_omar.csv',r'gender_tweets_martin.csv',r'gender_tweets_yousef.csv']
clean_file=r'clean_tweets_test.csv'

def clean(txt):
    TEXT_CLEANING_RE = "@|https?:\S+|http?:\S|[^A-Za-z]+"
    x=re.sub(TEXT_CLEANING_RE,' ',txt)
    return x




for file in files:
    with open(file,'r') as f:
        for i,y in enumerate(f.readlines()):
            print(i)
            clean_txt=''
            if y[0] == '0':
                clean_txt=f'0,{clean(y[2:])}'
            elif y[0] == '1':
                clean_txt=f'1,{clean(y[2:])}'
            else:
                clean_txt=f'{clean(y[2:])}'


            with open(clean_file,'a') as ff :
                ff.write(clean_txt+'\n')

            if i >3:break
# note the clean data still has tweets in multi lines    and empty tweets in some cases




    



