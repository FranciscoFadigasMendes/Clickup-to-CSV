import requests
import json
import csv


# Replace with your API and the specific ID
API_TOKEN = 'pk_88710984_GPU82FQ1W3H9CPDDVC67H0KQINS0BPJC'
ID = 901507004313  

url = f'https://api.clickup.com/api/v2/list/{ID}'

headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json'
}

#-------------------------------------------------------------------

# GET from ClickUP API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    tasks = response.json()
    print(tasks)  # This will contain task details
else:
    print("Error:", response.status_code, response.text)
    exit()

#-------------------------------------------------------------------

# Save the .json file
with open("get_Sprint4.json", "w") as fwriter:
    json.dump(fp=fwriter, obj=tasks, indent=4, sort_keys=True)

#-------------------------------------------------------------------

print("\n!!! DONE - API to JSON !!!")
