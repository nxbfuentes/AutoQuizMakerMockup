from django.http import HttpResponse
from django.shortcuts import render, redirect


def hello_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        file = request.FILES.get('file')
        if file is not None:
            # Do something with the file
            pass
        return redirect('quiz')
        return HttpResponse(f"Creating a quiz based on: {text}")
    else:
        return render(request, 'hello.html')
    
def quiz_view(request):
    if request.method == 'POST':
        answers = {
            'question1': 'c',
            'question2': 'a',
            'question3': 'd',
            'question4': 'c',
            'question5': 'c',
        }
        score = 0
        for question, correct_answer in answers.items():
            user_answer = request.POST.get(question)
            if user_answer == correct_answer:
                score += 1
        return HttpResponse(f"Your score: {score}")
    else:
        return render(request, 'quiz.html')
