from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.role}'

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_id': self.id})
