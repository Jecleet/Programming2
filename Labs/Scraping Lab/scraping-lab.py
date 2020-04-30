import time
import urllib.request
import certifi
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

twit_url = "https://twitter.com/oprah?lang=en"

#driver = webdriver.Chrome("/Users/james/PycharmProjects/P2_SP20/Labs/Scraping Lab/chromedriver")
#driver.implicitly_wait(10)
#driver.get(twit_url)
#Honestly I have no idea how to do this sorry.


# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()
url = "https://weather.com/weather/tenday/l/52189489abd4a1f10e4c5ee187dd6cdd3f761e42b8725e88dc42aacab98587ac"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

title = soup.find("title")
print(title.text)
#print(soup.prettify())


days = soup.find_all(headers="day")
high_low = soup.find_all(headers="hi-low")
descriptions = soup.find_all(headers= "description")
precip = soup.find_all(headers= "precip")
wind = soup.find_all(headers= "wind")

print(precip)

for i in range(len(wind)):
    print("On ", days[i].text, end="")
    print(" the weather will be", descriptions[i].text, end="")
    #print("There will be a high and low of", high_low[i].text) I have no idea why this doesn't work
    print(", have a rain chance of", precip[i].text, end="")
    print(", and has a wind speed of", wind[i].text)
