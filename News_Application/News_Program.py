
#-----Set up---------------------------------------------------------#

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from cProfile import label
from ctypes import pointer, resize
from faulthandler import disable
from sys import exit as abort
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD, ITALIC, Font
from tokenize import String
from turtle import back, bgcolor, color

# A function for opening a web document given its URL.
from urllib.request import urlopen

# Some standard Tkinter functions.
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Labelframe, Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.
from re import *

# A function for displaying a web document in the host
# operating system's default web browser 
from webbrowser import open as urldisplay

# All the standard SQLite database functions.
from sqlite3 import *
from xmlrpc.client import boolean

#
#--------------------------------------------------------------------#


#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("\nUnable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Solution---------------------------------------------#

#create main window
world_news = Tk()
world_news.title('World News')

#create font styles
heading_font = ('Arial', 25)
body_font = ('Arial', 20)
status_font = ('Arial', 15, ITALIC)

#set window size
world_news.geometry('750x600')

#set background
bg_colour = 'dodgerblue'
world_news.configure(background = bg_colour)

#creating variable for rss links
daily_mail_rss = 'https://www.dailymail.co.uk/home/index.rss'
abc_rss = 'https://www.abc.net.au/news/feed/2942460/rss.xml'
nytimes_rss = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

#creating a function for when the user click on Daily News radiobutton
def daily_news_interact():
    daily_mail_doc = download(daily_mail_rss)
    status_display['text'] = ('Stories have been downloaded from Daily News (UK)')
    show_source['state'] = (NORMAL)
    show_headline['state'] = (NORMAL)
    save_stories['state'] = (NORMAL)
    print_stories['state'] = (NORMAL)

#creating a function for when the user click on ABC News radiobutton
def abc_news_interact():
    abc_news_doc = download(abc_rss)
    status_display['text'] = ('Stories have been downloaded from ABC News (AUS)')
    show_source['state'] = (NORMAL)
    show_headline['state'] = (NORMAL)
    save_stories['state'] = (NORMAL)
    print_stories['state'] = (NORMAL)

#creating a function for when the user click on New York Times radiobutton
def ny_times_interact():
    nytimes_doc = download(nytimes_rss)
    status_display['text'] = ('Stories have been downloaded from The New York Times (USA)')
    show_source['state'] = (NORMAL)
    show_headline['state'] = (NORMAL)
    save_stories['state'] = (NORMAL)
    print_stories['state'] = (NORMAL)





#creating a function for the show sources push button
def show_sources_functions():
    if news_source_status.get() == 'DailyMail':
        status_display['text'] = "Here is the source of DailyMail's sources..."
        urldisplay(daily_mail_rss)
    elif news_source_status.get() == 'ABC':
        status_display['text'] = "Here is the source of ABC's sources..."
        urldisplay(abc_rss)
    elif news_source_status.get() == 'nytimes':
        status_display['text'] = "Here is the source of The New York Time's sources..."
        urldisplay(nytimes_rss)
    else:
        pass



#creating a function for show headline push button
def show_headline_functions():
    if news_source_status.get() == 'DailyMail':
        daily_mail_doc = download(daily_mail_rss)
        # finding the headline
        daily_mail_headline = findall('<title><!\[CDATA\[(.*?)\]\]></title>', daily_mail_doc)
        # finding the published date
        daily_mail_date = findall('<pubDate>(.*?)</pubDate>', daily_mail_doc)

        #printing status
        status_display['text'] = (f"The latest headlines from DailyMail (UK) are: \n {daily_mail_headline[1]} ({daily_mail_date[0]}) \n {daily_mail_headline[2]} ({daily_mail_date[1]}) \n {daily_mail_headline[3]} ({daily_mail_date[2]})")



    elif news_source_status.get() == 'ABC':
        abc_news_doc = download(abc_rss)
        # finding the headline
        abc_headline = findall('<title>(.*?)</title>', abc_news_doc)
        # finding the published date
        abc_headline_date = findall('<pubDate>(.*?)</pubDate>', abc_news_doc)

        #printing status
        status_display['text'] = (f"The latest headlines from ABC News (AUS) are: \n {abc_headline[2]} ({abc_headline_date[0]}) \n {abc_headline[3]} ({abc_headline_date[1]}) \n {abc_headline[4]} ({abc_headline_date[2]})")



    elif news_source_status.get() == 'nytimes':
        nytimes_doc = download(nytimes_rss)
        # finding the headline
        nytimes_headline = findall('<title>(.*?)</title>', nytimes_doc)
        # finding the published date
        nytimes_date = findall('<pubDate>(.*?)</pubDate>', nytimes_doc)

        #printing status
        status_display['text'] = (f"The latest headlines from The New York Times (USA) are: \n {nytimes_headline[2]} ({nytimes_date[0]}) \n {nytimes_headline[3]} ({nytimes_date[1]}) \n {nytimes_headline[4]} ({nytimes_date[2]})")
    else:
        pass



