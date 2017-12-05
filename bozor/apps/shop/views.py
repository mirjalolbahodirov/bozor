from django.http import HttpRequest, HttpResponse


# Create your views here.

def index(req):
    return HttpResponse("Hello")
