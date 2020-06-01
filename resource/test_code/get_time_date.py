import datetime

yestoday = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
today = datetime.date.today().strftime('%Y-%m-%d')
hours_now = datetime.datetime.now().strftime('%H')
print('hours_now: '+hours_now)
if int(hours_now)>=0 and int(hours_now)<5 :
    print(yestoday)
else:
    print(today) 
