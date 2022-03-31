import urllib.request
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
import pandas as pd

url = "https://www.thestar.com.my/search/?q=HIV&qsort=oldest&qrec=10&qstockcode=&pgno=1"
base_url = "https://www.thestar.com.my/search/?q=HIV&qsort=oldest&qrec=10&qstockcode=&pgno="
html = urlopen(url)

# returns the web page extraction
bs = BeautifulSoup(html) 
print(bs) 

# returns the no of web pages in the given range
url_list = ["{}{}".format(base_url,str(page)) for page in range(1,400)] 
s = []
for url in url_list:
    # print(url)
    s.append(url)

# returns all the data and save it to the tuple
# print(s)
data = []
data2 = []
for pg in s:
    page = urllib.request.urlopen(pg)
    try:
        search_response = urllib.request.urlopen(pg)
    except urllib.request.HTTPError:
        pass
    soup = BeautifulSoup(page, 'html.parser')
    ls = [x.get_text(strip=True) for x in soup.find_all("h2", {"class": "f18"})]
    ls1=  [x.get_text(strip=True) for x in soup.find_all("span", {"class": "date"})]
    
    data.append((ls))
    data2.append(ls1)
    # print(data)
    # print(data2)

    # stores the value in data frame
    df = pd.DataFrame(data[0],columns=['topic of article'])
    df['Date'] = data2[0]
    print(df)
