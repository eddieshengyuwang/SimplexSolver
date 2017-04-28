from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'simplex/start.html')
	
def processDimensions(request):
	if request.method == 'POST':
		rows = int(request.POST['rows'])
		cols = int(request.POST['cols'])
	print(rows)
	print(cols)
	return render(request, 'simplex/insertValues.html', { 'rows' : range(rows), 'cols' : range(cols) })

def insertValues(request):
	return render(request, 'simplex/insertValues.html')