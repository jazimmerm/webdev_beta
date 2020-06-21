from django.contrib import admin
from .models import Patient, Concern
from drview.models import Appointments, Doctor
from django.contrib.auth.models import User

class TreatedByInline(admin.TabularInline):
    model = Patient.treated_by.through

class PatientAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('last_name', 'user',)}

    inlines = [
        TreatedByInline,
    ]

class AppointmentsInline(admin.TabularInline):
    model = Appointments
    extra = 1

class AppointmentDocAdmin(admin.ModelAdmin):
    inlines = (AppointmentsInline,)

class AppointmentPatientAdmin(admin.ModelAdmin):
    inlines = (AppointmentsInline,)

admin.site.unregister(Doctor)
admin.site.unregister(Patient)
admin.site.register(Doctor, AppointmentDocAdmin)
admin.site.register(Patient, AppointmentPatientAdmin)