#creating a function for print story push button
def print_story_functions():
    # formatting the html file
    news_html = '''
    <!DOCTYPE html>
    <html>
    <head>

    <!-- creating the styles for each news story section, images and the body -->
        <style>
            .headline {
                border: solid 3px black;
                text-align: center;
                padding: 20px;
            }

            img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 500px;
                height: 300px;
            }

            body {background-color: #66a3ff}
        </style>
    </head>

    <body>
    <!-- putting the 'world news' logo -->
        <img src="world_news_500x300.png" class="image_center">

    <!-- the first news headline -->
        <div class="headline">
        <h1>HEADLINE_HERE1</h1>

        <img src="NEWS_IMAGE1">

        <h2>DESCRIPTION_HERE1</h2>

        <h3>NEWS_SOURCE<h3>

        <p>PUB_DATE1</p>
        </div>


    <!-- the second news headline -->
        <div class="headline">
        <h1>HEADLINE_HERE2</h1>

        <img src="NEWS_IMAGE2">

        <h2>DESCRIPTION_HERE2</h2>

        <h3>NEWS_SOURCE<h3>

        <p>PUB_DATE2</p>
        </div>


    <!-- the third news headline -->
        <div class="headline">
        <h1>HEADLINE_HERE3</h1>

        <img src="NEWS_IMAGE3">

        <h2>DESCRIPTION_HERE3</h2>

        <h3>NEWS_SOURCE<h3>

        <p>PUB_DATE3</p>
        </div>
    </body>
    </html>
    '''

    if news_source_status.get() == 'DailyMail':
        daily_mail_doc = download(daily_mail_rss)
        # finding the headline
        daily_mail_headline = findall('<title><!\[CDATA\[(.*?)\]\]><\/title>', daily_mail_doc)
        # finding the published date
        daily_mail_date = findall('<pubDate>(.*?)</pubDate>', daily_mail_doc)
        # finding the description
        daily_mail_desc = findall('<description><!\[CDATA\[(.*?)\]\]><\/description>', daily_mail_doc)
        # finding the image
        daily_mail_img = findall('<media:content type="image\/jpeg" url="([^">]+)"', daily_mail_doc)
        news_source = 'Daily Mail (UK)'

        #replacing elements
        news_html = news_html.replace('HEADLINE_HERE1', daily_mail_headline[1])
        news_html = news_html.replace('NEWS_IMAGE1', daily_mail_img[0])
        news_html = news_html.replace('DESCRIPTION_HERE1', daily_mail_desc[1])
        news_html = news_html.replace('PUB_DATE1', daily_mail_date[0])
        news_html = news_html.replace('HEADLINE_HERE2', daily_mail_headline[2])
        news_html = news_html.replace('NEWS_IMAGE2', daily_mail_img[1])
        news_html = news_html.replace('DESCRIPTION_HERE2', daily_mail_desc[2])
        news_html = news_html.replace('PUB_DATE2', daily_mail_date[1])
        news_html = news_html.replace('HEADLINE_HERE3', daily_mail_headline[3])
        news_html = news_html.replace('NEWS_IMAGE3', daily_mail_img[2])
        news_html = news_html.replace('DESCRIPTION_HERE3', daily_mail_desc[3])
        news_html = news_html.replace('PUB_DATE3', daily_mail_date[2])
        news_html = news_html.replace('NEWS_SOURCE', news_source)

        #creating the html file
        daily_mail_file = open('Latest_stories.html', 'w+')
        daily_mail_file.write(news_html)
        daily_mail_file.close

        #printing status
        status_display['text'] = (f"Stories from 'Daily Mail' (UK) have been printed as a HTML document")



    elif news_source_status.get() == 'ABC':
        abc_news_doc = download(abc_rss)
        # finding the headline
        abc_headline = findall('<title>(.*?)<\/title>', abc_news_doc)
        # finding the published date
        abc_headline_date = findall('<pubDate>(.*?)</pubDate>', abc_news_doc)
        # finding the description
        abc_desc = findall('<description>\s+<!\[CDATA\[(.*)\]]>', abc_news_doc)
        # finding the image
        abc_img = findall('<media:content\s+url=\"(.*)impolicy', abc_news_doc)
        news_source = 'ABC News (AUS)'

        #replacing elements
        news_html = news_html.replace('HEADLINE_HERE1', abc_headline[2])
        news_html = news_html.replace('NEWS_IMAGE1', abc_img[0])
        news_html = news_html.replace('DESCRIPTION_HERE1', abc_desc[0])
        news_html = news_html.replace('PUB_DATE1', abc_headline_date[0])
        news_html = news_html.replace('HEADLINE_HERE2', abc_headline[3])
        news_html = news_html.replace('NEWS_IMAGE2', abc_img[5])
        news_html = news_html.replace('DESCRIPTION_HERE2', abc_desc[1])
        news_html = news_html.replace('PUB_DATE2', abc_headline_date[1])
        news_html = news_html.replace('HEADLINE_HERE3', abc_headline[4])
        news_html = news_html.replace('NEWS_IMAGE3', abc_img[10])
        news_html = news_html.replace('DESCRIPTION_HERE3', abc_desc[2])
        news_html = news_html.replace('PUB_DATE3', abc_headline_date[2])
        news_html = news_html.replace('NEWS_SOURCE', news_source)

        #creating the html file
        abc_file = open('Latest_stories.html', 'w+')
        abc_file.write(news_html)
        abc_file.close

        #printing status
        status_display['text'] = (f"Stories from 'ABC News' (AUS) have been printed as a HTML document")


    elif news_source_status.get() == 'nytimes':
        nytimes_doc = download(nytimes_rss)
        # finding the headline
        nytimes_headline = findall('<title>(.*?)</title>', nytimes_doc)
        # finding the published date
        nytimes_date = findall('<pubDate>(.*?)</pubDate>', nytimes_doc)
        # finding the description
        nytimes_desc = findall('<description>(.*)<\/description>', nytimes_doc)
        # finding the image
        nytimes_img = findall('<media:content height=\"151\" medium=\"image\" url=\"(.*)\" width', nytimes_doc)
        news_source = 'The New York Times (USA)'

        #replacing elements
        news_html = news_html.replace('HEADLINE_HERE1', nytimes_headline[2])
        news_html = news_html.replace('NEWS_IMAGE1', nytimes_img[0])
        news_html = news_html.replace('DESCRIPTION_HERE1', nytimes_desc[1])
        news_html = news_html.replace('PUB_DATE1', nytimes_date[0])
        news_html = news_html.replace('HEADLINE_HERE2', nytimes_headline[3])
        news_html = news_html.replace('NEWS_IMAGE2', nytimes_img[1])
        news_html = news_html.replace('DESCRIPTION_HERE2', nytimes_desc[2])
        news_html = news_html.replace('PUB_DATE2', nytimes_date[1])
        news_html = news_html.replace('HEADLINE_HERE3', nytimes_headline[4])
        news_html = news_html.replace('NEWS_IMAGE3', nytimes_img[2])
        news_html = news_html.replace('DESCRIPTION_HERE3', nytimes_desc[3])
        news_html = news_html.replace('PUB_DATE3', nytimes_date[2])
        news_html = news_html.replace('NEWS_SOURCE', news_source)

        #creating the html file
        nytimes_file = open('Latest_stories.html', 'w+')
        nytimes_file.write(news_html)
        nytimes_file.close

        #printing status
        status_display['text'] = "Stories from 'The New York Times' (USA) have been printed as a HTML document"
    else:
        pass


