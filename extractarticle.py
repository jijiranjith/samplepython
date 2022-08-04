
import urllib.request
import requests
from bs4 import BeautifulSoup


HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',

                'Accept-Language': 'en-US, en;q=0.5'})  
# target url
url = 'https://www.health.com/news/covid-vaccine-nasal-spray'

 
# making requests instance
reqs = requests.get(url,headers=HEADERS)

 
# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

 
# displaying the title
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())

#display article text
print("Article: ")
for data in soup.find_all("p"):
    print(data.get_text())
   
file = open('1.txt', 'w')
file.write(title.get_text())
file.write(data.get_text())
file.close()
