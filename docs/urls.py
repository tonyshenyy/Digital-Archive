from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^docs/trails.html$', views.trial, name='trial'),
	url(r'^docs/cases.html$', views.case, name='case'),
	url(r'^docs/trial_details.html$', views.trial_detail, name='trial_detail'),
]
