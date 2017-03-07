from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc

def index(request):
	return render(request, 'docs/index.html', {})
