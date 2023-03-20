# datetime: whether `tzinfo` is aware (or not?)
import datetime 
from datetime import timedelta #date, timezone #, datetime
#from zoneinfo import ZoneInfo
import zoneinfo # works well: on py3.11.2


"""
Special thanks to everyone answering on `stackoverflow`
https://stackoverflow.com/questions/2881025/python-daylight-savings-time

"""

utc = "utc"# @"UTC"  
est = "America/New_York" # well-known est region
nowUTC = datetime.datetime.now() # the default :# this is goo but not great ! its subclass .tzinfo == None
# Specify `America/New_York` as an `est` by-product
estInfo = zoneinfo.ZoneInfo(est)
datetimeEst = datetime.datetime.now(tz = estInfo) 
# estStr = "US/Eastern" # syntax: notation is not used i.e. in then Us it is 'America/*; , where * is wild card

# Specify Another Region :
tokyoStr = "Asia/Tokyo"
tokyoInfo = zoneinfo.ZoneInfo(tokyoStr)
dateTokyo = datetime.datetime.now(tz=tokyoInfo)

tzinfo = datetime.datetime.now() # datetime.now().tzinfo # by default it's None (as it's UTC
tzinfo = datetime.datetime.now().tzinfo #  expose timezone's `tzinfo` instead of `datetime.tzinfo()
timetz = datetime.datetime.now().timetz()# can call `timetz()` 
tzname = datetime.datetime.now().tzname() #can also call `tzname() method
dst = datetime.datetime.now().dst() # check `dst` by the `dst()` method in `datetime`



print("tzinfo (naive datetime  datetime.datetime.now() = ",tzinfo)
print("tzinfo aware abstract method: datetime.tzinfo= ",datetime.tzinfo) 
print("timetz(timezone) = ",timetz)
print("tzname= ",tzname)
print("dst = ", dst)
print("tzinfo =", tzinfo)


#DEMO
# 1. naive time (in UTC)
print( f" does a naive `nowUTC` has a class `tzinfo` =  {nowUTC.tzinfo is None}", end='\n') # True


tokyoInfo = zoneinfo.ZoneInfo("Asia/Tokyo")
dateTokyo = datetime.datetime.now(tz=tokyoInfo) #Tokyo())

print("JST,Tokyo: dateTokyo = ",dateTokyo)
estInfo = zoneinfo.ZoneInfo("America/New_York")

    
print("EST: dt.timetz = ", datetime.datetime.now(estInfo)) #datetime.timetz(estInfo) ) # typeError: 'timetz' for 'datetime.datetime' objects doesn't apply to a 'zoneinfo.ZoneInfo' object


def sub(a:datetime.datetime, b : datetime.datetime )-> timedelta:

    return datetime.datetime.fromtimestamp(dt1) - datetime.datetime.fromtimestamp(dt2) #)
    
def makeAware(dt):
    return dt.timetz()

# source: https://help.alteryx.com/developer-help/field-python-class#:~:text=The%20Field%20class%20is%20provided,impact%20field%20types%20and%20metadata.
#Field :  may optionally specify a default value, using normal Python syntax

# The Field class is provided as a reference class to extend the class members of a Field object instantiated within the running Alteryx process.
# Use the methods in the Field class to impact field types and metadata
# 
# There is an in-built function called __dataclass_fields_ that is called on the class object and it returns all the fields the class contains. This method returns a dictionary of all the field information of the object.


# getDataClassFields

def getDataClassFields():

    print("Fields: ", datetime.datetime ) # Research: .__dataclass__) #__dataclass_fields_ )
    
    return datetime.datetime #.__dataclass__ #fields_



# createDatetime : creates a datetime 
def createDatetime(_date=nowUTC , tzinfo = zoneinfo.ZoneInfo(est) ):
    """ PEP431: returns a datetime , generated from a Utc date [default] with a time zone info `tzinfo` """
    
    return datetime.datetime(_date.year, _date.month, _date.day,_date.hour,_date.minute,_date.second , tzinfo =  zoneinfo.ZoneInfo("America/Los_Angeles") ) #zoneinfo.ZoneInfo("America/Los_Angeles"))


def combine(dt):
    _combinedtime = datetime.combine(dt.date() + timedelta(hours= 1), dt.time()) # uses timedelta(1 hour)
    return _combinedtime
    
#1 update Datetime :  -if we have an a timezone aware `datetime`
def updateDatetime(dt, defaultchange = 1): # hint: who told you to change time?
    # only update time in summer 
    """applied datetime date + timedelta """
    #
    naivetime = datetime.datetime.combine(dt.date() + datetime.timedelta(hours= 1), dt.time())
    # mynote: this would keep time in UTC+00:00 [unwanted]
    # we require to move this UTC displacement
    
    return naivetime

