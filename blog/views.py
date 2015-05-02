from django.template.loader import get_template
from django.shortcuts import render
from dbtest.models import *

# Create your views here.
def home(request):
	b=Person.objects.all()
	if b.first_name != "Vishal" && b.first_name != "Akshit":
		a=Person(first_name="Vishal", last_name="Tandon", jonobj="hitman")
		a.save()
		a=Person(first_name="Akshit", last_name="Agrawal", jonobj="hitman")
		a.save()
	a=Person.objects.all()
	res = []
	for i in a:
		res.append( i.first_name + " " + i.last_name )

	context = {"res":res}
	return render(request, 'index1.html', context)