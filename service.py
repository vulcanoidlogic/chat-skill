import requests
import json
import sys
squireURL  = "http://squire-200.iobtlab.com:9090/api/ChatHub/CentralModel"
azureURL = "https://iobtweb.azurewebsites.net/api/ChatHub/CentralModel"
response = requests.get(azureURL)
print(response)
##response.content() # Return the raw bytes of the data payload
##response.text() # Return a string representation of the data payload
result = response.json() # This method is convenient when the API returns JSON
# print(result)
if ( result['hasError'] == True):
    print(result['message'])
else:
    payload = result['payload']
    print(payload)
#now test a post ,  you need to see the map
position = dict({
            'user': "Mason_14",
            'lat': 58.894294200000004,
            'lng': -77.25141959999999,
            'alt': 0,
            'speed': 0,
            'heading': 0,
            'sourceGuid': "8693d3d1-f612-4a18-d8bc-33ef165855bd",
            'timeStamp': "2021-04-07T01:05:46.367Z",
            'personId': "MasonX_6"
          });
squireURL  = "http://squire-200.iobtlab.com:9090/api/ChatHub/Position"
azureURL = "https://iobtweb.azurewebsites.net/api/ChatHub/Position"
#  azureURL = "http://localhost:5000/api/ChatHub/Position"
headers = {'Content-type':'application/json', 'Accept':'application/json'}
# sending post request and saving response as response object
# extracting response text 
##response.content() # Return the raw bytes of the data payload
print("-----------------------------------------------------------------text")
try:
    response = requests.post(url = azureURL, json = position, headers = headers)
    print(response)
    result = response.json()
    # print(result)
    if ( result['hasError'] == True):
        print(result['message'])
    else:
        payload = result['payload']
        print(payload)
except TypeError as e:
    print(sys.exc_info()[0])
    print(sys.exc_info())
message = dict({
            "user": "Llam_9",
            "message": "Posting a Message",
            "sourceGuid": "375ad623-6e7c-4272-8aa7-d631d22a356d",
            "timeStamp": "2021-04-07T11:55:46.669Z",
            "personId": "Llam_9"
          })
squireURL  = "http://squire-200.iobtlab.com:9090/api/ChatHub/ChatMessage"
azureURL = "https://iobtweb.azurewebsites.net/api/ChatHub/ChatMessage"
#  azureURL = "http://localhost:5000/api/ChatHub/Position"
headers = {'Content-type':'application/json', 'Accept':'application/json'}
# sending post request and saving response as response object
# extracting response text 
##response.content() # Return the raw bytes of the data payload
print("-----------------------------------------------------------------text")
try:
    response = requests.post(url = azureURL, json = message, headers = headers)
    print(response)
    result = response.json()
    #print(result)
    if ( result['hasError'] == True):
        print(result['message'])
    else:
        payload = result['payload']
        print(payload)
except TypeError as e:
    print(sys.exc_info()[0])
    print(sys.exc_info())