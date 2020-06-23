from drview.models import Doctor, Specialty, Appointments
from patientview.models import Patient

class makePatientContext(object):
    def __init__(self, request):
        self.user = request.user.id

    def patients(self):
        patientlist = []
        self.doctor = Doctor.objects.get(user_id=self.user)
        treating = self.doctor.treats.all()
        for x in treating:
            patient = {'patient_name': '{0} {1}'.format(x.first_name, x.last_name),
             'patient_concern': 'Concern: {}'.format(x.primary_concern)}
            patientlist.append(patient)
        return (patientlist)

    def appointments(self):
        appointmentlist = []
        appts = Appointments.objects.all().filter(appt_doctor_id=self.doctor.pk).order_by('-starts_at')
        for y in appts:
            patient = Patient.objects.get(pk=y.appt_patient_id)
            appointment = {'patient_name': '{0} {1}'.format(patient.first_name, patient.last_name),
                           'time_start': y.starts_at,
                           'time_end': y.ends_at,
                           'location': y.appt_location,
                           'reason': y.reason[:30],
                           'patient_concern': patient.primary_concern,
                           'rrule_str': y.rrule,
                           }
            appointmentlist.append(appointment)

        return (appointmentlist)