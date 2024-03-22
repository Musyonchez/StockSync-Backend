import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import contextlib # Import contextlib
import os
from requests.auth import HTTPBasicAuth


def lipa_na_mpesa_online(request):
    # Your M-Pesa API credentials
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    # The M-Pesa OAuth endpoint
    oauth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    # Make a request to the OAuth endpoint to get an access token
    response = requests.get(oauth_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # Extract the access token from the response
    try:
        access_token = response.json().get("access_token")
    except json.JSONDecodeError:
        # Handle the error, e.g., log the error and return an appropriate response
        print("Error decoding JSON")
        return HttpResponse('Error decoding JSON', status=500)

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": f"Bearer {access_token}"}
    request_data = {
        "ShortCode": (os.getenv("SHORT_CODE")), # Updated with your Till Number
        "ResponseType": "Completed",
        "ConfirmationURL": "https://stocksync-backend.onrender.com/C2B-CONFIRMATION/", # Updated Confirmation URL
        "ValidationURL": "https://stocksync-backend.onrender.com/C2B-VALIDATION/" # Updated Validation URL
    }

    # Use contextlib.suppress to catch and ignore the exception
    with contextlib.suppress(requests.exceptions.RequestException):
        response = requests.post(api_url, json=request_data, headers=headers)
        response.raise_for_status() # Raises an HTTPError if the response status is 4xx or 5xx
        
    if response.status_code == 200:
        return HttpResponse('success')
    else:
        return HttpResponse(f'Error: {response.content}', status=response.status_code)




@csrf_exempt
def c2b_validation(request):
    if request.method != 'POST':
        return HttpResponse(status=405) # Method not allowed
    # Extract transaction details from the request
    data = json.loads(request.body)
    transaction_details = data['TransactionDetails']
    transaction_id = transaction_details['TransactionID']
    amount = transaction_details['Amount']
    msisdn = transaction_details['MSISDN']
    # Here you can implement your validation logic
    # For example, check if the transaction ID exists in your database and if the amount matches
    # For now, let's just return a success response
    response_data = {
        "ResultCode": 0,
        "ResultDesc": "Accepted",
        "ThirdPartyTransID": "123456789" # You can generate your own unique transaction ID here
    }
    return JsonResponse(response_data)


@csrf_exempt
def c2b_confirmation(request):
    if request.method != 'POST':
        return HttpResponse(status=405) # Method not allowed
    # Extract transaction details from the request
    data = json.loads(request.body)
    transaction_details = data['TransactionDetails']
    transaction_id = transaction_details['TransactionID']
    amount = transaction_details['Amount']
    msisdn = transaction_details['MSISDN']
    # Here you can update your database with the transaction details
    # For now, let's just return a success response
    response_data = {
        "ResultCode": 0,
        "ResultDesc": "Confirmed"
    }
    return JsonResponse(response_data)
