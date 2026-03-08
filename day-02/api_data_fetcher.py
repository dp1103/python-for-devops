""" Task:
1.Calls a public API (example: GitHub API, JSONPlaceholder) list
2.Fetches data using the requests library
3.Parses the JSON response
4.Extracts meaningful information from the response
5.Prints the processed output to the terminal
6.Saves the processed data into a JSON file"""

import requests
import json
api_url= 'https://api.github.com/events'

response=requests.get(url=api_url)
data_set=response.json()

# returning keys of data
# for i in data_set[:1]:   
#     print(i.keys())

events=[]  
event=[{
        "id": data['id'],
        "type": data['type'],
        "actor": data['actor']['login'],
        "repo": data['repo']['name'],
        "payload": data['payload']['ref'],
        "public": data['public'],
        "created_at": data['created_at']

    } for data in data_set[:5]]

events.extend(event) # TO MERGE LIST
# print(events)

with open("output.json", 'w') as file: 
    json.dump(events,file, indent=4)

def event_print():
    print("Events")
    for i in events:
        print(f"Event_id: {i["id"]}")
        print(f"Type: {i["type"]}")  
        print(f"Actor: {i["actor"]}")
        print(f"Repo: {i["repo"]}")
        print(f"payload: {i["payload"]}")
        print(f"Public: {i["public"]}")
        print(f"Creatd: {i["created_at"]}")
        print("-"*20)
    
event_print()