#creating a function for save story push button
def save_story_functions():
    if news_source_status.get() == 'DailyMail':
        daily_mail_doc = download(daily_mail_rss)
        # finding the headline
        daily_mail_headline = findall('<title><!\[CDATA\[(\w.*?)\]\]><\/title>', daily_mail_doc)
        # finding the published date
        daily_mail_date = findall('<pubDate>(\w.*?)</pubDate>', daily_mail_doc)
        # finding the description
        daily_mail_desc = findall('<description><!\[CDATA\[(\w.*?)\]\]><\/description>', daily_mail_doc)
        # finding the news source
        news_source = 'Daily Mail (UK)'

        #connect to the database
        connection = connect(database = 'world_news.db')
        daily_mail_db = connection.cursor()

        #deleting previous records
        delete_records = ("DELETE FROM interesting_stories")
        daily_mail_db.execute(delete_records)

        #executing INSERT to multiple rows
        multiple_stories = [(news_source, daily_mail_headline[1], daily_mail_date[0], daily_mail_desc[1]),
                            (news_source, daily_mail_headline[2], daily_mail_date[1], daily_mail_desc[2]),
                            (news_source, daily_mail_headline[3], daily_mail_date[2], daily_mail_desc[3])]
        daily_mail_db.executemany("INSERT INTO interesting_stories VALUES (?, ?, ?, ?)", multiple_stories) 
        connection.commit()
        daily_mail_db.close()
        connection.close()

        #printing status
        status_display['text'] = "Successfully saved DailyMail's stories to the sqlite database called 'world_news.db'"



    elif news_source_status.get() == 'ABC':
        abc_news_doc = download(abc_rss)
        # finding the headline
        abc_headline = findall('<title>(\w.*?)<\/title>', abc_news_doc)
        # finding the published date
        abc_headline_date = findall('<pubDate>(\w.*?)</pubDate>', abc_news_doc)
        # finding the description
        abc_desc = findall('<description>\s+<!\[CDATA\[(\w.*)\]]>', abc_news_doc)
        # finding the news source
        news_source = 'ABC News (AUS)'


        #connect to the database
        connection = connect(database = 'world_news.db')
        abc_db = connection.cursor()

        #deleting previous records
        delete_records = ("DELETE FROM interesting_stories")
        abc_db.execute(delete_records)

        #executing INSERT to multiple rows
        multiple_stories = [(news_source, abc_headline[2], abc_headline_date[0], abc_desc[0]),
                            (news_source, abc_headline[3], abc_headline_date[1], abc_desc[1]),
                            (news_source, abc_headline[4], abc_headline_date[2], abc_desc[2])]

        abc_db.executemany("INSERT INTO interesting_stories VALUES (?, ?, ?, ?)", multiple_stories) 
        connection.commit()
        abc_db.close()
        connection.close()

        #printing status
        status_display['text'] = "Successfully saved ABC News's stories to the sqlite database called 'world_news.db'"



    elif news_source_status.get() == 'nytimes':
        nytimes_doc = download(nytimes_rss)
        # finding the headline
        nytimes_headline = findall('<title>(\w.*?)</title>', nytimes_doc)
        # finding the published date
        nytimes_date = findall('<pubDate>(\w.*?)</pubDate>', nytimes_doc)
        # finding the description
        nytimes_desc = findall('<description>(\w.*)<\/description>', nytimes_doc)
        # finding the news source
        news_source = 'New York Times (USA)'

        #connect to the database
        connection = connect(database = 'world_news.db')
        nytimes_db = connection.cursor()

        #deleting previous records
        delete_records = ("DELETE FROM interesting_stories")
        nytimes_db.execute(delete_records)

        #executing INSERT to multiple rows
        multiple_stories = [(news_source, nytimes_headline[2], nytimes_date[0], nytimes_desc[1]),
                            (news_source, nytimes_headline[3], nytimes_date[1], nytimes_desc[2]),
                            (news_source, nytimes_headline[4], nytimes_date[2], nytimes_desc[3])]

        nytimes_db.executemany("INSERT INTO interesting_stories VALUES (?, ?, ?, ?)", multiple_stories) 
        connection.commit()
        nytimes_db.close()
        connection.close()

        #printing status
        status_display['text'] = "Successfully saved ABC News's stories to the sqlite database called 'world_news.db'"
    else:
        pass



