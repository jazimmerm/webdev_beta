from django.db import models
from django.contrib.auth.models import User
from patientview.models import Patient
from django.utils.translation import gettext as _

class Specialty(models.Model):

    specialty = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.specialty

class Doctor(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=256)
    specialties = models.ManyToManyField(Specialty,  blank=True, related_name='specialty_of')
    treats = models.ManyToManyField(Patient, blank=True, related_name='treated_by')
    appts = models.ManyToManyField(Patient, through='Appointments')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return ('{} {}'.format(self.first_name, self.last_name))

class Appointments(models.Model):
    #Choices for dropdown and repetition.
    NONE = ''
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    REPETITION_CHOICES = [
        (NONE, _('Repeat:')),
        (DAILY, _('Daily')),
        (WEEKLY, _('Weekly')),
        (MONTHLY, _('Monthly')),
    ]
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    WEEKDAY_CHOICES = [
        (MONDAY, _('Mon')),
        (TUESDAY, _('Tues')),
        (WEDNESDAY, _('Wed')),
        (THURSDAY, _('Thurs')),
        (FRIDAY, _('Fri')),
    ]

    #Model Fields
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    appt_location = models.CharField(max_length=100, null=True)
    appt_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appt_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    reason = models.TextField(max_length=256, null=True)
    rrule = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return "{0} - {1}: {2} Appointment with {3}".format(self.starts_at, self.ends_at, self.appt_doctor,  self.appt_patient)