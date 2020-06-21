from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import allowed_roles_redirect
from .static.drview.pyscripts.script_snippets import makePatientContext
from .forms import addAppointmentForm
from .models import Doctor
from patientview.models import Patient
from dal import autocomplete
from django.db.models import Q
import json

@login_required
@allowed_roles_redirect(['doctor'])
def home(request):
    context = {}
    patientcontext = makePatientContext(request)
    context['patientexample'] = patientcontext.patients()
    context['appointments'] = patientcontext.appointments()
    return render(request, 'drview/dr_home.html', context=context)

def schedule(request):
    context = {}
    patientcontext = makePatientContext(request)
    doc = Doctor.objects.get(user_id=request.user.pk)
    if request.method == 'POST':
        form = addAppointmentForm(data=request.POST, user=doc)
        if form.is_valid():
            weekdays = request.POST.getlist('byweekday')
            form.save(weekdays = weekdays)
    else:
        form = addAppointmentForm(user=doc)
    context['apptform'] = form
    context['patientexample'] = patientcontext.patients()
    context['appointments'] = patientcontext.appointments()

    return render(request, 'drview/calendar_view.html', context=context)

class patientAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Patient.objects.none()

        doc = Doctor.objects.get(user_id = self.request.user.pk)
        qs = doc.treats.all()
        if self.q:
            qs = qs.filter(Q(first_name__icontains=self.q)|Q(last_name__icontains=self.q))

        return qs