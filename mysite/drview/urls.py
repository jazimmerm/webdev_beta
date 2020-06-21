from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'drview' #for namespacing of urls

urlpatterns = [path('', RedirectView.as_view(url = '/dr-portal/home'), name = 'go-to-home'),
               path('home/', views.home, name = 'homepage'),
               path('calendar/', views.schedule, name = 'calendar'),
               path('patient-autocomplete/', views.patientAutoComplete.as_view(), name = 'patient-autocomplete')
               ]