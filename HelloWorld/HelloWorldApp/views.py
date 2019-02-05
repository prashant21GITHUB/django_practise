from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse("Test page")

def home(request):
    my_dict = {'my_name' : 'Prashant Bajpai'}
    return render(request, "index.html", context = my_dict)
