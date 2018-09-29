
txt_file=open("test.txt",'w')
txt_file.write("ssd")
txt_file.close()


index=0
for img in page_imgs:
    urllib.urlretrieve(img["src"],"test"+str(index)+".jpg")
    index+=1