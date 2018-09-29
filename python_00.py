from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uop
import urllib2 as ulb
import mysql.connector
from datetime import date,datetime,timedelta

#URL to  craw
myUrl='https://www.liontravel.com/promotion/holiday/moon_festival/?gclid=Cj0KCQjwof3cBRD9ARIsAP8x70MiOeeOsrCAWy6Y4EgKhR4t1MYP5cJxozcK2ongIiRWHGofYlMh3wkaAh9iEALw_wcB'

#if the web has setted mod_security,forbid spider
#try set urllib.request and add header to pretebt
#as real request

#get system time of python
row_date=datetime.now().date()

#equals ullib2.Request()
myReq=ulb.Request(myUrl,headers={'User-Agent':'user01'})

#Call urlopen by passing URL
#opening up connection,grabbing the page

#equals urllib2.urlopen()
uClient=uop(myReq)

#the way to get raw html
pageHtml=uClient.read()

#remember to close the connection
uClient.close()
#after close the urlopen,call uClient.read() will cause exception
#equal BeautifulSoup()
page_soup=soup(pageHtml,'html.parser')

#pretty the raw html
page_soup.prettify()

#get specific html element
AllSpan=page_soup.findAll('span')
Allp=page_soup.findAll('p')
AllImg=page_soup.findAll('img')
#get text of the element
#for span in AllSpan:
#    print(span.text)
# for img in AllImg:
#    print(img.src)

#get specific element by additional attribute
AllDivs=page_soup.find_all('div',{"class":"item"})

cnx=mysql.connector.connect(user='orientEST99',password='Westgo93',host='rds-mysql-testing.c5z6ydt3nxpc.ap-southeast-1.rds.amazonaws.com',
                            database='mySQL_For_Python',auth_plugin='mysql_native_password')

#get insert commandor
cursor=cnx.cursor()
for div in AllDivs:
    #create sql string
    add_row=("INSERT INTO `mySQL_For_Python`.Tours "
             "(Date,TourName,TourDate) "
             "VALUES "
             "(%s,%s,%s) ")
    row_data=(row_date,div.find('img')['alt'],row_date)
    #execute command
    cursor.execute(add_row,row_data)
cnx.commit()
cursor.close()
cnx.close()    
    