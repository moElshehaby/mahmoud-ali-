import requests
import bs4
url = "https://cairosales.com/ar/small-appliances/coffee-maker/?n=225"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, "html.parser")
list = soup.find_all('div', {'class': 'product-container'})
for item in list:
	print(item.find('a', {'class': 'product-name'}).text)
	if item.find('span', {'class': 'price product-price'}) == None:
		print("price not determine ")
	else:
		print(item.find('span', {'class': 'price product-price'}).text)