#DEMO
#tokyo = Tokyo()
#updateDatetime()
dateTokyo = createDatetime(nowUTC, tokyoInfo)
print("dateTokyo =", dateTokyo)

# updateDatetime

#naivetime

# 1. timezone 
def getTimezone(timezoneStr = utc )-> datetime.timezone:
    _timezone = tokyoInfo #pytz.timezone(timezone)
    return _timezone

#2 naive2local 
def naive2local(dt, timezone = getTimezone("UTC")):
    localtime = createDatetime(dt, timezone) #datetime.fromutc(naivetime) #
    
     #dt.tzinfo.localize(naivetime)
    return localtime


# DEMO

dateFormatting = "%Y-%m-%d %H:%M:%S"
getDataClassFields()

#--------
#def convertToTimezone():
# Date to UTC 
def datetimeToStr( _dateTimewZone , dateFormattring = "%Y-%m-%d %H:%M:%S "): #.%mmm"):

    dateString = "N/A"
    # a better `datetime` with `zone` ewpresentation
    #1. check object if is str already 
    if (type(_dateTimewZone) == str): # type(Zone) should not be equal to `string `str`
        print( _dateTimewZone )
    # else:
        
    #     dateString = dateObjectwZone.isoformat(dateFormatting )
    #dateString = time.strftime( dateformatting )
    # otherwise: Apply the computation process : #TODO: How tostringfy a `datetime` object
    #dateString = datetimeToStr( _dateTimewZone , dateFormattring)
    #Q. how to convert datetime to str ?
    # dateString = str(_dateTimewZone , dateFormattring)
    t =datetime.datetime(_dateTimewZone.year,_dateTimewZone.month, _dateTimewZone.day,
                      _dateTimewZone.hour, _dateTimewZone.minute, _dateTimewZone.second )
    
    #t = datetime.datetime(2012, 2, 23, 0, 0)
    t.strftime(dateFormatting)
    #dateString = _dateTimewZone.strftime(dateFormatting)
    
    #datetime.datetime.fromisoformat(
    return dateString

def strToDatetime(_dateTimewZoneStr , dateFormattring = "%Y-%m-%d %H:%M:%S"): #"%Y-%m-%d %H:%M:%S.%mmm"):
    """ if first argument is string (keep using same formatting), everything runs smoothly """ 
    _dateTimewZone = datetime.datetime.strptime(_dateTimewZoneStr, dateFormatting) # _dateTimwwZone.strptime(

    return _dateTimewZone
#def printDate():
    
#------------  

#from datetime to string datetime

_Datetime = datetime.datetime.strftime(nowUTC, dateFormatting )
strDatetime = strToDatetime(_Datetime)

strDatetime  = strToDatetime(_Datetime, dateFormatting )

print("strDatetime = ", strDatetime)

# from strDatetime to Datetime
# get a UTC date , from string
#nowUTC = datetime.datetime.strptime( strDatetime, dateFormatting )

#timezone
##EST

estTz = getTimezone("EST")
naiveTime = updateDatetime(nowUTC)
localTime = naive2local( nowUTC, naiveTime) # naive to local timezone 


print("new: estTz = ", estTz)

# original time
print("Time UTC NOW: ", nowUTC)
print("local time: ", naiveTime) 

print("local time: ", localTime  ) 

# Datetime-Aware-ness


#2. getAwareDate : requires timezone = getTimezone(utc) # getDST
def getAwareDate( dt , timezone=getTimezone(utc)): #timezone = "UTC" ): #getDst
    """ gets aware Date, from a date, timezone """

    #if datetime is None
    if dt is None:   
        dt  = datetime.utcnow() # date, in utc # any generated date is in UTC (default)

     # Setting a  timezone

    # localize timezone, on the given `datetime`
    timezone_aware_date = createDatetime(dt, tokyoInfo) 
    return timezone_aware_date 

#3. checkIsAware : checks if datetime is aware of `timezone`
def checkIsAware(timezone_aware_date): # this is not dst, but timezone_aware 
    """checks whether a given `datetime` is aware of `timezone` """

    _tzSeconds = timezone_aware_date.dst  #.tzinfo._dst.seconds  #WARNING: TZINFO been removed (the point: check dst time if it has value (other than 0)
    
    isAware = None
    #1. If `timezone is `'s seconds has a zero
    if _tzSeconds == 0:
        isAware = False
    # if timezone is nonzero (different, from UTC) 
    if _tzSeconds != 0: 
        isAware = True #return true
    else: raise ValueError("Unexpected Input: Please Try again, then retry later")

    return isAware
    
