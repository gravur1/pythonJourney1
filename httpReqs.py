#pip install requests --upgrade

from os import stat
from apispec import APISpec
import requests
from pprint import pprint
import json
import webbrowser
#resp = requests.get("https://www.metaweather.com/api/location/2487956/2018/11/28")
#print(resp.status_code) # should return 200
#file = open("/home/kali/httpFile", 'r+')
#file.write(resp.text)
#file.close()


#########
#### Getting data
#data = json.loads(resp.text)
#pprint(data)

#########
#### Getting info about other API
#responseStar = requests.get("http://swapi.co/api/planets/3")
#print(responseStar.status_code)
#print(responseStar.text)


#########
#### Get requests with Parameters and open web urls
#url = "http://www.wikipedia.org"
#resp_obj = requests.get(url)
#print(resp_obj)
#webbrowser.open(resp_obj.url)

#search_term = input("Enter the term you want to search: ")
#URL = 'http://www.youtube.com/search'
#PARAMS = {'q' : search_term}
#r_get = requests.get(url = URL, params = PARAMS)
#print(r_get.status_code)
#print(r_get.url)
#webbrowser.open(r_get.url)

#########
#### Post requests
#r_post = requests.post('https://en.wikipedia.org/w/index.php', data = {'search' : 'kubernetes'})
#print(r_post.status_code)
#print(type(r_post))
#pprint(r_post.text)

#saving content of the http request to a file
#with open('/home/kali/kubs.html', 'wb') as f:
#    for  chunk in r_post.iter_content(chunk_size=10000):
#        f.write(chunk)

#sending a file as a POST request
#url = 'http://httpbin.org/post'
#files = {'files' : open('/home/kali/newFile', 'rb')}
#values = { 'upload_file' : '/home/kali.newFile', 'OUT' : 'csv'}

#print(files)
#r_post = requests.post(url,files=files,data=values)
#print(r_post.status_code)
#pprint(r_post.text)


#########
#### Post request with multiple attributes
#pastebin API documentation ("http://pastebin.com/api")
post_link = 'http://pastebin.com/api/api_post.php'
payload = "{'username' : 'john', 'email' : 'john@john.com'}"
API_KEY = '<>'
parameters = {'api_dev_key':API_KEY,
              'api_option':'paste',
              'api_paste_code':payload,
              'api_paste_format':'python'}
r_post = requests.post(post_link, data=parameters)

if(r_post == 200):
    print("Successful request")
    print("You can find the coe pasted on this link: {}".format(r_post.text))
    webbrowser.open(r_post.text)
else:
    print("Failed to process the request")



