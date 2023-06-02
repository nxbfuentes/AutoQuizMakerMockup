from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        return HttpResponse(f"Creating a quiz based on:\n {text}")
    else:
        return render(request, 'hello.html')