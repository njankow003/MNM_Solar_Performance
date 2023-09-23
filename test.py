import requests

#Get the Pi Web API URL
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/interpolated?starttime=2011-06-01 00:00:00 &endtime=*&interval=1h"


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