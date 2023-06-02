from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_view, name='hello'),
    path('quiz/', views.quiz_view, name='quiz'),
]
