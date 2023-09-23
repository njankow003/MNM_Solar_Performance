import requests

#Get the Pi Web API URL
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/DAILY_TOTAL_STREAM_ID/summary?starttime=2011-06-01 00:00:00&endtime=*&summaryType=Maximum&summaryDuration=1d"

#Make a GET request to the Pi Web API
response = requests.get(url)

#Check the response status code
if response.status_code == 200:
    # The request was successful
    print("The request was successful")
else:
    # The request failed
    print("The request failed")

#Get the Pi Web API response
#response_json = response.json()

#Print the Pi Web API response
#print(response_json)