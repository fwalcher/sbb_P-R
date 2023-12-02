import requests

API_URL = "https://journey-service-int.api.sbb.ch"
CLIENT_SECRET = "MU48Q~IuD6Iawz3QfvkmMiKHtfXBf-ffKoKTJdt5"
CLIENT_ID = "f132a280-1571-4137-86d7-201641098ce8"
SCOPE = "c11fa6b1-edab-4554-a43d-8ab71b016325/.default"
api_key = 'bf9e3a88ab8101ba22ba8c752bbbcfd8'


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
    headers = {
        'Authorization': f"Bearer {get_token()['access_token']}",
        'Content-Type': 'application/json',
    }
    # Include the header (and additional ones if needed in your request


endpoint = '/v1/journey'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Make a GET request to the API
#response = requests.get(f'{API_URL}{endpoint}?api_key={api_key}', headers=headers)
response = requests.get(f'https://journey-service-int.api.sbb.ch/v1/journey?api_key={api_key}')
# Process the response
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    print(f'Error: {response.status_code} - {response.text}')



