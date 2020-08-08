#This python program imports file from exported bookmarks(a html file)
#currently it can sort only bookmarks saved in ENG language
#BeautifulSoup is a external library used to handle the tags
from bs4 import BeautifulSoup
import re
import sys
import os

try:
    file = input("\n Enter the location of your exported BOOKMARK file (like D:\Documents\exported-bookmarks.html): \n -> ")
    filehandler = open(file,encoding="utf8")
except:
    print("\n Error while openning the file")
    input("\n\n\t\t\t\tPress Enter key to Exit.")
    sys.exit()

bookmarkFileName = input("\n Enter the filename for the bookmark: \n -> ")
soup = BeautifulSoup(filehandler,"html.parser")

htmlTags = soup('a')

class HtmlClass:
    #the class which stores both href and content of Anchor element
    rawBookmarkLists = list()
    rawBookmarkListsHref = list()

htmlClassOject = HtmlClass()

for tag in htmlTags:
    #contentString = re.sub(r'[^\x00-\x7F]+',' ', tag.contents[0])
    htmlClassOject.rawBookmarkLists.append(tag.contents[0])
    newUrl = tag.get('href', None)
    htmlClassOject.rawBookmarkListsHref.append(newUrl)

sortedBookmarkList = list()

dictTotal = dict()
for lstItems in range(len(htmlClassOject.rawBookmarkLists)):
    dictTotal[htmlClassOject.rawBookmarkListsHref[lstItems]]  = htmlClassOject.rawBookmarkLists[lstItems]

sortedBookmarkList = sorted(dictTotal.items(), key = lambda value: value[1])

folder =  os.path.join("C:",os.environ["HOMEPATH"], "Desktop")
stringName = bookmarkFileName + ".html"
path = folder + "/" + stringName
HtmlFile = open(path,"w")

HtmlFile.write("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <title> """+ stringName +"""</title>
                    <style>
                        a{
                            padding:2px;
                            margin:2px;
                            text-decoration:none;
                            color: #4d0066;
                            }
                            a:hover{
                            color: #FFF;
                            background-color:#4d0066
                        }
                    </style>
                </head>
                <body>
                    <h2>Sorted bookmark list:</h2>
                """)

for value, key in sortedBookmarkList:
    try:
        HtmlFile.write("""
        <a href=""" + value + " target=" + "_blank" +" title="+ value + ">" + key + "</a></br>")
    except Exception as e:
        HtmlFile.write("<h4>ERROR: HTML displays only unicode format</h4>")

HtmlFile.write("""
                </body>
                </html>
            """)

HtmlFile.close()
print("\n Your bookmarks are successfully sorted!")
print("\n " + bookmarkFileName + ".html is created in: {}".format(folder))

input("\n\n\t\t\t\tPress Enter key to Exit.")
