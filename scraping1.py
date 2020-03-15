# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:29:34 2020

@author: Srihaasa
"""

from bs4 import BeautifulSoup
import certifi
import urllib3
import csv
import re
#from halo import Halo
def getImageurl(url):
    r1 = http.request('GET', url)
    soup = BeautifulSoup(r1.data, 'lxml')
    for choice in soup.find_all('div', class_='poster'):  
        imgurl = choice.img.get("src").encode('utf-8') 
        imgurl= imgurl.decode('utf-8')
        imgurl = imgurl.replace('\n','')
       
    return imgurl  
def getLanguage(url):
    r1 = http.request('GET', url)
    soup = BeautifulSoup(r1.data, 'lxml')
    for a in soup.find_all("a", href=re.compile('language')):
        language= a.text
        #print(language)
    return language
def getPlot(url):
    r1 = http.request('GET', url)
    soup = BeautifulSoup(r1.data, 'lxml')
    for a in soup.find_all('div',class_='inline canwrap') :
        plot= a.span.text
        #print(plot)
    return plot
def getWatch(title):
    title = title.replace(" ", "_")
    title = title.replace(".", "")
    title = title.replace(":", "")
    title = title.replace("-", "")
    title = title.replace(",", "")
    title = title.replace("'", "")
    title = title.replace("__", "_")
    
    isascii = lambda s: len(s) == len(s.encode())
    if (not isascii):
        print("cannot do")
    else:
        print("It may have been an ascii-encoded unicode string")
        title.encode('utf-8')
        title=title.replace(u'\xe9', 'e')
        print(title)
    #url1="https://www.rottentomatoes.com/search/?search=%s"
        url1="https://www.rottentomatoes.com/m/"+ str(title)
        print("entered")
    #url1=url1+str(url)
        r1 = http.request('GET', url1)
        print(url1)
        soup = BeautifulSoup(r1.data, 'lxml')
        #print(soup)
        choice=soup.find("ul", class_='affiliates__list')
        if(choice==None):
            print("not found")
        else:    
            for ch1 in choice.find_all('a'):
                print(ch1.get('href'))
        
        #link= a.href
        
def getreviews(url):
    List=[]
    r1 = http.request('GET', url)
    soup = BeautifulSoup(r1.data, 'lxml')
    for choice in soup.find_all('div', class_='lister-item-content'):  
        review_text = choice.a.text.encode('utf-8') 
        review_text= review_text.decode('utf-8')
        review_text= review_text.replace('\n','')
       # print(review_text)
        List.append(review_text)
        #rating = choice.find('span', class_='rating-other-user-rating').text.encode('utf-8')
        #print(rating)
    return List    
f = open('imdb.csv', 'w',newline='')
csvfile = csv.writer(f)
csvfile.writerow(["Name", "Year of release","Runtime","Language","Cast_Crew","ImageURL","Plot", "Rating", "Genre", "Reviews"])
#pages = int(raw_input("enter number of pages to scrap:"))
pages=1
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2019-01-01,2020-01-01&genres=action'

http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
i = 1
while pages > 0:
    #request = urllib3.request(url)
    #request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0')
    #myurlopener = urllib3.build_opener()
    #myurl = myurlopener.open(request)
    r = http.request('GET', url)
    #spinner = Halo(text="Processing Page", spinner="dots")
    #spinner.start()
    #myurldata = myurl.read()
    soup = BeautifulSoup(r.data, 'lxml')
    #print(r.data)
    for choice in soup.find_all('div', class_='lister-item-content'):                                   # find the and iterate over the div containing required data
        name = choice.a.text.encode('utf-8') 
        name= name.decode('utf-8') 
        cast= choice.select("a[href*=name]")
        for i in range(0,len(cast)):
            mystr=str(cast[i])
            mystrList=mystr.split(">")
            mystr1=mystrList[1]
            cast[i]= mystr1[0: mystr1.find("<")]            
            #print(cast[i])    
        #print(cast)                                                                # get the name of the movie
        imdburl = choice.a.get('href').encode('utf-8')
        imdburl= imdburl.decode("utf-8")
        print(imdburl)
        urlp2= "https://www.imdb.com"+imdburl
        imageurl= getImageurl(urlp2)
        language= getLanguage(urlp2)
        plot= getPlot(urlp2)
        #print(imageurl)
        link= getWatch(name)
        imdburl1= imdburl.split("/")
        print(imdburl1[2])
        urlp1= "https://www.imdb.com/title/"+imdburl1[2]+"/reviews?ref_=tt_urv"
        
        List= getreviews(urlp1)
        reviewsList=[]
        x= len(List)
        if(x<3):
            reviewsList=List
        else:
            reviewsList.append(List[0])
            reviewsList.append(List[1])
            reviewsList.append(List[2])
       # print(imdburl)                                                   # get the imdb url of the movie
        #if not imdburl.startswith('http://www.imdb.com'):                                               # check if link is valid or not
            #imdburl = "http://www.imdb.com" + imdburl
        year = choice.find('span', class_='lister-item-year').text.encode('utf-8')  
        year=year.decode('utf-8')                    # get the year of release of the movie
        try:
            rating = choice.find('div', class_='ratings-imdb-rating').get('data-value').encode('utf-8') # get the ratings of the movie
        except AttributeError:                                                                          # if ratings not available then store "NA"
            rating = "NA"
        rating= rating.decode('utf-8')    
        genre = choice.find('span', class_='genre').text.encode('utf-8')  
        
        genre= genre.decode('utf-8')
        runtime = choice.find('span', class_='runtime').text.encode('utf-8')  
        
        runtime= runtime.decode('utf-8')
        #imageurl = choice.find('div', class_='lister-item-image').get("src")
        #print(imageurl)
        #genre.rstrip("\n")
        genreList=genre.split(',')  
        for i in range (0,len(genreList)):
            genreList[i]=genreList[i].replace("\n","")
            genreList[i]=genreList[i].strip("\r\t")
        print(genreList)                              # get the genre of the movie
        try:
            votes = choice.find('span', {"name": 'nv'}).text.encode('utf-8')                            # get the number of votes for the movie
        except AttributeError:                                                                          # if votes not available then store "NA"
            votes = "NA"
        #print(votes)
        
        csvfile.writerow([name, '2019', runtime,language,cast,imageurl,plot,rating, genreList, reviewsList])                                   # write the fetched values to the csv file
    url = soup.find('a', class_="lister-page-next").get('href')                                         # get the url of next page to be scraped
    if not url.startswith("http://www.imdb.com/search/title"):                                          # check if url is valid or not
        url = "http://www.imdb.com/search/title" + url
    #spinner.stop()
    pages = pages - 1
    print("\nPage Number " + str(i) + " complete")
    i = i + 1
print("Scraping Complete")
f.close()

