from bs4 import BeautifulSoup
import re
import requests
# from mdbinsert import Insertition
from pymongo import MongoClient
client = MongoClient()
db = client.netmeds

class Parser2:
	def Extractor(self, collection ,medicinelink):
		self.link = medicinelink
		try:
			r3 = requests.get(medicinelink)
			soup3 = BeautifulSoup(r3.content, 'html.parser')
			medicine_name = soup3.find_all("h1", {'class':'page-title'})
			name = " "
			try:
				for mn in medicine_name:
					name = mn.find("span").text
					print(name)
			except:
				name = ' NA '


			medicine_comp = soup3.find("div", {'class':'col-sm-12 padding-r-none'})
			# for mc in medicine_comp:
			# 	# comp = mc.find("a")
			# 	# for c in comp:
			# 	# 	composition = c.find("span", {'class':'gen_name'})
			# 	# 	print(composition)
			# 	element = mc.find("span", {'class':'gen_name'})
			# 	composition = element.replace_with('')
			# 	print(composition)
			# composition = medicine_comp.find("a")
			try:
				composition = medicine_comp.find("span",{'class':'gen_name'}).text
			except:
				composition = ' NA '
			# composition2=composition1.unwrap()
			# print(composition2)
			# for tag in medicine_comp.find_all("span",{'class':'gen_name'}):
			# 	composition = tag.replace_with('')
			# print(composition)
			try:
				manufacturer = soup3.find("a",  {'class':'p_manuf'}).text
				# print(manufacturer)
			except :
				manufacturer = ' NA '
				# print(manufacturer)
				
			try:
				price = soup3.find("span", {'class':'price'}).text
			except:
				price = ' NA '
			# price = price[3:]
			# price=float(price)
			# print(price)
			print()

			# obj3 = Insertition()
			# obj3.insert_document(collection,name,composition,manufacturer,price)
			insert_document(collection,name,composition,manufacturer,price)

		# except requests.exceptions.ConnectionResetError:
		# 		print("handle exceptions")

		except requests.exceptions.ConnectionError:
				print('handle exceptions')

def insert_document(collection,name,composition,manufacturer,price):
		collection_nm = collection
		collection= db[collection_nm]
		# print(collection)
		# medicine = {"name":name, "composition":composition, "manufacturer": manufacturer, "price": price}
		# medicine["name"] = name
		# medicine["composition"] = composition
		# medicine["manufacturer"] = manufacturer
		# medicine["price"] = price
		# print(medicine)
		collection.insert_one({"name":name, "composition":composition, "manufacturer": manufacturer, "price": price})
				

			