#DEMO
#1.get timezone of choice #"UTC"

timezone = getTimezone("UTC") #instead of "America/EST") 
timezone_aware_date = getAwareDate( nowUTC, timezone) #"EST") # recheck 
isAware = checkIsAware( timezone_aware_date)  # either `True` or `False` # checkDst 

print("timezone = ", timezone)
print("timezone_aware_date", timezone_aware_date )
print("isAware = ",isAware)

# IsAware
checkIsAware = checkIsAware( getAwareDate( nowUTC, tokyoInfo ) )  #recheck 
# note: getDst() : fun assumes we have already set up a dst , in the
# so, if no dst,  last funL checkDstL returns None 

"""
1. DST: daylight saving
1.1 check dsk
"""

def daylightSaving(dt, timezone_aware_date):

    #wrong indicator: checks awareness 9NOT DST)  
    isAware = checkIsAware(timezone_aware_date) # checkDst
    isSummer = False
    #check for a dichotomy
     #when it's a summer time (while flag is not, yet) 
    if isAware == True and isSummer == False: # dichotomy
        isSummer= True
        adjustForSummer(dt) # add +01:00 additional hour, added for summer  dt.replace (?)
    elif isAware == False and isSummer == True:
        isSummer = False
        adjustForWinter(dt) # removes +01:00 additional hour added in summer 



def getdiff(dt1, dt2):
    #credits: murgatroid99
    #get the difference as datetime.timedelta object]
    diff = sub(dt1 , dt2) #( #datetime.datetime.fromtimestamp(dt1) - datetime.datetime.fromtimestamp(dt2))
    return diff

# uses time library # unnecessary
def getdiff2(now, then, _formatting ="%a %b %d %H:%M:%S %Y" ):

    import time
    now = time.strftime(_formatting)
    now = datetime.strptime(now, _formatting)
    
    then = time.ctime(os.path.getmtime("x.cache"))
    # customized output 
    tdelta =  - datetime.strptime(then, _formatting)
    return tdelta


def timeAdjust(dt1, dt2 )-> timedelta:

    now = dtt1  #datetime.now()
    then = dt2 #datetime.fromtimestamp(os.path.getmtime("x.cache"))
    tdelta = getdiff(now , then ) #  now - then
    return tdelta 

def adjustForWinter(_date= nowUTC, _tzinfo= tokyoInfo):
    # 00:00: remove one hour 
    pass
def adjustForSummer(_date= nowUTC, _tzinfo= tokyoInfo):
    # +01:00: add one hour
    localize
    pass

def createDatetime(_date=nowUTC , tzinfo = zoneinfo.ZoneInfo(est) ):
    """ PEP431: returns a datetime , generated from a Utc date [default] with a time zone info `tzinfo` """
    
    return datetime.datetime(_date.year, _date.month, _date.day,_date.hour ,_date.minute, _date.second , tzinfo = tzinfo )  # zoneinfo.ZoneInfo("America/Los_Angeles") ) #zoneinfo.ZoneInfo("America/Los_Angeles"))


def is_dst(dt = datetime.datetime.now(), timezone= "UTC"): #None, timezone = "UTC"):

    if dt is None:
        dt = datetime.UTC
        #timezone = pytz.timezone #TODO: add timeinfo for UTC 
        timezone_aware =  createDatetime() #timezone.localize() # replaced with createDatetime 

    return timezone

# Datetime 
#nowUTC = datetime.datetime.now() # .hour

#issue1: datetime has not attribute tz-localize`:

def soln1(startTimeZone= "America/New_York"): #'US/Eastern'):
    #timeinfo.TimeInfo("America/New_York")
    datetime_object_start = datetime.astimezone(timeinfo.TimeInfo(startTimeZone)).isoformat()  #instead of `pytz.timezone('US/Eastern')).isoformat()`
    return datetime_object_start

def soln2(startTimeZone='US/Eastern'):
    """ or use this format """
    datetime_object_start = datetime.astimezone(timeinfo.TimeInfo("America/New_York")).strftime('%m/%d/%y %H:%M:%S')

    return datetime_object_start

dateNow = datetime.datetime.now()
# print(" dateNowZone = datetime.datetime.now( timezone.utc).astimezone()", dateNowZone = datetime.datetime.now( timezone.utc).astimezone() )

#---

# get `EST`

# error : datetime does not have `tz_localize` 
#dt_aware = datetime.datetime.tz_localize('EST', ambiguous='infer')


