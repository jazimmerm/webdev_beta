from django.contrib import admin
from .models import Doctor, Specialty, Appointments
from patientview.models import Patient

class SpecialtyInline(admin.TabularInline):
    model = Doctor.specialties.through

class TreatsInline(admin.TabularInline):
    model = Doctor.treats.through

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('last_name', 'user',)}

    inlines = [
        TreatsInline,
    ]
    exclude = ('treats',)

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):

    inlines = [
        SpecialtyInline,
    ]
    exclude = ('specialties',)

class AppointmentsInline(admin.TabularInline):
    model = Appointments
    extra = 1


class AppointmentDocAdmin(admin.ModelAdmin):
    inlines = (AppointmentsInline,)

class AppointmentPatientAdmin(admin.ModelAdmin):
    inlines = (AppointmentsInline,)

admin.site.unregister(Doctor)
admin.site.register(Doctor, AppointmentDocAdmin)
admin.site.register(Patient, AppointmentPatientAdmin)
