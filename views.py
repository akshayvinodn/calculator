from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    if request.method=='POST':

        a=int(request.POST['num1'])
        
        b=int(request.POST['num2'])
        
        d=b-a
        
        
        return HttpResponse(d)
    return render(request,'index.html')

def register(request):
    return render(request,'reg.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
