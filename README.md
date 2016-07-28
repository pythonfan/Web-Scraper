# Web-Scraper
###Introduction
This application connects to backpage.com, scrapes information from it using BeautifulSoup based on the user’s selection of categories and stores it in a uniformly formatted text file in the user’s local directory. 
It is aimed at eliminating distractions caused by advertisements and unwanted links popping up.
The application provides a single interface to users using Python CGI through which they can access multiple pages by selecting all the required options.

###Filename: webscraper1.py

-Appends all the selected options into a list.

-Creates a table “backtable1” inside database
called mysql.

-This table contains the selected choices.

-Executes “webscraper.py”

-Deletes the table for reuse.

###Filename: webscraper.py

-Opens the database , retrieves the table
contents and stores it in a list.

-Goes to the backpage website

-Parses its HTML source.

-Stores the links in backlinkscgi.txt file .

-Compares the list items with the links and goes
to those urls.

-Scrapes the data from urls and stores it in
information.txt file.
