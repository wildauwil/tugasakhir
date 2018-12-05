import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from scrapy.http.request import Request

from time import sleep, time
from random import randint

'''
url = 'https://www.tempo.co/indeks/2018/12/04/sport'

response = get(url)
print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_ = 'card card-type-1')
print(type(movie_containers))
print(len(movie_containers))

first_berita = movie_containers[0]
first_berita


coba_title = first_berita.find('h2', class_ = 'title')
coba_title

#first_desc = first_berita.a[2].p.text
#first_desc
'''
'''
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year

first_movie.strong

first_imdb = float(first_movie.strong.text)
first_imdb

first_mscore = first_movie.find('span', class_ = 'metascore favorable')

first_mscore = int(first_mscore.text)
print(first_mscore)

first_votes = first_movie.find('span', attrs = {'name':'nv'})
first_votes

first_votes = int(first_votes['data-value'])

eighth_movie_mscore = movie_containers[7].find('div', class_ = 'ratings-metascore')
type(eighth_movie_mscore)
'''
headers = {"Accept-Language": "en-US, en;q=0.5"}

pages = [str(i) for i in range(1,5)]

# Redeclaring the lists to store data in
title = []
desc = []
lengkap = []
#imdb_ratings = []
#metascores = []
#votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

years_url = ['09','10', '11', '12', '13']
# Extract data from individual movie container
for year_url in years_url:

    response = get('https://www.tempo.co/indeks/2018/01/' + year_url + '/sport' , headers = headers)
    
    # Pause the loop
    #sleep(randint(8,15))
    print (year_url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_ = 'card card-type-1')
    f = open('tes.txt', 'a')
    for container in movie_containers:

            # The name
            coba = container.find('h2', class_ = 'title').text
            #name = container.div.a[2].h2.text
            title.append(coba)

            descript = container.find('div', class_ = 'wrapper clearfix').text
            desc.append(descript)

            news = container.find('a')
            news_link = news.get('href')
            response2 = get(news_link)
            
            #yield detail_request
            html_soup2 = BeautifulSoup(response2.text, 'html.parser')
            
            lebih_lengkap = html_soup2.find('article').text
            lebihh = BeautifulSoup(lebih_lengkap).text
            lengkap.append(lebihh)

            f.write("\ntitle: %s    | deskripsi: %s     | lengkap:  %s   \n" %(coba, desc, lebihh))

        
        
f.close()
import pandas as pd

test_df = pd.DataFrame({'judul': title,
                       'hm': lengkap})
print(test_df.info())
#print(test_df)
