import requests
import matplotlib.pyplot as plt
import urlBuilder

startTime = "starttime=2023-09-22 00:00:00" #yesterday
endTime = "&endtime=*" #to current
interval = "&interval=1h" #1 hour interval
summaryType = "&summaryType=Maximum" #maximum summary, as opposed to average

def feetToMeters(feet):
    return feet * 0.09290304


#Get the Pi Web API URL
urlBusFlow = urlBuilder.buildURL("Bus Barn", "FlowTag",startTime,endTime,interval,summaryType)
urlBusDaily = urlBuilder.buildURL("Bus Barn", "DailyTotal",startTime,endTime,interval,summaryType)
urlVehDaily = urlBuilder.buildURL("Electric Vehicle Charging", "DailyTotal",startTime,endTime,interval,summaryType)
urlVehFlow = urlBuilder.buildURL("Electric Vehicle Charging", "FlowTag",startTime,endTime,interval,summaryType)

#Make a GET request to the Pi Web API
responseBusFlow = requests.get(urlBusFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))
responseBusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
responseVehDaily = requests.get(urlVehDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
responseVehFlow = requests.get(urlVehFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))

#Get the Pi Web API response
jsonBusFlow = responseBusFlow.json()
jsonBusDaily = responseBusDaily.json()
jsonVehDaily = responseVehDaily.json()
jsonVehFlow = responseVehFlow.json()

# Gets bus daily values and times into an array
BusDailyTime = []
BusDailyValue = []
for dict in jsonBusDaily['Items']:
    #print(dict["Timestamp"])
    BusDailyTime.append(dict["Timestamp"])
    BusDailyValue.append(dict["Value"])

BusFlowTime = []
BusFlowValue = []
for dict1 in jsonBusFlow['Items']:
    #print(dict["Timestamp"])
    BusFlowTime.append(dict1["Timestamp"])
    #print(dict["Timestamp"])
    BusFlowValue.append(dict1["Value"])

VehDailyTime = []
VehDailyValue = []
for dict2 in jsonVehDaily['Items']:
    #print(dict["Timestamp"])
    VehDailyTime.append(dict2["Timestamp"])
    VehDailyValue.append(dict2["Value"])

VehFlowTime = []
VehFlowValue = []
for dict3 in jsonVehFlow['Items']:
    #print(dict["Timestamp"])
    VehFlowTime.append(dict3["Timestamp"])
    #print(dict["Value"])
    VehFlowValue.append(dict3["Value"])

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
plt.title("")
plt.xlabel("")
plt.ylabel("")
#plt.plot(XAxis, YAxis, label = "")
plt.plot(BusFlowTime, BusFlowValue, label = "Bus Flow")
plt.plot(VehFlowTime, VehFlowValue, label = "Veh Flow")
plt.legend()
plt.show()
