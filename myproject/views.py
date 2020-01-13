from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def bye(request):
    return HttpResponse("Goodbye World")
