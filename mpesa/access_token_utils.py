# mpesa_utils.py
import os
import requests
from contextlib import suppress

def get_access_token():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    headers = {'Content-Type': 'application/json'}
    auth = (consumer_key, consumer_secret)
    
    try:
        response = requests.get(access_token_url, headers=headers, auth=auth)
        response.raise_for_status()
        access_token = response.json().get("access_token")
        print("acces Token", access_token)
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error getting access token: {e}")
        return None



# def lipa_na_mpesa_online(request):
#     # Your M-Pesa API credentials
#     consumer_key = os.getenv("CONSUMER_KEY")
#     consumer_secret = os.getenv("CONSUMER_SECRET")

#     # The M-Pesa OAuth endpoint
#     access_token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

#     # Make a request to the OAuth endpoint to get an access token

#     headers = {'Content-Type': 'application/json'}
#     auth = (consumer_key, consumer_secret)
    
#     # # Extract the access token from the response
#     try:
#         response = requests.get(access_token_url, headers=headers, auth=auth)
#         response.raise_for_status()  # Raise exception for non-2xx status codes
#         access_token = response.json().get("access_token")
#         print("acces Token", access_token)
#     except json.JSONDecodeError:
#         # Handle the error, e.g., log the error and return an appropriate response
#         print("Error decoding JSON")
#         return HttpResponse('Error decoding JSON', status=500)