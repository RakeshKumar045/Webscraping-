#import the library used to query a website
import urllib.request #if you are using python3+ version, import urllib.request
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki) #For python 3 use urllib.request.urlopen(wiki)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

#Use function “prettify” to look at nested structure of HTML page
print(soup.prettify())

#Return content between opening and closing tag including tag
print(soup.title)

#Return string within given tag
print(soup.title.string)

#Find all the links within page’s <a> tags
print(soup.find_all("a"))

#iterate over each a tag and then return the link using attribute “href” with get.
all_links = soup.find_all("a")
for link in all_links:
	print(link.get("href"))


right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
print(right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))


 #import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

print(df)