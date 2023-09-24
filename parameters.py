#Define an interval of flow times and the unit of time
intervalAmount = "1"
intervalUnits = "h"

#Set "Interpolated" or "Summary"
interpOrSummary = "Interpolated"

#If using Summary, define the type of summary
if interpOrSummary == "Summary":
    #Define summary type as "Maximum" or "Average"
    summaryType1 = "Total"
    summaryType2 = "Total"

#Define a start date or collect data since installation
sinceInstall = True
startYear = "2023"
startMonth = "9"
startDay = "22"

#Define an end date or collect data until now
untilCurrent = False
endYear = "2011"
endMonth = "07"
endDay = "01"

#Define location as either "Bus Barn" or "Electric Vehicle Charging"
Location1 = "Bus Barn"

Location2 = "Bus Barn"

#Define DataType as "FlowTag" or "DailyTotal"
DataType1 = "FlowTag"

DataType2 = "FlowTag"



if interpOrSummary == "Interpolated":
    urlInterval = "&interval=" + intervalAmount + intervalUnits
    setSummaryType1 = ""
    setSummaryType2 = ""
if interpOrSummary == "Summary":
    urlInterval = "&summaryDuration=" + intervalAmount + intervalUnits

if interpOrSummary == "Summary":
    setSummaryType1 = "&summaryType=" + summaryType1
    setSummaryType2 = "&summaryType=" + summaryType2
    urlInterval = "&summaryDuration=" + intervalAmount + intervalUnits

# if interpOrSummary == "Summary":
#     summaryType2 = "&summaryType=" + maximumOrAverage2
#     # if maximumOrAverage2 == "Maximum":
#     #     summaryType2 = "&summaryType=Maximum" #maximum summary, as opposed to average
#     # if maximumOrAverage2 == "Average":
#     #     summaryType2 = "&summaryType=Average"
    # if maximumOrAverage1 == "Maximum":
    #     summaryType1 = "&summaryType=Maximum" #maximum summary, as opposed to average
    # if maximumOrAverage1 == "Average":
    #  summaryType1 = "&summaryType=Average"

if sinceInstall == True:
    startTime = "starttime=2011-06-01 00:00:00"
else:
    startTime = "starttime=" + str(startYear) + "-" + str(startMonth) + "-" + str(startDay) + " 00:00:00"

if untilCurrent == True:
    endTime = "&endtime=*"
else:
    endTime = "&endtime="  + str(endYear) + "-" + str(endMonth) + "-" + str(endDay) + " 00:00:00"

if interpOrSummary == "Summary":
    setInterpOrSummary = "/summary?"
if interpOrSummary == "Interpolated":
    setInterpOrSummary = "/interpolated?"