from bs4 import BeautifulSoup as soup
import urllib2
import mysql.connector
from selenium import webdriver
from datetime import date,datetime,timedelta

row_datetime=datetime.now().date()

bahaURL="https://forum.gamer.com.tw/?page=0&c=94"

#if the web has javascript to generate elements
#use PhantomJS
driver=webdriver.PhantomJS()
driver.get(bahaURL)

#page_source() to get raw html
page_soup=soup(driver.page_source,'html.parser')
page_soup.prettify()

titleDiv=page_soup.find('div',{'id':'data-container'})

titlelist=titleDiv.find_all('div',{'class':'forum_list_title'})

#create sql connection
SQLConnection=mysql.connector.connect(user="orientEST99",password="Westgo93",
                                      host='rds-mysql-testing.c5z6ydt3nxpc.ap-southeast-1.rds.amazonaws.com',
                                      database='mySQL_For_Python',auth_plugin='mysql_native_password')

#create sql command
cursor=SQLConnection.cursor()

index=1
for List in titlelist:
    titleA=List.find('a')
    #creat sql string
    addRow=(
        "INSERT INTO `mySQL_For_Python`.Baha_Rank "
        "(NameOfGame,Rank,Date) "
        "VALUES "
        "(%s,%s,%s) "
    )
    row_data=(titleA.text,str(index),row_datetime)
    #execute sql
    cursor.execute(addRow,row_data)
    index+=1
SQLConnection.commit()
cursor.close()
SQLConnection.close()


