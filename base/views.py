from django.shortcuts import render
from django.http import HttpResponse
from base.models import user




def home(request):
	return render(request, 'home.html')
# Create your views here.
def error(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user(username=username, password=password).save()
		msg="data stored succesfully"
		return render(request, 'error.html')
	else:
		return HttpResponse("<h1>404-notfound<h1>")
