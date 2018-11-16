from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

# this is the url where we get the dataset to be scraped and analyzed
url = "http://www.hubertiming.com/results/2017GPTR10K"
# url is then passed to the urlopen() function to get the html of the page
html = urlopen(url)

# the next step is to parse the html using bs4

# pass the html object as an argument into the BeautifulSoup() function
# lxml is then used to parse the html
soup = BeautifulSoup(html, 'lxml')

# extract runner data
data = soup.find_all('tbody')
# clean up results by printing only text without html tags
str_data = str(data)
cleantext_tbody = BeautifulSoup(str_data, "lxml").get_text()
print(cleantext_tbody)
