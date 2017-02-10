# -*- coding: utf-8 -*-
import indicoio

indicoio.config.api_key = '13dc8340875d36746ad23178688494d4'
#This is the actual one
class textProcess:
        
        def __init__(self,text):
               try:
                self.data=indicoio.emotion(text)
                
               except:
                self.data=None                          
              
        def get_json(self):
               self.data['happiness'] = self.data.pop('joy')
               return self.data
       


