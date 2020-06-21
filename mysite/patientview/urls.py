from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'patientview' #for namespacing of urls

urlpatterns = [path('', RedirectView.as_view(url = '/patient-portal/home'), name = 'go-to-home'),
               path('home/', views.home, name = 'homepage'),
               ]