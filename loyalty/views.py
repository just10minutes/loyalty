from django.http import HttpResponse


def index(request):
    return HttpResponse("This is what we want to achieve")
