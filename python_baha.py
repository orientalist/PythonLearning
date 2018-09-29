from bs4 import BeautifulSoup as soup
import urllib2
import mysql.connector
from datetime import date,datetime,timedelta
from selenium import webdriver

#get datetime of system
row_dateTime=datetime.now().date()

#URL to craw
bahaURL="https://forum.gamer.com.tw/?page=0&c=94"

#create request
myReq=urllib2.Request(bahaURL,headers={'User-Agent':'User001'})

#begin sending request
uClient=urllib2.urlopen(myReq)

#get raw html
pageHtml=uClient.read()

#close the request
uClient.close()

#soup the html
page_soup=soup(pageHtml,'html.parser')

#make it more readable
page_soup.prettify()

#get specific elements
AllTitleDivs=page_soup.find('div',{"id":"BH-master"})

for div in AllTitleDivs:
    print(div)