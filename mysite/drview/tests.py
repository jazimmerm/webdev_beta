from django.contrib.auth.models import User
from drview.models import Doctor, Specialty, Patient, Appointments
import datetime

# for creating user instances must use Doctor.objects.create(user=USERINSTANCE)

momdoc = Doctor.objects.get(name='Cindy')
pat = Patient.objects.get(name='pat')

st = datetime.datetime(2020, 5, 15,  14, 0, 0, 0)
et = datetime.datetime(2020, 5, 15,  16, 0, 0, 0)

appt1 = Appointments.objects.create(starts_at = st, ends_at = et, appt_location = 'West Palm', appt_doctor=momdoc, appt_patient=pat, reason='Legs')

appt1.save()





