import urllib
import re
from bs4 import BeautifulSoup
############################################
import MySQLdb
db=MySQLdb.connect(user="root",passwd="",db="mysql",unix_socket="/opt/lampp/var/mysql/mysql.sock")
cu=db.cursor()
cu.execute("select * from backtable1")
res=cu.fetchall()
ls=[]
for row in res:
	ls.append(row[0])
#print ls
db.close()
#########################################
myurl='http://bangalore.backpage.com/'
fob= urllib.urlopen(myurl)
soup= BeautifulSoup(fob.read())
#print(soup.title.text)
#print "list",ls
#ls=['Antiques']
fob1= open("/opt/lampp/cgi-bin/backlinkscgi.txt","w+")
for tag in soup.findAll('li',{"class":"indexSectionList"}):
	children=tag.findChildren()
	for child in children:	
		fob1.write(child['href']+"?layout=full"+'\n')
				
fob1.close()
count=0
fob2= open("/opt/lampp/cgi-bin/backlinkscgi.txt","r")
outfi = open("/opt/lampp/cgi-bin/information.txt","w")
for url in fob2.readlines():
    #print"url: ",url
    #print "ls[count]=",ls[count]
    if((count<len(ls)) and ls[count] in url):
	    count=count+1
	    #print"count: ",count
	    fob3= urllib.urlopen(url)
	    #print"Url opened\n"
	    soup1= BeautifulSoup(fob3.read())
	    #print(soup1.title.text)
	    outfi.write("================================================================================================================================================"+'\n')
            outfi.write(soup1.title.text+'\n')
            outfi.write("================================================================================================================================================"+'\n')
	    im= soup1.findAll('img')
	    [j.extract() for j in im]
	    bo= soup1.findAll('div',{'id':"postingTitle"})
	    bo2=soup1.findAll('div',{'class':'postingBody'})
	    bo1=soup1.findAll('div',{'class':'adInfo'})
	    count1=0
            for i in bo:
		 try:
			 
			 #print(i.text +'\n')
			 temp = i.text.replace(u"\xa0", u" ")
			 (temp).encode('ascii','ignore')
			 #print"Reached here!"
		       	 outfi.write(temp)
			 #print"bo2[count1]= ",bo2[count1].text
	       		 ch=bo2[count1].findChildren('a')
			 for k in ch:
				tmp1 =k['href']
				#print "tmp1:",tmp1
				temp1= tmp1.replace(u"\xa0", u" ")
				temp1.encode('ascii','ignore')
				k.extract()
			 #print "temp1= ",temp1
			 temp2= bo2[count1].text.replace(u"\xa0", u" ").replace(u"\u2013", u" ") .replace(u"\u2019", u" ")
			 (temp2).encode('ascii','ignore')
			 #print"body: ",temp2
		         temp3= bo1[count1].text.replace(u"\xa0", u" ")
			 (temp3).encode('ascii','ignore')
			 count1 +=1 
			 outfi.write('\n'+temp2+'\n')
			 #print"Again here"
			 outfi.write('\n'+temp1)
				 
			 outfi.write('\n'+temp3)
			 #print"bo1[count1]=",temp3	 
		                 
			 outfi.write("--------------------------------------------------------------------------------------------------------------------"+'\n')     
		 except UnicodeEncodeError:
	         	 #print"Character found"
			 pass
    		 
    
    #else:
        #print"Error"
fob2.close()
outfi.close()
