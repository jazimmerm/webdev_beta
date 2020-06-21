from drview.models import Doctor, Specialty, Appointments
from patientview.models import Patient

def makePatientContext(request):
    user = request.user.id
    patients = []
    appointments = []
    doctor = Doctor.objects.get(user_id=user)
    treating = doctor.treats.all()
    appts = Appointments.objects.all().filter(appt_doctor_id=doctor.pk).order_by('-starts_at')
    for x in treating:
        patient = {'patient_name': '{0} {1}'.format(x.first_name, x.last_name),
         'patient_concern': 'Concern: {}'.format(x.primary_concern)}
        patients.append(patient)
    for y in appts:
        patient = Patient.objects.get(pk=y.appt_patient_id)
        appointment = {'patient_name': '{0} {1}'.format(patient.first_name, patient.last_name),
                       'time_start': y.starts_at,
                       'time_end': y.ends_at,
                       'location': y.appt_location,
                       'reason': y.reason[:30],
                       'patient_concern': patient.primary_concern,
                       'rrule_repetition': y.repetition,
                       'rrule_byweekday': y.byweekday
                       }
        appointments.append(appointment)

    context = {
            'Title': 'Doctor Portal Home',
            'patientexample': patients,
            'appointments': appointments,
    }

    return context