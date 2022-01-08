import snscrape.modules.twitter as twitterScrapper

def searchByKeyword():
    scraper=twitterScrapper.TwitterSearchScraper('emotion since:2021-01-01 until:2021-05-31')
    for i, tweet in enumerate(scraper.get_items()):
        if i>2:
            break
        print(tweet.user.username)
        print(f"{i} , content: {tweet.content}")


def searchByNames(name,num_of_tweets=10):
    scraper=twitterScrapper.TwitterSearchScraper(f'from:{name}')
    l=[]
    for i, tweet in enumerate(scraper.get_items()):
        if i>num_of_tweets:        # number of tweets that will be fetched 
            break
        # print(tweet.user.username)
        # print(f"{i} , content: {tweet.content}")
        l.append(tweet.content)
    return l


'''
If a name has no tweets it is ignored automatically 
'''

def addingMale_FemaleTweets(gender=0):
    if gender==0:fileName='females'
    elif gender==1:fileName='males'
    else:
        print("invalid input")
        return 
    cnt=0
    with open(fileName,'r') as f :
        
        for i,j in enumerate(f.readlines()):
            print(i)
            #if i >15:break           # stopping at row 15 in the names file      (this condition should be removed for full scraping) 
            
            if i>2000:             # starting from the first name (ignoring the first lines of comments in the file)         
                with open('gender_tweets.csv','a') as file:
                    try:
                        tweett=searchByNames(j)
                        if tweett != None:
                            for kkk in tweett:
                                file.write( f'{gender},{kkk}\n')
                            cnt+=1
                            
                    except:pass
    print(cnt)
# addingMale_FemaleTweets()
addingMale_FemaleTweets(1)

# done till 1800

