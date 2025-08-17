import datetime

from django.http import JsonResponse


def index(request):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse(
        {
            "name": "figen",
            "user": "admin",
            "server_time": current_date,
        }
    )
