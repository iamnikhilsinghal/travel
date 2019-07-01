from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
	return render(request,'home.html',{'name':'Nik'})
	#return HttpResponse("<h1> Hello Response </h1>")
	
def result(request):
	a=int(request.POST['num1'])
	b=int(request.POST['num2'])
	c=a+b
	return render(request,'result.html',{'res':c})



# Create your views here.
