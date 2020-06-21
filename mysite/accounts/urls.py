from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'accounts' #for namespacing of urls

urlpatterns = [path('', RedirectView.as_view(url = '/accounts/login/'), name = 'go-to-login'),
               path('signup/', views.register, name = 'Register'),
               path('login/', views.userLogin, name = 'login'),
               path('logout/', views.logout_view, name = 'logout')
               ]