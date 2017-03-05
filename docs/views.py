from django.shortcuts import render
from django.http import HttpResponse
from .models import Docs

def index(request):
	return render(request, 'docs/index.html', {})
