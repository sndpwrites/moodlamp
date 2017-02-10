import httplib, urllib, base64,json
#This gets emotions from givenurl
class imageProcess:
        
        def __init__(self,imageurl):
                headers = {
                    # Request headers
                    'Content-Type': 'application/json',
                    'Ocp-Apim-Subscription-Key': 'a0087b0f59144ae0a40ab33cdcdbec50',
                }
                self.imageurl=imageurl
                params = urllib.urlencode({
                })

                try:
                    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
                    print self.imageurl
                    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{'url':'"+self.imageurl+"'}", headers)
                    response = conn.getresponse()
                    self.data = response.read()
                   
                    
                    conn.close()
                except Exception as e:
                    print("[Errno {0}] {1}".format(e.errno, e.strerror))
        def get_json(self):
                return self.data
        def get_emotions(self):
                answer=json.loads(self.data)
                
                return answer
                
a=imageProcess("https://ig-s-c-a.akamaihd.net/hphotos-ak-xfa1/t51.2885-15/sh0.08/e35/p750x750/16464986_380891058936170_3981819473807015936_n.jpg?ig_cache_key=MTQ0NDY2OTExODA1MzQ4Nzk0Mg%3D%3D.2")
print a.get_emotions()
