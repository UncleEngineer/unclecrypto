#crypto.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def rangeprice(name='bitcoin',start='20200101',end='20200131'):

	url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start={}&end={}'.format(name,start,end)

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')
	table = data.findAll('tr')

	list_days = []
	list_dict = {}
	for row in table[3:]:
		rw = row.findAll('div')
		days = []
		for i,r in enumerate(rw):
			if i > 0 and i < 5:
				days.append(float(r.text.replace(',','')))
			elif i > 4:
				days.append(int(r.text.replace(',','')))
			else:
				days.append(r.text.replace(',',''))

		list_days.append(days)
		list_dict[days[0]] = {'date':days[0],'open':days[1],'high':days[2],'low':days[3],'close':days[4],'volume':days[5],'marketcap':days[6]}

	return (list_days,list_dict)


def dayprice(name='bitcoin',day='20200131'):

	try:
		url = 'https://coinmarketcap.com/currencies/{}/historical-data/?start={}&end={}'.format(name,day,day)

		webopen = req(url)
		page_html = webopen.read()
		webopen.close()

		data = soup(page_html,'html.parser')
		table = data.findAll('tr')

		list_days = []
		list_dict = {}

		for row in table[3:]:
			rw = row.findAll('div')
			days = []
			for i,r in enumerate(rw):
				if i > 0 and i < 5:
					days.append(float(r.text.replace(',','')))
				elif i > 4:
					days.append(int(r.text.replace(',','')))
				else:
					days.append(r.text.replace(',',''))

			list_days.append(days)
			list_dict[days[0]] = {'date':days[0],'open':days[1],'high':days[2],'low':days[3],'close':days[4],'volume':days[5],'marketcap':days[6]}
		list_dict = list_dict[list_days[0][0]]
		list_days = list_days[0]
	except:
		list_days = ['Not Found / Connection Loss']
		list_dict = {'error':'Not Found / Connection Loss'}


	return (list_days,list_dict)


if __name__ == '__main__':
	L,D = rangeprice('xrp',start='20200105',end='20200131')
	print(L)
	print(D)

	L,D = dayprice('bitcoin','20200131')
	print(L)
	print(D)