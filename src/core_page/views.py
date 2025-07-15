from django.http import HttpResponse,JsonResponse


def index(request):
    return JsonResponse(data={"name"  : "eren"})

