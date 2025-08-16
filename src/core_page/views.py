import datetime
import logging

from django.http import JsonResponse

logger = logging.getLogger(__name__)


def index(request):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse(
        {
            "name": "eren",
            "user": "admin",
            "server_time": current_date,
        }
    )
