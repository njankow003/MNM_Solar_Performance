import requests
import matplotlib.pyplot as plt

# I*A*C = E
# C = E / (I*A)

def feetToMeters(feet):
    return feet * 0.09290304

#Get the Pi Web API URL
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/recorded"

#Make a GET request to the Pi Web API
response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))

#Check the response status code
if response.status_code == 200:
    # The request was successful
    print("The request was successful")
else:
    # The request failed
    print("The request failed")

#Get the Pi Web API response
response_json = response.json()

#Print the Pi Web API response
print(response_json)

EVCATime = []
CAMBUSTime = []
EVCAEnergy = []
CAMBUSEnergy = []

plt.title("Conversion Efficiency of EVCA Over Time")
plt.xlabel("Time")
plt.ylabel("Conversion Efficiency")
plt.plot(EVCATime, EVCAEnergy)
plt.legend()
plt.show()

plt.title("Conversion Efficiency of EVCA Over Time")
plt.xlabel("Time")
plt.ylabel("Conversion Efficiency")
plt.plot(CAMBUSTime, CAMBUSEnergy)
plt.legend()
plt.show()

plt.title("Conversion Efficiency of EVCA and CA Overlapped")
plt.xlabel("Time")
plt.ylabel("Conversion Efficiency")
plt.plot(EVCATime, EVCAEnergy, label = "EVCA")
plt.plot(CAMBUSTime, CAMBUSEnergy, label = "CA")
plt.legend()
plt.show()