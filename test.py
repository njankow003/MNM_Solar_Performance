import requests

#Get the Pi Web API URL
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfg_m58A6BxNVULugR7j2EabASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfEZMT1cgVEFH/recorded"
urlBusDaily = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/F1AbEAVYciAZHVU6DzQbJjxTxWwimrOBShT7hGiW-T9RdLVfgFiqSlzYXN1c8B8kKhkXr4ASVRTTlQyMjU5XFJZQU4gU0FOREJPWFxTT0xBUiBQUk9EVUNUSU9OXEJVUyBCQVJOfERBSUxZIFRPVEFM/recorded"

#Make a GET request to the Pi Web API
response = requests.get(url, auth=('njankowski', 'eje3+ydIjO9?-39'))
responsebusDaily = requests.get(urlBusDaily, auth=('njankowski', 'eje3+ydIjO9?-39'))
#Check the response status code
if response.status_code == 200:
    # The request was successful
    print("The request was successful")
else:
    # The request failed
    print("The request failed")

#Get the Pi Web API response
response_json = response.json()
response_jsonBusDaily = responsebusDaily.json()
#Print the Pi Web API response
#print(response_json)

#print(dir(response_json))

#print(response_json.items())

#print(response_json['Items'][0]["Timestamp"])

#for dict in response_json['Items']:
 #   print(dict["Value"])

for dict in response_jsonBusDaily['Items']:
    print(dict["Timestamp"])
