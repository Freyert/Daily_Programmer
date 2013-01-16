#Date Conversions	
__kin = 1
__uinal = 20
__tun = 18 * 20
__katun = 20 * 18 * 20
__baktun = 20 * 20 * 18 * 20



def __year_to_days__(y):
	return 365*y + y/4 - y/100 + y/400

def __month_to_days__(m):
		return (m*306 + 5)/10


#Calculates total days since March 1, 0 AD
#Credit: http://alcor.concordia.ca/~gpkatch/gdate-method.html
def total_days(y,m,d):
	m = (m+9)%12
	y = y-m/10

	return __year_to_days__(y) + __month_to_days__(m) + (d-1)



def __year_from_days__(d):
	return(10000*d +14780)/3652425

#Calculates date from number of days, using March 1, 0 AD as base year.
#Credit: http://alcor.concordia.ca/~gpkatch/gdate-method.html
def date_from_number_of_days(d):
	y = __year_from_days__(d)
	ddd = d -__year_to_days__(y)
	if(ddd<0):
		y = y- 1
		ddd = __year_to_days__(y)
	mi = (100*ddd + 52)/3060
	mm = (mi + 2)%12 + 1
	y = y + (mi+2)/12
	dd = ddd - (mi*306 +5)/10 + 1
	return (y, mm, dd)

#Calculates Mayan Longcount
def long_count(y, m, d):
	BC_days = total_days(3112, 9, 20) #August 11, 3114 BC Gregorian, with some tweaking.
	AD_days = total_days(y,m,d)
	
	all_the_days = BC_days + AD_days	
	
	baktuns = all_the_days/__baktun
	remainder = all_the_days%__baktun
	katuns = remainder/__katun
	remainder = remainder%__katun
	tuns = remainder/__tun
	remainder = remainder%__tun
	uinals = remainder/__uinal
	kins = remainder%__uinal 

	return (baktuns, katuns, tuns, uinals, kins)

#Calculates the Gregorian Calendar date from Mayan longcount.
def inv_longcount(baktuns, katuns, tuns, uinals, kins):
	days = baktuns * __baktun + katuns * __katun + tuns * __tun + uinals * __uinal + kins
	return date_from_number_of_days(days)



#User input section
def read_user_input():
	count = int(raw_input('How many lines shall I read?  '))
	lines = []
	print "Please enter all dates in this format: day month year i.e.: 1 1 1970"
	while(count > 0):
		lines.append(raw_input('Date {0} '.format(count)))
		count = count - 1

	return lines

def parse_user_input(lines):
	dates = []
	for item in lines:
		dates.append(item.split())
	return dates

user_dates = parse_user_input(read_user_input())
for date in user_dates:
	print "{0}.{1}.{2}.{3}.{4}".format(*long_count(int(date[2]), int(date[1]), int(date[0])))	

