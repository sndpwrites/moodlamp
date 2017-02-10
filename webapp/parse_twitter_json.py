import json,operator
from getting_old import imageProcess  
from text_sentiment import textProcess  
#format ['12312312',{'sad':'0.8'},{'angry':0.4}] ,['12312300',{'happy':'0.7'},{'surprise':0.2}] ,['12312310',{'disgust':'0.9'},{'angry':0.1}]]
from twitter import getTweets
import pickle
net_tweets=[]
def get_json(username):
        json=getTweets(username,20)
        tweet_all=[]
        net_emotions_media=[]
        for each_tweet in json:
               emotions=None
               if (each_tweet[2]!=''):
                        sentiment_image=imageProcess(each_tweet[2])
                        emotions=sentiment_image.get_emotions()     
               net_tweets.append(each_tweet[0])        
               sentiment_text=textProcess(each_tweet[0])
               
               text_emotions=sentiment_text.get_json()
               
               if text_emotions==None and emotions != None:
                                lists=emotions
               elif emotions==None and text_emotions!= None:
                                lists=text_emotions
               elif text_emotions == None and emotions==None:
                                lists=None
               else:
                                lists= {key: emotions[key] + (9*text_emotions.get(key, 0)/3) for key in emotions.keys()}
               print "***********"
               print each_tweet[0]
               if lists!=None:          
                                lists=(sorted(lists.items(), key=operator.itemgetter(1),reverse=True))
                                lists=dict((x,y) for x,y in lists[:2])
                                print lists
                                net_emotions_media.append([each_tweet[1],lists])
                #tweet_all.append(each_tweet[1],sentiment_text)
        with open('outfile1', 'wb') as fp:
                pickle.dump(net_tweets, fp)
        
        return net_emotions_media


