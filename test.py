import requests
import matplotlib.pyplot as plt

#Get the Pi Web API URL
<<<<<<< HEAD
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/recorded"
urlBusDaily = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgFiqSlzYXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfERBSUxZIFRPVEFM/recorded"


#Make a GET request to the Pi Web API
response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))
responsebusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
=======
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/interpolated"

#Make a GET request to the Pi Web API
response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))
>>>>>>> aa1d879999f09f9160e670befb43d401f6e1a309


#Get the Pi Web API response
response_json = response.json()
response_jsonBusDaily = responsebusDaily.json()

# Gets bus daily values and times into an array
BusDailyTime = []
BusDailyValue = []
for dict in response_jsonBusDaily['Items']:
    #print(dict["Timestamp"])
    BusDailyTime.append(dict["Timestamp"])
    BusDailyValue.append(dict["Value"])


plt.title("")
plt.xlabel("")
plt.ylabel("")
#plt.plot(XAxis, YAxis, label = "")
plt.plot(BusDailyTime, BusDailyValue, label = "Bus Daily")
plt.legend()
plt.show()
