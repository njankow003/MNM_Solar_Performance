#endTime = "&endtime=*" #to current

#Define an interval of flow times and the unit of time
intervalAmount = "1"
intervalUnits = "h"

#Define summary type as Maximum or Average
maximumOrAverage = "Maximum"

#Define a start date or collect data since installation
sinceInstall = False
startYear = "2023"
startMonth = "9"
startDay = "22"

#Define an end date or collect data until now
untilCurrent = True
endYear = ""
endMonth = ""
endDay = ""

#Define location as either Bus Barn or Electric Vehicle Charging
Location1 = "Bus Barn"

Location2 = "Electric Vehicle Charging"

#Define DataType as FlowTag or DailyTotal
DataType1 = "FlowTag"

DataType2 = "FlowTag"




urlInterval = "&interval=" + intervalAmount + intervalUnits
if maximumOrAverage == "Maximum":
    summaryType = "&summaryType=Maximum" #maximum summary, as opposed to average
if maximumOrAverage == "Average":
    summaryType = "&summaryType=Average"

if sinceInstall == True:
    startTime = "2011-06-01 00:00:00"
else:
    startTime = "starttime=" + str(startYear) + "-" + str(startMonth) + "-" + str(startDay) + " 00:00:00"

if untilCurrent == True:
    endTime = "&endtime=*"
else:
    endTime = "&endtime="  + str(endYear) + "-" + str(endMonth) + "-" + str(endDay) + " 00:00:00"