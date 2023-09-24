import requests
import matplotlib.pyplot as plt

# I*A*C = E
#4YTYIMO1EOAHxbLnkwIWLSDSTCCN8RHqxC5dWJ4l
#conversionEfficiency = energyGenerated / (solarIrradiance * solarArrayArea)
url = "http://developer.nrel.gov/api/nsrdb/v2/solar/psm3-2-2-download.json?api_key=4YTYIMO1EOAHxbLnkwIWLSDSTCCN8RHqxC5dWJ4l"

payload = "names=2021&leap_day=true&interval=30&utc=true&email=honored.njankow003%40gmail.com&attributes=dhi%2Cdni%2Cghi&wkt=MULTIPOINT(-106.22%2032.9741%2C-106.18%2032.9741%2C-106.1%2032.9741)"

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