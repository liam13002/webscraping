from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.cryptocurrencychart.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}



req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr")

import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = '+14245442887'

myCellPhone = "+16822329322"

for row in table_rows[1:6]:
    td= row.findAll("td")
    
    rank = td[0].text
    name = td[1].text.lstrip().rstrip()
    price = float(td[2].text.replace('$', '').replace(',',''))
    day_change = float(td[4].text.replace('%', '').replace('+', ''))
    yesterday_price = price * (1-(day_change/100))
    

    if name == "Bitcoin (BTC)" and price < 40000:
        message = "The price of Bitcoin has dropped below $40,000"
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)
        print(textmessage.status)

    if name == "Ethereum (ETH)" and price < 3000:
        message = "The Price of Ethereum has dropped below $3000"
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)
        print(textmessage.status)

    price = "$" + format(price, ",.2f")
    day_change = format(day_change, ".2") + "%"
    yesterday_price = "$" + format(yesterday_price, ",.2f")
    print(rank + ":" + name)
    print("Current Price: " + str(price))
    print("24 Hour Change: ", day_change)
    print("Yesterday's Price: ", str(yesterday_price))
    print()



