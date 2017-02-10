import operator 
from parse_insta_json import parseJson
from parse_twitter_json import get_json
from datetime import datetime
import calendar


def getMood(instagram_user,twitter_username):
        print instagram_user,twitter_username
        instagram_values_caption=parseJson(instagram_user) #photos not caption
        twitter_values_photo=get_json(twitter_username)
        
        #facebook_values=[['12312302',{'sad':'0.4'},{'angry':0.3}] ,['12312320',{'happy':'0.57'},{'surprise':0.32}] ,['12312299',{'disgust':'0.23'},{'angry':0.1}] ]
        #twitter_values=[]
        
        aggr=instagram_values_caption+twitter_values_photo

        aggr=sorted(aggr,reverse=True)
        print aggr
        print "******************************"
        d = datetime.utcnow()
        current = calendar.timegm(d.utctimetuple())
       
        #print instagram_values_caption
        # This basically subs the dates in the aggr from current date and creates a mappable value. Garna time lagya thyo do not  modify.
        diff=[(current- int(a))/500 for a in (aggr[j][0] for j in range(len(aggr)))] 
        
        multiplier=[pow(1.01,-x) for x in diff]
       
        norm= [i/sum(multiplier) for i in multiplier]
       
        a=[ [[aggr[n][1].keys()[0],aggr[n][1].values()[0]],[aggr[n][1].keys()[1],aggr[n][1].values()[1]]] for n in range(len(aggr))]
        ab=[]
        final = {}
        
        for j in range(len(norm)):
                ab.append({a[j][0][0]:float(a[j][0][1])*norm[j]})
                ab.append({a[j][1][0]:float(a[j][1][1])*norm[j]})
       # print"Here", ab
        #print len(ab)
        keys=[ab[j].keys()[0] for j in range(len(ab))]
        #print keys      
        print "***********************"
        for k in keys:           # Init all elements to zero.
            final[k] = 0
        for d in ab:
            for k in d.keys():
                final[k] = final[k] + d[k]  
        #print final     

        sorted_final= sorted(final.items(), key=operator.itemgetter(1),reverse=True)
        
        print sorted_final
        print "THE MOOOD IS: ",sorted_final[0][0]   
        print "***********************"
        print "***********************"     
        return sorted_final
        #aggr_final=[{aggr[n][1].keys():aggr[n][1].values()*norm[n] for n in range(len(aggr))}]

