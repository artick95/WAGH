import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://stomarket.com/"



headers={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

tables=soup.find_all('table','table')



table_pd = pd.read_html(str(tables[0]))
print(table_pd)
table_pd[0].to_csv('result.csv')