#creating find story header
news_sources = LabelFrame(world_news, font = body_font, relief = 'groove',
                                borderwidth = 4, text = 'Find Stories')
news_sources.configure(background = bg_colour)



#creating radio buttons for each news source
#creating variables so user can only select one news source at a time
news_source_status = StringVar()
news_source_status.set(' ')

news_values = ['DailyMail', 'ABC', 'nytimes']


#creating radio button for 'Daily Mail' news
daily_mail_logo = PhotoImage(file = 'daily_mail_600x250.png')
resized_daily_mail_logo = daily_mail_logo.subsample(4, 4)

daily_mail = Radiobutton(news_sources, image = resized_daily_mail_logo,
                                variable = news_source_status, value = news_values[0],
                                command = daily_news_interact)
daily_mail.configure(background = bg_colour)


#creating radio button for 'ABC' news
abc_logo = PhotoImage(file = 'ABC_News_Channel_600x250.png')
resized_abc_logo = abc_logo.subsample(4, 4)


abc_news = Radiobutton(news_sources, image = resized_abc_logo,
                                variable = news_source_status, value = news_values[1],
                                command = abc_news_interact)
abc_news.configure(background = bg_colour)


#creating radio button for 'New York Times' news
ny_times_logo = PhotoImage(file = 'New_York_Times_Logo_600x250.png')
resized_ny_times_logo = ny_times_logo.subsample(4, 4)


