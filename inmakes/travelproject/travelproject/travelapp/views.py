from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    j1 = Team.objects.all()
    return  render(request,"index.html",{'result':obj,'result1':j1})

#def about(request):
    #return  render(request,"result.html")
#def contact(request):
    #return HttpResponse("hello everybody")
#def addition(request):
    #x=int(request.GET['number1'])
    #y=int(request.GET['number2'])
    #res=x+y
    #res2=x-y
    #res3=x*y
    #res4=x/y
    #return render(request,"result.html",{'result':res,'substraction':res2,'multiplication':res3,'div':res4})