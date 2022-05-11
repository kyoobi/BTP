import sys,os
import django
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()
from swag.models import CSV
import csv, datetime
from datetime import timedelta

start_date = datetime.date(2022,5,1)
start_time = datetime.time(0,0)
end_date = datetime.date.today()
dt = datetime.datetime.combine(start_date,start_time)
while(dt.date() != end_date):
	year = dt.date().year
	month = dt.date().month
	day = dt.date().day
	link = "static/SLDC_Data/"+str(year)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2)+"-"+str(month).zfill(2)+"-"+str(year)+".csv"
	try:
		print(day,month,year);
		dataReader = csv.reader(open(link), delimiter=',', quotechar='"')
		ip=0
		for row in dataReader:
			print("q",ip)
			ip += 1
			sp = row[0].split(':')
			tim = datetime.time(int(sp[0]),int(sp[1]))
			while(tim != dt.time()):
				print(tim, (dt.time()))
				print("w")
				results=[]
				results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
				if (len(results[0]) == 0):
					data = CSV.objects.create(timestamp = str(dt.time()), load_value = None, date = dt.date())
				dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))

			results=[]
			results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
			if (len(results[0]) == 0):
				data = CSV.objects.create(timestamp = row[0], load_value = row[1], date = dt.date())
			dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))
			print(",,,,",dt.time())

		if(dt.time() != datetime.time(0,0)):
			print("in")
			results=[]
			results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
			if (len(results[0]) == 0):
				
				data = CSV.objects.create(timestamp = str(dt.time()), load_value = None, date = dt.date())
				
			while(str(datetime.time(23,55)) != str(dt.time())):
				print("e")
				dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))
				results=[]
				results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
				if (len(results[0]) == 0):
					data = CSV.objects.create(timestamp = str(dt.time()), load_value = None, date = dt.date())
			dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))

	except Exception as e:
		results=[]
		results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
		if (len(results[0]) == 0):
			data = CSV.objects.create(timestamp = str(dt.time()), load_value = None, date = dt.date())
		while(str(dt.time()) != '23:55:00'):
			print("r")
			dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))
			results=[]
			results.append(CSV.objects.filter(date = dt.date(), timestamp = str(dt.time())))
			if (len(results[0]) == 0):
				data = CSV.objects.create(timestamp = str(dt.time()), load_value = None, date = dt.date())
		dt = (datetime.datetime.combine(dt.date(),dt.time())+timedelta(minutes=5))
		print(e)
