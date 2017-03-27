from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc

def home(request):
	return render(request, 'docs/home.html', {})

def trial(request):
	return render(request, 'docs/trials.html', {})

def trial_detail(request):
	return render(request, 'docs/trial_details.html', {})

def case(request):
	return render(request, 'docs/cases.html', {})
