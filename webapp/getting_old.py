import httplib, urllib, base64,json
#This is the actual one
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
                try:
                        return answer[0]['scores']
                except:
                        print "none"       

