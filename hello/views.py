from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello! Enter a text below to turn into a quiz: ")