ny_times = Radiobutton(news_sources, image = resized_ny_times_logo,
                                variable = news_source_status, value = news_values[2],
                                command = ny_times_interact)
ny_times.configure(background = bg_colour)






# creating 'view story' header
view_story = LabelFrame(world_news, font = body_font, relief = 'groove',
                            borderwidth = 4, text = 'View Stories')
view_story.configure(background = bg_colour)



#creating button for 'show source'
show_source = Button(view_story, font = body_font, text = 'Show source', activeforeground = 'brown',
                        command = show_sources_functions, state = DISABLED)

#creating button for 'show headline'
show_headline = Button(view_story, font = body_font, text = 'Show headline', activeforeground = 'brown',
                        command = show_headline_functions, state = DISABLED)

#creating button for 'Print stories'
print_stories = Button(view_story, font = body_font, text = 'Print stories', activeforeground = 'brown',
                        command = print_story_functions, state = DISABLED)

#creating button for 'Save stories'
save_stories = Button(view_story, font = body_font, text = 'Save stories', activeforeground = 'brown',
                        command = save_story_functions, state = DISABLED)





#creating 'Message' header
message_display = LabelFrame(world_news, font = body_font, relief = 'groove',
                            borderwidth = 4, text = 'Messages')
message_display.configure(background = bg_colour)




#creating label to display status
status_display = Label(message_display, font = status_font,  width = 52, height = 12, 
                            anchor = 'nw', justify = LEFT, wraplength = 470,
                            text = 'Please select a news source...')
status_display.configure(background = bg_colour)



#creating world news logo
world_news_logo = PhotoImage(file = 'world_news_500x300.png')
world_news_embed = Label(world_news, image = world_news_logo)


#putting label frames together
news_sources.grid(pady = 10, padx = 5, row = 0, column = 2, sticky = 'n')
view_story.grid(pady = 10, padx = 5, row = 1, column = 2, sticky = 'n')
message_display.grid(padx = 5, pady = 5, row = 1, column = 0, sticky = 'sw')
world_news_embed.grid(padx = 5, pady = 5, row = 0, column = 0, sticky = 'nw')

#putting widgets together for find stories
daily_mail.grid(row = 0, column = 2, padx = 20, pady = 10)
abc_news.grid(row = 1, column = 2, padx = 20, pady = 10)
ny_times.grid(row = 2, column = 2, padx = 20, pady = 10)

#putting widget together for view story
show_source.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
show_headline.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
print_stories.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
save_stories.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')

#putting widget for messages
status_display.grid(padx = 10, pady = 10, row = 1, column = 0, sticky = 'nw')


#start event loop
world_news.mainloop()