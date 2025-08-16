from django.http import HttpResponse,JsonResponse


def index(request):
    data = {
    "name": "eren",
    "user": "admin"
    }
    return JsonResponse(data)

