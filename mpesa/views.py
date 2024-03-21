import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def register_till_number(request):
    access_token = "zaYtJtX9AD6ncIShL7IbgROwHXCYfxr40lNgDawF4FBMJlcD" # Updated with your Consumer Key
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": f"Bearer {access_token}"}
    request_data = {
        "ShortCode": "4225734", # Updated with your Till Number
        "ResponseType": "Completed",
        "ConfirmationURL": "YOUR_CONFIRMATION_URL", # Replace with your actual Confirmation URL
        "ValidationURL": "YOUR_VALIDATION_URL" # Replace with your actual Validation URL
    }

    response = requests.post(api_url, json=request_data, headers=headers)
    return HttpResponse('success')


@csrf_exempt
def c2b_validation(request):
    # Process the validation request from M-Pesa
    # This is where you check the transaction details and decide whether to accept the transaction
    # For now, let's just return a success response
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

@csrf_exempt
def c2b_confirmation(request):
    # Process the confirmation request from M-Pesa
    # This is where you receive the final transaction details
    # For now, let's just return a success response
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Confirmed"})
