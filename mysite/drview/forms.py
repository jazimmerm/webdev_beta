from django import forms
from .models import Appointments
from dal import autocomplete
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.translation import gettext as _

class addAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(addAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['appt_patient'].queryset = self.user.treats.all()

    date = forms.DateField(label='Date',
                           widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder': 'Date'}))
    starts_at = forms.TimeField(label='Start Time:', widget=forms.DateInput(
        attrs={'class': 'timepicker form-control', 'placeholder': 'Start Time'}))
    ends_at = forms.TimeField(label='End Time:', widget=forms.DateInput(
        attrs={'class': 'timepicker form-control', 'placeholder': 'End Time'}))
    appt_location = forms.CharField(label='Location', max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
                                    required=False)
    reason = forms.CharField(label='Reason for Visit:', max_length=500,
                             widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Reason for Visit'}),
                             required=False)

    byweekday = forms.MultipleChoiceField(choices=Appointments.WEEKDAY_CHOICES,
                                          widget = forms.CheckboxSelectMultiple(attrs={'name':'weekday'}),
                                          required=False)

    class Meta:
        model = Appointments
        fields = ('appt_patient', 'appt_location', 'reason', 'repetition')
        exclude = ('appt_doctor', 'starts_at', 'ends_at',)
        widgets = {
            'appt_patient': autocomplete.ModelSelect2(url='drview:patient-autocomplete',
                                                      attrs={'class':'form-control',
                                                             'theme':'bootstrap',
                                                             'data-placeholder': 'Patient Name'}),
            'repetition': forms.Select(attrs = {'class':'form-control', 'data-target':'weekdayCollapse'}),
        }

    def is_valid(self):
        valid = super(addAppointmentForm, self).is_valid()
        self.cd = self.cleaned_data
        start_time = self.cd.get('starts_at')
        end_time = self.cd.get('ends_at')

        if not valid:
            raise ValidationError(_('Invalid form entry.'), code='invalid')
        elif start_time > end_time:
            raise ValidationError(_('Start time must be before end time.'), code='Bad date order')
        else:
            return True

    def save(self, weekdays = None):

        start_datetime = datetime.combine(self.cd['date'], self.cd['starts_at'])
        end_datetime = datetime.combine(self.cd['date'], self.cd['ends_at'])

        self.starts_at = start_datetime
        self.ends_at = end_datetime
        self.appt_doctor = self.user

        super(addAppointmentForm, self).save()





