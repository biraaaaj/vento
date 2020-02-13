from django.http import JsonResponse

APP_INFO = {
    'name': 'invest',
    'version': '0.1'
}


def welcome(request):
    return JsonResponse(APP_INFO)
