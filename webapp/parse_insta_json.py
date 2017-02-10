import json,requests,operator
#from text_sentiment import get_sentiments
from getting_old import imageProcess    
from text_sentiment import textProcess
import pickle

insta_image=[]
# format ['12312312',{'sad':'0.8'},{'angry':0.4}] ,['12312300',{'happy':'0.7'},{'surprise':0.2}] ,['12312310',{'disgust':'0.9'},{'angry':0.1}]]
def parseJson(username):
        url='http://instagram.com/'+username+'/?__a=1'
        net_media=[]
        print url
        json_data=requests.get(url).json()
        insta_pic=json_data['user']['profile_pic_url_hd']
        for media in  json_data['user']['media']['nodes']:
                net_media.append([media['caption'],media['thumbnail_src'],media['date']])
        net_emotions_text=[]
        net_emotions_media=[]
        
        for each_media in net_media[:5]:
                   insta_image.append(each_media[0])
                   emotions=imageProcess(each_media[1])
                   emotions=emotions.get_emotions()
                   #print emotions
                   text_emotions=textProcess(each_media[0])
                   text_emotions=text_emotions.get_json()
                  # print each_media[0],text_emotions
                   if text_emotions==None and emotions != None:
                        lists=emotions
                   elif emotions==None and text_emotions!= None:
                        lists=text_emotions
                   elif text_emotions == None and emotions==None:
                        lists=None
                   else:
                       
                        lists= {key: emotions[key] + text_emotions.get(key, 0) for key in emotions.keys()}
                  
                   if lists!=None:          
                        lists=(sorted(lists.items(), key=operator.itemgetter(1),reverse=True))
                        
                        lists=dict((x,y) for x,y in lists[:2])
                        print lists
                        net_emotions_media.append([each_media[2],lists])
                              
                  # print lists : Remainign tasks, sort the results for lists before printing
                  
                   #text_sentiment=get_sentiments(each_media[0])
                   #net_emotions_text.append([each_media[2],text_sentiment])
        
        with open('outfile', 'wb') as fp:
                pickle.dump(insta_image, fp)
        with open('pic', 'wb') as fp:
                pickle.dump(insta_pic, fp)
        return net_emotions_media        
        #print net_emotions_text
#print parseJson('sandeep.neupane')    

