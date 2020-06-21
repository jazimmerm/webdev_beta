from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles_redirect

# Create your views here.
@login_required
@allowed_roles_redirect(['patient'])
def home(request):
    return render(request, 'patientview/patient_home.html')