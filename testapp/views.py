from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    #return HttpResponse("heheheh")
    return render(request,'index.html')

def contact(request):
    return HttpResponse("this is contact page ")

def about(request):
    return render(request,'about.html')

