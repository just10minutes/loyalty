from django.http import HttpResponse


def index(request):
    return HttpResponse("Lets work on this new Loyalty App")
