#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
# getlist() returns a list containing the
# values of the fields with the given name
options = form.getlist('option')

ls=[]
print "Content-Type: text/html\n"
print '<html><title>Web Scraper-Found</title>'
print'<body text="MistyRose" bgcolor="Navy">'
#print 'The options list:', options

if(len(options)==0):
	print"<br/><br/><br/><br/><h1 align='center'>Please Select atleast one of the options</h1><br/><br/>"
	print"<div style 'text-align:center;'><img src='http://www.sherv.net/cm/emoticons/confused/yellow-smiley-confused-emoticon.gif'></div>"
	print"<a href='http://localhost/back.html' style= 'color:MistyRose'><h3>Go back</h3></a>"
else:
	print"<h1>You searched for:</h1>"
	for opt in options:	
		print '<h3>', cgi.escape(opt), '</h3>'
		ls.append(opt)
		#print '<p>' ,ls,'</p>'
		#print '</body></html>'
	print"<div style 'text-align:center;'><img src='http://www.sherv.net/cm/emoticons/yes/huge-thumbs-up-smiley-emoticon.gif' ></div>"
	import MySQLdb
	db=MySQLdb.connect(user="root",passwd="",db="mysql",unix_socket="/opt/lampp/var/mysql/mysql.sock")
	cu=db.cursor()
	st="create table backtable1 (opti varchar(20));"
	cu.execute(st)
	for opt in options:
		cu.execute("INSERT INTO backtable1 (opti) VALUES ('%s')" %(opt))
		db.commit()
	
	db.close()

	import os
	os.system("python webscraper.py")
	print"<p>Search Complete!! Open information file to view scraped results</p>"
	db=MySQLdb.connect(user="root",passwd="",db="mysql",unix_socket="/opt/lampp/var/mysql/mysql.sock")
	cu=db.cursor()
	cu.execute("drop table backtable1;")
	db.close()
	print '</body>'
	print '</html>'

