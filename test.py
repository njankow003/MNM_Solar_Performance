import requests
import matplotlib.pyplot as plt
import urlBuilder
import parameters as p

#startTime = "starttime=2023-09-22 00:00:00" #yesterday
# endTime = "&endtime=*" #to current
# interval = "&interval=1h" #1 hour interval
# summaryType = "&summaryType=Maximum" #maximum summary, as opposed to average

# startYear = "2022"
# startMonth = "9"
# startDay = "22"
# startTime = "starttime=" + str(startYear) + "-" + str(startMonth) + "-" + str(startDay) + " 00:00:00" 

def feetToMeters(feet):
    return feet * 0.09290304

def getRequest(url):
    return requests.get(url, auth=('njankowski','eje3+ydIjO9?-39'))

def getResponse(request):
    return request.json()

def getTimesAndVals(json):
    Times = []
    Values = []
    for dict in json["Items"]:
        Times.append(dict["Timestamp"])
        Values.append(dict["Value"])
        #print(dict["Value"])
    #print("###########")
    return (Times, Values)

def Plot1(Times, Values, Label):
    return plt.plot(Times, Values, label = str(Label))

def Plot2(Times, Values, Label):
    return plt.plot(Times, Values, label = str(Label))

def createLabel(Location,DataType):
    return str(DataType) + " for the " + str(Location) + " location."

Vals1 = getTimesAndVals(getResponse(getRequest(urlBuilder.buildURL(p.Location1, p.DataType1,p.startTime,p.endTime,p.urlInterval,p.summaryType))))[0]
Times1 = getTimesAndVals(getResponse(getRequest(urlBuilder.buildURL(p.Location1, p.DataType1,p.startTime,p.endTime,p.urlInterval,p.summaryType))))[1]
Label1 = createLabel(p.Location1, p.DataType1)

Vals2 = getTimesAndVals(getResponse(getRequest(urlBuilder.buildURL(p.Location2, p.DataType2,p.startTime,p.endTime,p.urlInterval,p.summaryType))))[0]
Times2 = getTimesAndVals(getResponse(getRequest(urlBuilder.buildURL(p.Location2, p.DataType2,p.startTime,p.endTime,p.urlInterval,p.summaryType))))[1]
Label2 = createLabel(p.Location2, p.DataType2)

plt.title("")
plt.xlabel("")
plt.ylabel("")
Plot1(Vals1,Times1,Label1)
Plot2(Vals2,Times2,Label2)
plt.legend()
plt.show()



#Get the Pi Web API URL
# urlBusFlow = urlBuilder.buildURL("Bus Barn", "FlowTag",p.startTime,p.endTime,p.urlInterval,p.summaryType)
# urlBusDaily = urlBuilder.buildURL("Bus Barn", "DailyTotal",p.startTime,p.endTime,p.urlInterval,p.summaryType)
# urlVehDaily = urlBuilder.buildURL("Electric Vehicle Charging", "DailyTotal",p.startTime,p.endTime,p.urlInterval,p.summaryType)
# urlVehFlow = urlBuilder.buildURL("Electric Vehicle Charging", "FlowTag",p.startTime,p.endTime,p.urlInterval,p.summaryType)

# #Make a GET request to the Pi Web API
# responseBusFlow = requests.get(urlBusFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))
# responseBusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
# responseVehDaily = requests.get(urlVehDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
# responseVehFlow = requests.get(urlVehFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))

# #Get the Pi Web API response
# jsonBusFlow = responseBusFlow.json()
# jsonBusDaily = responseBusDaily.json()
# jsonVehDaily = responseVehDaily.json()
# jsonVehFlow = responseVehFlow.json()

# print(getValAndTimes(jsonBusFlow))
# #getValAndTimes(jsonBusDaily)




# # Gets bus daily values and times into an array
# BusDailyTime = []
# BusDailyValue = []
# for dict in jsonBusDaily['Items']:
#     #print(dict["Timestamp"])
#     BusDailyTime.append(dict["Timestamp"])
#     BusDailyValue.append(dict["Value"])

# BusFlowTime = []
# BusFlowValue = []
# for dict1 in jsonBusFlow['Items']:
#     #print(dict["Timestamp"])
#     BusFlowTime.append(dict1["Timestamp"])
#     #print(dict["Timestamp"])
#     BusFlowValue.append(dict1["Value"])

# VehDailyTime = []
# VehDailyValue = []
# for dict2 in jsonVehDaily['Items']:
#     #print(dict["Timestamp"])
#     VehDailyTime.append(dict2["Timestamp"])
#     VehDailyValue.append(dict2["Value"])

# VehFlowTime = []
# VehFlowValue = []
# for dict3 in jsonVehFlow['Items']:
#     #print(dict["Timestamp"])
#     VehFlowTime.append(dict3["Timestamp"])
#     #print(dict["Value"])
#     VehFlowValue.append(dict3["Value"])

"""
plt.title("")
plt.xlabel("")
plt.ylabel("")
#plt.plot(XAxis, YAxis, label = "")
plt.plot(BusDailyTime, BusDailyValue, label = "Bus Daily")
plt.plot(VehDailyTime, VehDailyValue, label = "Veh Daily")
plt.legend()
plt.show()
"""
# plt.title("")
# plt.xlabel("")
# plt.ylabel("")
# Plot1(Vals1,Times1,Label1)
# Plot2(Vals2,Times2,Label2)
# #plt.plot(XAxis, YAxis, label = "")
# #plt.plot(BusFlowTime, BusFlowValue, label = "Bus Flow")
# #Plot1(getValAndTimes(jsonBusFlow)[0],getValAndTimes(jsonBusFlow)[1],"Bus Flow")
# #Plot2(getValAndTimes(jsonVehFlow)[0],getValAndTimes(jsonVehFlow)[1],"Veh Flow")
# #plt.plot(getValAndTimes(jsonBusFlow)[0], getValAndTimes(jsonBusFlow)[1], label = "Bus Flow")
# #plt.plot(VehFlowTime, VehFlowValue, label = "Veh Flow")
# plt.legend()
# plt.show()
