import pickle
def getData():
                with open ('outfile', 'rb') as fp:
                        itemlist = pickle.load(fp)
                with open ('outfile1', 'rb') as fp:
                        tweetlist = pickle.load(fp)  
                with open('pic', 'rb') as fp:
                        picture=pickle.load(fp)
	        return itemlist,tweetlist,picture
