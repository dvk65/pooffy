from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'homepage.html')

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request,'results.html', {'results':res})
# Create your views here.
