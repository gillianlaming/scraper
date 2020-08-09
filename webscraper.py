from bs4 import BeautifulSoup
import requests
import urllib.request,sys,time
import pandas as pd 

#url of the page that we want to Scarpe
#+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
URL = 'https://www.nytimes.com/'

try:
     # this might throw an exception if something goes wrong.
     page=requests.get(URL)      # this describes what to do if an exception is thrown
     print("Success!") 
except Exception as e:    
    
    # get the exception information
    error_type, error_obj, error_info = sys.exc_info()      
    
    #print the link that cause the problem
    print ('ERROR FOR LINK:',URL)
    
    #print error info and line that threw the exception                          
    print (error_type, 'Line:', error_info.tb_lineno)
    
   #continue

content=BeautifulSoup(page.content,'html.parser')
#print(content.prettify())
weblinks = content.find_all('article')
#mainContent=content.find_all("div",class_="balancedHeadline")
print(len(weblinks))


