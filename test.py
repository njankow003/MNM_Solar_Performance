import requests
import matplotlib.pyplot as plt


def feetToMeters(feet):
    return feet * 0.09290304


#Get the Pi Web API URL
urlBusFlow = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/recorded"
urlBusDaily = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgFiqSlzYXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfERBSUxZIFRPVEFM/recorded"
urlVehDaily = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwYTCY6CdT7hGiW-T9RdLVfg_XDEejkXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEVMRUNUUklDIFZFSElDTEUgQ0hBUkdJTkd8REFJTFkgVE9UQUw/recorded"

#Make a GET request to the Pi Web API
responseBusFlow = requests.get(urlBusFlow, auth=('njankowski', 'eje3+ydIjO9?-39'))
responseBusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
responseVehDaily = requests.get(urlVehDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))

#Get the Pi Web API response
jsonBusFlow = responseBusFlow.json()
jsonBusDaily = responseBusDaily.json()
jsonVehDaily = responseBusDaily.json()

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
    print(dict["Timestamp"])
    BusFlowValue.append(dict["Value"])

VehDailyTime = []
VehDailyValue = []
for dict in jsonVehDaily['Items']:
    #print(dict["Timestamp"])
    VehDailyTime.append(dict["Timestamp"])
    VehDailyValue.append(dict["Value"])

plt.title("")
plt.xlabel("")
plt.ylabel("")
#plt.plot(XAxis, YAxis, label = "")
plt.plot(BusDailyTime, BusDailyValue, label = "Bus Daily")
plt.plot(VehDailyTime, VehDailyValue, label = "Veh Daily")
plt.legend()
plt.show()
