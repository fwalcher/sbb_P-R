import requests
import json


API_URL = "https://journey-service-int.api.sbb.ch"
CLIENT_SECRET = "MU48Q~IuD6Iawz3QfvkmMiKHtfXBf-ffKoKTJdt5"
CLIENT_ID = "f132a280-1571-4137-86d7-201641098ce8"
SCOPE = "c11fa6b1-edab-4554-a43d-8ab71b016325/.default"

def get_token():
    params = {
        'grant_type': 'client_credentials',
        'scope': SCOPE,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    return requests.post('https://login.microsoftonline.com/2cda5d11-f0ac-46b3-967d-af1b2e1bd01a/oauth2/v2.0/token',
                         data=params).json()

def use_token():
    auth = get_token()['access_token']
    headers = {
        'Authorization': f"Bearer {auth}",
        'Content-Type': 'application/json'
    }
    json_data = {"origin": "[7.38364, 46.95432]",
              "destination": "[8.54191,47.38517]",
              "date": "2023-12-18",
              "time": "13:07"
    }      
    out = requests.post('https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination',
                        headers=headers, json=json_data).json()
    return out

out = use_token()



# Replace 'path/to/your/output_file.txt' with the actual path and file name you want to use
# output_file_path = '/Users/felix/Documents/GitHub/apis/output_file.json'

# Open the file in write mode ('w')
# with open(output_file_path, 'w') as output_file:
    # Write content to the file
    # json.dump(out,output_file,indent=2)

# The file will be automatically closed when you exit the 'with' block

for i in range(len(out["trips"][0]["legs"])):
    tmp = str(out["trips"][0]["legs"][i]["id"]) +":" +str(out["trips"][0]["legs"][i]["mode"]) + ":" + str(out["trips"][0]["legs"][i]["duration"])
    print(tmp)

print("\n \n \n")


import pandas as pd

# Replace 'path/to/your/file.csv' with the actual path to your CSV file
csv_file_path = '/Users/felix/Documents/GitHub/apis/mobilitat.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Display the DataFrame
print(df)