from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Contactform(models.Model):

    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    organization_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20015)
    comments = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('customer:contact_us')


    def __str__(self):
        return self.name
