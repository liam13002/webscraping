import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapter = random.randint(1,21)

if chapter < 10:
    chapter = "0" + str(chapter)
else:
    chapter = str(chapter)

webpage = 'https://ebible.org/asv/JHN'+ chapter +".htm"

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll("div", class_='main')

#print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split('.')

#print(verse_list)

my_verse = random.choice(verse_list[:len(verse_list)-5])

#print(f"Chapter: {chapter}, Verse: {my_verse}")

message = "Chapter:" + chapter + " Verse: " + my_verse
print(message)

import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = '+14245442887'

myCellPhone = "+16822329322"

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)

print(textmessage.status)