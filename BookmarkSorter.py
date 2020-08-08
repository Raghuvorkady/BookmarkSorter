#This python program imports file from exported bookmarks(a html file)
#currently it can sort only bookmarks saved in ENG language
#BeautifulSoup is a external library used to handle the tags
from bs4 import BeautifulSoup
from operator import itemgetter, attrgetter, methodcaller
import string
import re
import sys
import os

# define the name of the directory to be created

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
    listForBookmarkDict = list()

htmlClassOject = HtmlClass()

for tag in htmlTags:
    #contentString = re.sub(r'[^\x00-\x7F]+',' ', tag.contents[0])
    htmlClassOject.rawBookmarkLists.append(tag.contents[0])
    newUrl = tag.get('href', None)
    htmlClassOject.rawBookmarkListsHref.append(newUrl)

"""print(htmlClassOject.rawBookmarkLists)
print(htmlClassOject.rawBookmarkListsHref)"""

"""firstLetterCaps = list(string.ascii_uppercase)
firstLetterSmall = list(string.ascii_lowercase)"""

"""bookmarkDict = dict()
listForBookmarkDict = list()"""

def printBookmarks():
    i = 0
    sum = 0
    stringName = bookmarkFileName + ".html"
    HtmlFile = open(stringName,"w")
    for letter in range(len(firstLetterCaps)):
        for eachValue in bookmarkDict[letter]:
            i = i + 1
            sum = sum + 1
            lineString = "\n===============================================================================\n"

            eachValue = re.sub(r'[^\x00-\x7F]+',' ', eachValue)
            string = " " + str(firstLetterCaps[letter]) + "- Bookmarks["+ str(i) + "]: " +  str(eachValue)
            try:
                HtmlFile.write(string)
                HtmlFile.write("<br/>")
            except Exception as e:
                HtmlFile.write("<br/>")
                HtmlFile.write("<h3>ERROR: Encoding Error</h3>")
                HtmlFile.write("<br/>")
            print(string)
        print("\n\tTotal Bookmarks in", firstLetterCaps[letter] ,"folder are:", i)
        i = 0
        print(lineString)

        HtmlFile.write("<br/>")
        HtmlFile.write(lineString)
        HtmlFile.write("<br/>")
    HtmlFile.close()
    totalBookmarks = sum
    print("Your total Bookmarks are:", totalBookmarks)

"""for iterator in range(len(firstLetterCaps)):
    for item in htmlClassOject.rawBookmarkLists:
        if item.startswith(firstLetterSmall[iterator]) or item.startswith(firstLetterCaps[iterator]):
            htmlClassOject.listForBookmarkDict.append(item)
    htmlClassOject.listForBookmarkDict.sort()
    bookmarkDict[iterator] = htmlClassOject.listForBookmarkDict
    htmlClassOject.listForBookmarkDict = list()"""

lstContent = list()
lstHref = list()
lstTotal = list()

dictTotal = dict()
for lstItems in range(len(htmlClassOject.rawBookmarkLists)):
    lstContent = htmlClassOject.rawBookmarkLists[lstItems]
    lstHref = htmlClassOject.rawBookmarkListsHref[lstItems]
    dictTotal[lstHref]  = lstContent
lstTotal.append(dictTotal)

sort_orders = sorted(dictTotal.items(), key = lambda value: value[1])

"""for key, value in sort_orders:
	print("CONTENT: ", key," HREF: " ,value)"""

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
}</style>
</head>
<body>
<h2>Sorted bookmark list:</h2>""")

for value, key in sort_orders:
    try:
        HtmlFile.write("""
        <a href=""" + value + " target=" + "_blank" +" title="+ value + ">" + key + "</a></br>")
    except Exception as e:
        #HtmlFile.write("<br/>")
        HtmlFile.write("<h4>ERROR: HTML displays only unicode format</h4>")
        #HtmlFile.write("<br/>")

HtmlFile.write("""
</body>
</html>
""")

HtmlFile.close()
print("\n Your bookmarks are successfully sorted!")
print("\n " + bookmarkFileName + ".html is created in: {}".format(folder))

#printBookmarks()
input("\n\n\t\t\t\tPress Enter key to Exit.")
