from django.http import HttpResponse


def index(request):
    return HttpResponse("This is Index page of wonderful Loyalty App.")
