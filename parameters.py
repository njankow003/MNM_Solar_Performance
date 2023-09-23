endTime = "&endtime=*" #to current
interval = "1" #1 hour interval
intervalUnits = "h"
urlInterval = "&interval=" + interval + intervalUnits
summaryType = "&summaryType=Maximum" #maximum summary, as opposed to average

sinceInstall = False
startYear = "2022"
startMonth = "9"
startDay = "22"
if sinceInstall == True:
    startTime = "2011-06-01 00:00:00"
else:
    startTime = "starttime=" + str(startYear) + "-" + str(startMonth) + "-" + str(startDay) + " 00:00:00"

untilCurrent = True
endYear = ""
endMonth = ""
endDay = ""
if untilCurrent == True:
    endTime = "&endtime=*"
else:
    endTime = "&endtime="  + str(endYear) + "-" + str(endMonth) + "-" + str(endDay) + " 00:00:00"