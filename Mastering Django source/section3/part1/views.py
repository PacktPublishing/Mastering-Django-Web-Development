from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(req):
	context = {
		"name": "matt", 
		"now": datetime.now(),
		"publisher": "Packt"
		}

	return render(req, 'index.html', context)