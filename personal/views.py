from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'personal/home.html') 
	#render looks at template directory

def contact(request):
	return render(request, 'personal/basic.html', {'content' : ['If you would like to contatct me, please email me','es2wang@edu.uwaterloo.ca']})
