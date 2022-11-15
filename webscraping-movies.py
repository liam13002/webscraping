
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##
table_rows = soup.findAll("tr")


for row in table_rows[1:6]:
    td= row.findAll("td")
    rank = td[0].text
    name = td[1].text
    gross = int(td[7].text.replace('$', '').replace(',',''))
    theaters = int(td[6].text.replace(',',''))
    distributor = td[9].text.rstrip()
    average_gross = format(gross / theaters, ",.2f")
    gross = "$" + format(gross, ",.2f")
    print(rank)
    print(f"Title: {name}")
    print(f"Studio: {distributor}")
    print("Total Gross:", gross)
    print(f"Average Gross: ${average_gross}")
    print()

