from django.db import models
from django.contrib.auth.models import User

class Concern(models.Model):

    concern = models.CharField(max_length=100)

    def __str__(self):
        return self.concern

class Patient(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=256)
    primary_concern = models.ForeignKey(Concern, on_delete=models.SET_NULL, blank=True, null=True, editable=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)