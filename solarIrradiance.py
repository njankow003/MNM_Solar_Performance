import requests
import matplotlib.pyplot as plt

# I*A*C = E
#conversionEfficiency = energyGenerated / (solarIrradiance * solarArrayArea)
url = "http://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.json?api_key=4YTYIMO1EOAHxbLnkwIWLSDSTCCN8RHqxC5dWJ4l"

payload = "wkt=POINT(179.9901 -16.96)&attributes=alpha,aod,ghi,dni,dhi&names=2018&utc=true&leap_day=true&email=njankow003@gmail.com"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

"""
EVCATime = []
EVCAEnergy = []

plt.title("Conversion Efficiency of EVCA Over Time")
plt.xlabel("Time")
plt.ylabel("Conversion Efficiency")
plt.plot(CAMBUSTime, CAMBUSEnergy, color = "o")
plt.show()
"""