import requests
url = "http://eoddata.com/stocklist/NASDAQ/A.htm"
page = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

elements=[]
table=soup.find('div',{'id':'ctl00_cph1_divSymbols'})
for tr in table.find_all('tr'):
	for td in tr.find_all('td'):
		element= td.text
		elements.append(element)
x=len(elements)

symbol=[]
for y in range(0,x,10):
	symbol.append(elements[y])
names=[]
for y in range(1,x,10):
	names.append(elements[y])

import pandas as pd
df = pd.DataFrame(index = None)
df['stock_symbol'] = symbol
df['stock_name'] = names

df.set_index('stock_symbol', inplace = True)
print(df.head())

df.to_json('NASDAQ Stock List')


