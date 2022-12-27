from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import json

# Create your views here.
def back_office(request):
	users = User.objects.all()
	data = {
		'users': users
	}
	return render(request, 'back_office.html', data)

def create_user(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		firstname = data['firstname']
		lastname = data['lastname']
		birth_date = data['brithdate']
		User.objects.create(first_name=firstname, last_name=lastname, brith_date=birth_date)
		return HttpResponse({'status': 'ok'})