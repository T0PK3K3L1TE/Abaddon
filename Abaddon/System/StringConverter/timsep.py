import time

def timedict():

    ctime = time.asctime()

    tlist = ctime.split(' ')

    wday  = tlist[0]
    month = tlist[1]
    day   = tlist[3]
    year  = tlist[5]

    ctim  = tlist[4]

    tstr  = ctim.split(':')
    
    hour  = tstr[0]
    minu  = tstr[1]

    tdict = {}

    tdict['WeekDay']   = str(wday)
    tdict['Month']     = str(month)
    tdict['Day']       = str(day)
    tdict['Year']      = str(year)
    tdict['Hour']      = str(hour)
    tdict['Minuetes']  = str(minu)

    return tdict
