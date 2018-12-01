import calendar
import time
ticks = time.time() #time intervals are floating point numbers in units of seconds. Particular instants in time are
#expressed in seconds since 12:00am January 1 1970
print("no of ticks since 12:00am January 1 1970 is : " ,ticks)

localtime = time.localtime(time.time())
print(localtime)
localtimeinlocalformat = time.asctime(time.localtime(time.time()))
print(localtimeinlocalformat)

cal = calendar.month(1993,2)
print(cal)
cal = calendar.month(2027,2)
print(cal)

clocktime = time.clock()
print(clocktime)
altzonetime = time.altzone
print("%d" % (altzonetime))
ctime = time.ctime()
print("%s" % (ctime))


print("starting time is %s" % (time.ctime()))
time.sleep(0)
print("ending time is %s" % (time.ctime()))

thisyearcalender=calendar.calendar(2017,w=1,l=1,c=6)
print(thisyearcalender)
weekdaycalender = calendar.firstweekday()
print(weekdaycalender)
leapyearfind = calendar.isleap(2020)
print(leapyearfind)