def isTzNaive(dt, errorMsg="Unexpected value encountered"):
    """
    checks if datetime is `tzinfo` naive
    """
    _naive = True 

    if dt.tzinfo == None:
        pass
    elif dt.tzinfo != None:
        _naive = False
    else:
        raise ValueError(errorMsg)
    return _naive

#end of time zone (tz) (using `ZoneInfo`)

# DST manipulation

# import pytz # depreciate : 1. erroneous 2. slow  3.built-in replacement exists
def is_date_of_DSTtransition(dt: datetime, zone) -> bool: #preferred
    
    #_d = $pytz.timezone(zone).localize(
        #TYPEERROR: combine() argument 2 must be datetime.time, not str  
      # _d = datetime.datetime.combine(dt.date(), zone ) #time.min)
        _d = createDatetime(dt.date(), zone ) 
        #TODO: fine
        # datetime.timedelta(hours = 1) #TODO: implement this 
        
        return _d.dst() != pytz.timezone(zone).normalize(_d+timetz(1)).dst()
"""
for d in range(366):
    if is_date_of_DSTtransition(datetime.datetime(2021, 1, 1) + datetime.timedelta(d), "Europe/Berlin"):
        print((datetime(2021, 1, 1) + timedelta(d)).date())
"""
# 2021-03-28
# 2021-10-31


# 1. using Ambigous (DST)

def is_date_of_DSTtransition(dt: datetime, zone: str) -> bool:
    """
    check if the date part of a datetime object falls on the date
    of a DST transition.
    """
    _d = datetime.combine(dt.date(), time.min).replace(tzinfo=ZoneInfo(zone))
    return _d.dst() != (_d+timedelta(1)).dst()

def toTzAware(dt,startTimeZone='EST'): # preferred (but ambigous inference ) 
    """ convertz `naive` datetime to an aware, adding a startTimezone`
    a 3 captial letter word XXX ,a string indicating current timezone  
    """
    dt_aware = datetime.datetime.now()
    if isTzNaive(dt) is False:
        dt_aware = dt.datetime.tz_localize(startTimeZone, ambiguous = 'infer')
    return dt_aware



dateUtc = datetime.datetime.now()
dateUtc.year
#dst setUp :
#Hint: dst is `fold` oriented : as we are either on a
## otherwwise : check_Dst returns None ( if country does not use a DST ) - based on the `timezoneInfo`

# Using (non-amboigous) DST   
def getDateDst(dateTime = dateUtc, timeZone =tokyoInfo  ): # DST is fold-Oriented

    dtDst = datetime.datetime(year=dateTime.year, month = dateTime.month, day = dateTime.day,
                      hour= dateTime.hour, minute = dateTime.minute, second = dateTime.second,
                      microsecond= dateTime.microsecond, fold = 0, tzinfo = timeZone ) # fold affects date
    return dtDst



# Demo:  getDateDst
estInfo = zoneinfo.ZoneInfo(est)
 
dateEst = datetime.datetime.now(tz = estInfo)

dateEstwDst = getDateDst(dateEst, timeZone = estInfo ) # getDateDst # estDst

dateTokyo = datetime.datetime.now(tz = tokyoInfo)
print("date tokoyo w/ Daylight DST",dateTokyo)

dateTokyoDst = getDateDst(dateEst, timeZone = estInfo ) # getDateDst # estDst
getDateDst(dateTokyo, timeZone = tokyoInfo )
print("date EST w/ Daylight DST", dateEstwDst)


# 2. timezone Aware-nes 
awareDate = ( getAwareDate(( dateEstwDst ) )) # estDst) #ok #isEstDstAware

print("awareDate = ", awareDate ) 
isAware = checkIsAware

print("isthe Dst time Aware = ", isAware) #isEstDstAware) #isDistEst)
#print("isDst = ", isEstAware #isDistEst)


#print("EstDst = ", estDst) # dateEst

#  Fold (DST ) 
# fold = 1 #error no such thing: parameter: dateTime (outside scope of function 
dtDstNoFold = datetime.datetime(year=dateEst.year, month = dateEst.month, day = dateEst.day,
                      hour= dateEst.hour, minute = dateEst.minute, second = dateEst.second,
                      microsecond= dateEst.microsecond, fold = 0, tzinfo = estInfo )

# fold = 2

dtDstFold = datetime.datetime(year=dateEst.year, month = dateEst.month, day = dateEst.day,
                      hour= dateEst.hour, minute = dateEst.minute, second = dateEst.second,
                      microsecond= dateEst.microsecond, fold = 1, tzinfo = estInfo )



print("dtDstFold = ", dtDstNoFold)

print("dtDstFold = ", dtDstFold)

#TODO: add 1 hour , sub 1 hour 
