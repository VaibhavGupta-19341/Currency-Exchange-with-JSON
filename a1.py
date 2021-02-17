# Name : Vaibhav Gupta
# Roll No : 2019341
# Group : 9

import datetime
import urllib.request

def getLatestRates():
	"""
	Returns: a JSON string that is a response to a latest rates query.

	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	url1 = urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
	data1 = str(url1.read())

	return data1

def changeBase(amount, currency, desiredCurrency, date):
	"""
	Outputs: a float value f.
	"""
	assert date >= '1999-01-05' , "Date out of scope!! Please try again"
	assert date <= str(datetime.date.today()), "Date out of scope!! Please try again"
	url2 = urllib.request.urlopen("https://api.exchangeratesapi.io/"+date)
	data2 = str(url2.read())

	currency = currency.upper()
	desiredCurrency = desiredCurrency.upper()


	assert currency in data2,currency + " Not found!! Please try again"
	assert desiredCurrency in data2,desiredCurrency + " Not found!! Please try again"

	if desiredCurrency == 'EUR':
		rate_dc=1
	else:
		dc=int(data2.find(desiredCurrency))
		cut2=int(data2.find(',',dc))

		if data2[cut2-1]=='}':
			rate_dc = float(data2[dc + 5:cut2-2])
		else:
			rate_dc= float(data2[dc + 5:cut2])

	if currency == 'EUR':
		cost=amount*rate_dc
	else:
		c = int(data2.find(currency))
		cut1 = int(data2.find(',', c))

		if data2[cut1-1]=='}':
			rate_c = float(data2[c + 5:cut1-2])
		else:
			rate_c= float(data2[c + 5:cut1])

		cost=amount/(rate_c/rate_dc)

	return cost

def printAscending(json):
	"""
	Output: the sorted order of the Rates
	You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
	json=json[:-36] +','+json[-36:]
	if 'CAD' in json:
		c = int(json.find('CAD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		canada=[rate,'CAD']

	if 'HKD' in json:
		c = int(json.find('HKD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		Hong_Kong=[rate,'HKD']

	if 'ISK' in json:
		c = int(json.find('ISK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		iceland=[rate,'ISK']

	if 'PHP' in json:
		c = int(json.find('PHP'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		philippines=[rate,'PHP']

	if 'DKK' in json:
		c = int(json.find('DKK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		denmark=[rate,'DKK']

	if 'HUF' in json:
		c = int(json.find('HUF'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		hungary=[rate,'HUF']

	if 'CZK' in json:
		c = int(json.find('CZK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		czechia=[rate,'CZK']

	if 'AUD' in json:
		c = int(json.find('AUD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		australia=[rate,'AUD']

	if 'RON' in json:
		c = int(json.find('RON'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		romania=[rate,'RON']

	if 'SEK' in json:
		c = int(json.find('SEK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		sweden=[rate,'SEK']

	if 'IDR' in json:
		c = int(json.find('IDR'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		indonesia=[rate,'IDR']

	if 'INR' in json:
		c = int(json.find('INR'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		india=[rate,'INR']

	if 'BRL' in json:
		c = int(json.find('BRL'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		brazil=[rate,'BRL']

	if 'RUB' in json:
		c = int(json.find('RUB'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		russia=[rate,'RUB']

	if 'HRK' in json:
		c = int(json.find('HRK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		croatia=[rate,'HRK']

	if 'JPY' in json:
		c = int(json.find('JPY'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		japan=[rate,'JPY']

	if 'THB' in json:
		c = int(json.find('THB'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		thailand=[rate,'THB']

	if 'CHF' in json:
		c = int(json.find('CHF'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		switzerland=[rate,'CHF']

	if 'SGD' in json:
		c = int(json.find('SGD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		singapore=[rate,'SGD']

	if 'PLN' in json:
		c = int(json.find('PLN'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		poland=[rate,'PLN']

	if 'BGN' in json:
		c = int(json.find('BGN'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		bulgaria=[rate,'BGN']

	if 'TRY' in json:
		c = int(json.find('TRY'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		turkey=[rate,'TRY']

	if 'CNY' in json:
		c = int(json.find('CNY'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		china=[rate,'CNY']

	if 'NOK' in json:
		c = int(json.find('NOK'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		norway=[rate,'NOK']

	if 'NZD' in json:
		c = int(json.find('NZD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		New_Zealand=[rate,'NZD']

	if 'ZAR' in json:
		c = int(json.find('ZAR'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		South_Africa=[rate,'ZAR']

	if 'USD' in json:
		c = int(json.find('USD'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		USA=[rate,'USD']

	if 'MXN' in json:
		c = int(json.find('MXN'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		mexico=[rate,'MXN']

	if 'ILS' in json:
		c = int(json.find('ILS'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		israel=[rate,'ILS']

	if 'GBP' in json:
		c = int(json.find('GBP'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		UK=[rate,'GBP']

	if 'KRW' in json:
		c = int(json.find('KRW'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		South_Korea=[rate,'KRW']

	if 'MYR' in json:
		c = int(json.find('MYR'))
		cut = int(json.find(',', c))
		rate = float(json[c + 5:cut])
		malaysia=[rate,'MYR']

	countries=[canada,Hong_Kong,iceland,philippines,denmark,hungary,czechia,australia,romania,sweden,indonesia,india,brazil,russia,croatia,japan,thailand,switzerland,singapore,poland,bulgaria,turkey,china,norway,New_Zealand,South_Africa,USA,mexico,israel,UK,South_Korea,malaysia]
	coun=sorted(countries,key=lambda x : x[0])
	for i in coun:
		print('1 Euro = '+str(i[0])+' '+str(i[1]))

def extremeFridays(startDate, endDate, currency):
	"""
	Output: on which friday was currency the strongest and on which was it the weakest.
	You don't have to return anything.
		
	Parameters: 
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	"""
	url3 = urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at=" + startDate + "&end_at=" + endDate)
	data3 = str(url3.read())
	currency = currency.upper()
	assert startDate >= '1999-01-05', "startDate out of scope!! Please try again"
	assert endDate <= str(datetime.date.today()), "endDate out of scope!! Please try again"
	assert currency != 'EUR',"Search for some other currency because Euro is used as a basis"
	assert currency in data3, currency + " Not found!! Please try again"

	fridays = []
	rates = []

	f = data3.find(':')
	j = e = data3.find(':', f + 1)
	dates = [datetime.datetime.strptime(data3[f + 3:e - 1],"%Y-%m-%d")]
	for i in data3:
		r = data3.find('}', j)
		t = data3.find(':', r)
		if data3[r + 3:t - 1] == '\"start_at':
			break
		dates.append(datetime.datetime.strptime(data3[r + 3:t - 1],"%Y-%m-%d"))
		j = t + 1

	for i in dates:
		if i.weekday()==4:
			fridays.append(i.strftime("%Y-%m-%d"))

	for i in fridays:
		j=int(data3.find(i))
		c = int(data3.find(currency,j))
		cut = int(data3.find(',', c))
		if data3[cut-1]=='}':
			r = float(data3[c + 5:cut-2])
		else:
			r= float(data3[c + 5:cut])
		rates.append([r,i])

	l=len(rates)
	extreme=sorted(rates,key=lambda x : x[0])
	print(currency + ' was strongest on ' + str(extreme[0][1]) + '. 1 Euro was equal to ' + str(extreme[0][0]) +' '+ currency )
	print(currency + ' was weakest on ' + str(extreme[l-1][1]) + '. 1 Euro was equal to ' + str(extreme[l-1][0]) +' '+ currency)

def findMissingDates(startDate, endDate):
	"""
	Output: the dates that are not present when you do a json query from startDate to endDate
	You don't have to return anything.

	Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""
	assert startDate >= '1999-01-05', "startDate out of scope!! Please try again"
	assert endDate <= str(datetime.date.today()), "endDate out of scope!! Please try again"
	url3 = urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at=" + startDate+"&end_at=" + endDate)
	data3 = str(url3.read())

	f=data3.find(':')
	j=e=data3.find(':',f+1)
	date_p=[data3[f+3:e-1]] #first currency
	for i in data3:
		r=data3.find('}',j)
		t=data3.find(':',r)
		if data3[r+3:t-1] == '\"start_at':
			break
		date_p.append(data3[r+3:t-1]) #following currencies
		j=t+1

	start = datetime.datetime.strptime(startDate,"%Y-%m-%d")
	end = datetime.datetime.strptime(endDate,"%Y-%m-%d")
	date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days + 1)]

	date_l=[]

	for date in date_generated:
		date_l.append(date.strftime("%Y-%m-%d"))

	print('The following dates were not present:')
	for i in date_l:
		if i not in date_p:
			print(i)

