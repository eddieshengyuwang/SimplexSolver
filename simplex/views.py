from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'simplex/start.html')
	
def simplexAlgo(request):
	if request.method == 'POST':
		rows = request.POST['rows']
		cols = request.POST['cols']
	print(rows)
	print(cols)
	return HttpResponse('')

def insertValues(request):
	return render(request, 'simplex/insertValues.html')