from bs4 import BeautifulSoup,SoupStrainer
# from urllib.request import Request, urlopen
import requests
import re
from medicines import Parser
import time
url = 'https://www.netmeds.com/prescriptions'

# webpage = urllib.request.urlopen(url)

# soup = BeautifulSoup(webpage, 'html.parser')

# for cat in soup.findAll('a', attrs={'class': "alpha-drug-list"}):
#     print(question.get_text())                     


# req = Request('https://www.netmeds.com/prescriptions', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()


# soup = BeautifulSoup(webpage, 'html.parser')
# con = []
r = requests.get(url)
# strainer = SoupStrainer(class_ = "alpha-drug-list")
soup = BeautifulSoup(r.content,'html.parser')
# count=0
# for cat in soup.findAll('a', attrs={'href': re.compile("^https://www.netmeds.com/prescriptions/[A-Za-z]")}):
#     print(cat.get('href'))
#     count +=1
conditions = soup.find_all("ul", {'class':'alpha-drug-list'})


# for condition in conditions:
# 	list_element = condition.find_all("li")
# 	for element in list_element:
# 		condition_link=element.find("a").attrs["href"]
# 		# print(condition_link)
# 		obj = Parser()
# 		obj.Extractor(conditionlink = 'https://www.netmeds.com/prescriptions/allergies')
# 		time.sleep(240)
collection_name = ''  #Put medicine category here
obj = Parser()
obj.Extractor(conditionlink = 'https://www.netmeds.com/prescriptions/ulcer-reflux-flatulence', collection = collection_name)

	
