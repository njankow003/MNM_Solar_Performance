import requests
import parameters as p

# def checkInput(checkInput):
#     if checkInput.isdigit():
#         return True
#     return False

# startYear = input("enter start year: ")
# startMonth = input("enter start month: ")
# startDay = input("enter start day: ")

#intervalInput = input("enter an interval time followed by s, m, or h: ")
#interval = "&interval="+ intervalInput
#starttime=2011-06-01 00:00:00

#startDate = "starttime=" + str(startYear) + "-" + str(startMonth) + "-" + str(startDay) + " 00:00:00" 
startDate = "starttime=2023-09-22 00:00:00"
# print(startDate)
# if checkInput(startYear) == True:
#     print("good job")
# else:
#     print("Please input a year in the form: XXXX")

def buildURL(Location: str,DataType,startTime,endTime,interval,summaryType):
    if Location == "Bus Barn" and DataType == "DailyTotal":
        url = "F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgFiqSlzYXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfERBSUxZIFRPVEFM"
    if Location == "Bus Barn" and DataType == "FlowTag":
        url = "F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH"
    if Location == "Electric Vehicle Charging" and DataType == "DailyTotal":
        url = "F1AbEAVYciAZHVU6DzQbJjxTxWwYTCY6CdT7hGiW-T9RdLVfg_XDEejkXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEVMRUNUUklDIFZFSElDTEUgQ0hBUkdJTkd8REFJTFkgVE9UQUw"
    if Location == "Electric Vehicle Charging" and DataType == "FlowTag":
        url = "F1AbEAVYciAZHVU6DzQbJjxTxWwYTCY6CdT7hGiW-T9RdLVfgFTQq7q9xNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEVMRUNUUklDIFZFSElDTEUgQ0hBUkdJTkd8RkxPVyBUQUc"
    FinalUrl = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/" + url + p.setInterpOrSummary + startTime + summaryType + endTime + interval
    return FinalUrl

#For Bus Barn
#Get the Pi Web API URL

Interpolated = "/interpolated?"
Summary = "/summary?"

print(buildURL(p.Location1, p.DataType1,p.startTime,p.endTime,p.urlInterval,p.summaryType1))



sinceInstallation = "starttime=2011-06-01 00:00:00"
sinceSeptember = "starttime=2023-09-01 00:00:00"
sinceYesterday = "starttime=2023-09-22 00:00:00"
startTime = sinceYesterday
endTime = "&endtime=*" #up to current
#interval = "&interval=1h"

maximumSummary = "&summaryType=Maximum"
averageSummary = "&summaryType=Average"
summaryType = averageSummary
#url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/" + DataType + Interpolated + startTime + endTime + interval + summaryType

#url = buildURL("Bus Barn", "DailyTotal", startDate,endTime,interval,summaryType)
#print(url)
#Make a GET request to the Pi Web API
#response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))

#Check the response status code
# if response.status_code == 200:
#     # The request was successful
#     print("The request was successful")
# else:
#     # The request failed
#     print("The request failed")



#Get the Pi Web API response
#response_json = response.json()

#Print the Pi Web API response
#print(response_json)


#response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))

#Get the Pi Web API response
#jsonResponse = response.json()

# Gets bus daily values and times into an array
# BusDailyTime = []
# BusDailyValue = []
# for dict in jsonResponse['Items']:
#      #print(dict["Timestamp"])
#      #print(dict["Value"])
#      BusDailyTime.append(dict["Timestamp"])
#      BusDailyValue.append(dict["Value"])