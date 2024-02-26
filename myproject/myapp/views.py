from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is my first Django view.")
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
