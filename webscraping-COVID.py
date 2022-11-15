# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)



from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}



req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr")

state_worst_death = ''
state_best_death = ''
state_worst_test = ''
state_best_test = ''
high_death_ratio = 0.0
low_death_ratio = 100.0
high_test_rate = 0.0
low_test_rate = 100.0

for row in table_rows[2:52]:
    td= row.findAll("td")
    state = td[1].text
    cases = int(td[2].text.replace(",",""))
    deaths = int(td[4].text.replace(",",""))
    tests= int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))
    death_rate = round((deaths/cases)*100, 2)
    test_rate= round((tests / population)*100,2)
    if death_rate > high_death_ratio:
        high_death_ratio = death_rate
        state_worst_death = state
    
    if death_rate < low_death_ratio:
        low_death_ratio = death_rate
        state_best_death = state

    if test_rate > high_test_rate:
        high_test_rate = death_rate
        state_worst_test = state
    
    if test_rate < low_test_rate:
        low_test_rate = test_rate
        state_worst_test = state

    print(state)
    print(death_rate)
    print(test_rate)
    print()

print("Best Death Rate: "+ state_best_death, " ", low_death_ratio, "%")
print("Worst Death Rate: "+ state_worst_death, " ", high_death_ratio, "%")
print("Best Test Rate: "+ state_best_test, " ", high_test_rate, "%")
print("Worst Test Rate: " + state_worst_test, " ", low_test_rate, "%")

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

