from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        file = request.FILES.get('file')
        if file is not None:
            # Do something with the file
            pass
        return HttpResponse(f"Creating a quiz based on: {text}")
    else:
        return render(request, 'hello.html')