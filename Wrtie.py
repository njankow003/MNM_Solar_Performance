import requests
import json
url = "https://itsnt2259.iowa.uiowa.edu/piwebapi/streams/DAILY_TOTAL_STREAM_ID/summary?starttime=2011-06-01 00:00:00&endtime=*&summaryType=Maximum&summaryDuration=1d" #maxCount will set upper limit of values to be returned
filepath = "C:/Users/Jorom/Documents/test.txt"
response = requests.get(str(url), auth=('<user>', '<password>'), verify=False) #verify=False will disable the certificate verification check
json_data = response.json()
timestamp = []
value = []
isGood = []
#Parsing Json response
for j_object in json_data["Items"]:
 timestamp.append(j_object["Timestamp"])
 value.append(j_object["Value"])
 isGood.append(j_object["Good"])

event_array = zip(timestamp, value, isGood)
#Writing to file
with open(str(filepath), "w") as f:
 for item in event_array:

    try:
        writestring = "Timestamp: " + str(item[0]) + " , Value: " + str(item[1]) + " , isGood: " + str(item[2]) + " \n"

    except:

        try:
            writestring = "" + str(item[0]) + " \n"
        except:
            writestring = "" + " \n"

 f.write(writestring)
 f.close()



#filepath = "C:/Users/Jorom/Documents/test.txt"

#with open(filepath, "w") as f:
#    f.write("hello")

#f.close()