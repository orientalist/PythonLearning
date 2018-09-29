from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uop
import urllib2 as ulb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from operator import itemgetter


browser=webdriver.Chrome()

myUrl='https://www.instagram.com/doiuky/'

browser.get(myUrl)

time.sleep(1)

elem=browser.find_element_by_tag_name('body')

no_of_pagedowns=60
element_imgs=list()
temp_imgs=list()
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    page_soup=soup(browser.page_source,'html5lib')
    page_imgs=page_soup.find_all('img',{'class':'FFVAD'})
    
    if no_of_pagedowns!=60:
        resultSet=set(page_imgs).difference(set(temp_imgs))
        element_imgs.append(resultSet)
        temp_imgs=page_imgs
    else:
        temp_imgs=page_imgs
        element_imgs.append(page_imgs)
        
    no_of_pagedowns-=1



index=0
for img_list in element_imgs:
    for img in img_list:
        urllib.urlretrieve(img["src"],"test"+str(index)+".jpg")
        index+=1

