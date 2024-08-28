from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from .models import SOSAlert
import requests
import time



# ====================================== SOS CALLS ======================================

def get_sos_calls(request):
    # api_url = "https://www.randomnumberapi.com/api/v1.0/random"
    
    # try:
    #     response = requests.get(api_url)
    #     if response.status_code == 200:
    #         random_number = response.json()
    #     else:
    #         random_number = 0
    # except requests.RequestException as e:
    #     print(f"API request failed: {e}")
    #     random_number = 0
    
    return JsonResponse({'sos_calls': 10})

# ====================================== GET VOLUNTEERS NUMBER ======================================

def get_volunteers_number(request):
    
    # api_url = "https://www.randomnumberapi.com/api/v1.0/random"
    
    # try:
    #     response = requests.get(api_url)
        
    #     if response.status_code == 200:
    #         random_number = response.json()
        
    #     else:
    #         random_number = 0
        
    # except:
    #     random_number = 0
    
    return JsonResponse(
        {
            'volunteers_number': 20
        }
        )

# ====================================== GET USERS NUMBER ======================================

def get_users_number(request):
    
    # api_url = "https://www.randomnumberapi.com/api/v1.0/random"
    
    # response = requests.get(api_url)
    
    # if response.status_code == 200:
    #     users = response.json()
        
    # else:
    #     users = 0
    
    return JsonResponse({
        'users_number': 30
    })
        
# ====================================== FETCH SOS CALLS ======================================



def fetch_sos_alert(request):
    try:
        # Fetch the latest SOS alert
        latest_alert = SOSAlert.objects.latest('timestamp')
        # Calculate the time difference
        time_difference = timezone.now() - latest_alert.timestamp
        
        # Check if the latest alert was within the last 2 minutes
        if time_difference <= timedelta(seconds=30):
            alert_data = {
                "message": latest_alert.message,
                "timestamp": latest_alert.timestamp,
                "time_difference": str(time_difference.seconds) + " seconds ago"
            }
            return JsonResponse({"alert": alert_data})
        else:
            return JsonResponse({"alert": None, "message": "No recent SOS alerts"})
    
    except SOSAlert.DoesNotExist:
        # If no alerts exist in the database
        return JsonResponse({"alert": None, "message": "No SOS alerts available"})
