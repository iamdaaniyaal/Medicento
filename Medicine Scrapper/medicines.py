from bs4 import BeautifulSoup
# from urllib.request import Request, urlopen
import re
import requests
from medicine_details import Parser2
import time

class Parser:
	def Extractor(self,conditionlink,collection):
		self.link = conditionlink
		# req2 = Request(conditionlink, headers={'User-Agent': 'Mozilla/5.0'})
		# webpage2 = urlopen(req2).read()
		r2 = requests.get(conditionlink)
		soup2 = BeautifulSoup(r2.content, 'html.parser')
		medicines = soup2.find_all('div',{'class': 'panel-body'})
		# ulist_element = medicines.find_all("ul")
		# print(medicines)
		# for med in medicines:
		# 	medicine = med.attrs["href"]
		# 	print(medicine)
		# 	obj2 = Parser2()
		# 	obj2.Extractor(medicinelink = medicine)

		# for medicine in soup2.find("a").attrs["href"]:
		
		# ulist_element = medicines.find("ul")
		# print(ulist_element)
		# 	print(medicine)
		c=0
		for medicine in medicines:
			ulist_element = medicine.find_all("ul")
			for uelement in ulist_element:
				llist_element=uelement.find_all("li")
				for med in llist_element:
					medicine_link=med.find("a").attrs["href"]
					# print(medicine_link)
					c+=1
					obj2 = Parser2()
					# print(collection)
					obj2.Extractor(collection, medicinelink = medicine_link)
					# time.sleep(5)

		print(c)

# obj2 = Parser2()
# obj2.Extractor('Allergies','https://www.netmeds.com/prescriptions/lecet-2-5mg-syrup-60ml')

