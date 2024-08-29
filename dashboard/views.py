from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import SOSAlert


# ====================================== DASHBOARD ======================================

def dashboard(request):
    
    api_url = "http://www.randomnumberapi.com/api/v1.0/random"
    
    return render(request, "dashboard/index.html")

# ====================================== OUR VOLUNTEERS ======================================

def our_volunteers(request):
    return render(request, "dashboard/our_volunteers.html")


# ====================================== DANGER ZONES ======================================

def danger_zones(request):
    return render(request, "dashboard/danger_zones.html")

# ============================================================================================


@csrf_exempt
def sos_call(request):
    if request.method == 'POST':
                
        SOSAlert.objects.create(message="An SOS has been triggered")
        return JsonResponse({
            "status": "success", 
            "message": "SOS alert created"
            })
    
    return JsonResponse({
        "status": "failed", 
        "message": "Invalid request method"
        }, status=400)

