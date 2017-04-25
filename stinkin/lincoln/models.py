from django.db import models

# Create your models here.

class Construction (models.Model):
    area        = models.CharField(max_length=255)
    reason      = models.CharField(max_length=255)
    close_date  = models.DateField()
    open_date   = models.DateField()
    more_info   = models.TextField(null=True, blank=True)
    shape       = models.TextField(null=True, blank=True)
    def __str__ (self):
        return self.area

class Pothole (models.Model):
    not_id      = models.CharField(max_length=255)
    report_date = models.DateField()
    status      = models.CharField(max_length=255)
    location    = models.CharField(max_length=255, null=True, blank=True)
    district    = models.CharField(max_length=255, null=True, blank=True)
    source      = models.CharField(max_length=255, null=True, blank=True)
    latitude    = models.DecimalField(max_digits=50, decimal_places=10, null=True, blank=True)
    longitude   = models.DecimalField(max_digits=50, decimal_places=10, null=True, blank=True)
    def __str__ (self):
        return self.location

class Complaint (models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    problem = models.TextField()
    def __str__ (self):
        return self.email
