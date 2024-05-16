import requests
from bs4 import BeautifulSoup

books_rating=[]
books_name=[]
books_price=[]
books_link=[]


for j in range(1,51):
  response=requests.get(f'https://books.toscrape.com/catalogue/page-{j}.html')
  soup=BeautifulSoup(response.text,'html.parser')
  books_nm=soup.find_all('article',class_='product_pod')
  books_pr=soup.find_all('div',class_='product_price')
  books_lk=soup.find_all('article',class_='product_pod')
  books_rt=soup.find_all('article',class_='product_pod')

  for i in range(20):
    books_name.append(books_nm[i].find('a',title=True).attrs['title'])
    books_price.append(books_pr[i].find('p').text.strip('A'))
    link=books_lk[i].find('a').attrs
    books_link.append('https://books.toscrape.com/catalogue/'+link['href'])
    bk=books_rt[i].find('p').attrs
    books_rating.append(bk['class'][1])



import pandas as pd
df=pd.DataFrame()

for i in range(len(books_name)):
  df-df._append({'book Name':books_name[i],
                'Price':books_price[i],
                'Star Rating':books_rating[i],
                'Link of the Book':books_link[i]},ignore_index=True)

display(df)