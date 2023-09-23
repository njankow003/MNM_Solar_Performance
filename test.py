import requests
import matplotlib.pyplot as plt


def feetToMeters(feet):
    return feet * 0.09290304


#Get the Pi Web API URL
urlBusFlow = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/recorded"
urlBusDaily = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgFiqSlzYXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfERBSUxZIFRPVEFM/recorded"


#Make a GET request to the Pi Web API
responseBusFlow = requests.get(urlBusFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))
responsebusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))


#Get the Pi Web API response
jsonBusFlow = responseBusFlow.json()
jsonBusDaily = responsebusDaily.json()

# Gets bus daily values and times into an array
BusDailyTime = []
BusDailyValue = []
for dict in jsonBusDaily['Items']:
    #print(dict["Timestamp"])
    BusDailyTime.append(dict["Timestamp"])
    BusDailyValue.append(dict["Value"])

BusFlowTime = []
BusFlowValue = []
for dict in jsonBusFlow['Items']:
    #print(dict["Timestamp"])
    BusFlowTime.append(dict["Timestamp"])
    BusFlowValue.append(dict["Value"])

plt.title("")
plt.xlabel("")
plt.ylabel("")
#plt.plot(XAxis, YAxis, label = "")
plt.plot(BusDailyTime, BusDailyValue, label = "Bus Daily")
plt.plot(BusFlowTime, BusFlowValue, label = "Bus Flow")
plt.legend()
plt.show()
