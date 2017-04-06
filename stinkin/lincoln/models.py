from django.db import models

# Create your models here.
class Contact (models.Model):
    company     = models.CharField(max_length=255)
    name        = models.CharField(max_length=255, null=True, blank=True)
    phone       = models.CharField(max_length=12, null=True, blank=True)
    def __str__ (self):
        return "{0}, {1}".format(self.name, self.company)

class Location (models.Model):
    name        = models.CharField(max_length=255)
    slug        = models.SlugField()
    def __str__ (self):
        return self.name

class Violation (models.Model):
    name        = models.CharField(max_length=255)
    slug        = models.SlugField()
    def __str__ (self):
        return self.name

class Ticket (models.Model):
    ticket_id   = models.CharField(max_length=255)
    issue_date  = models.DateTimeField()
    location    = models.ForeignKey(Location)
    violation   = models.ForeignKey(Violation)
    def __str__ (self):
        return self.ticket_id

class Construction (models.Model):
    area        = models.CharField(max_length=255)
    reason      = models.CharField(max_length=255)
    close_date  = models.DateField()
    open_date   = models.DateField()
    contacts    = models.ManyToManyField(Contact)
    more_info   = models.TextField(null=True, blank=True)
    shape       = models.TextField(null=True, blank=True)
    def __str__ (self):
        return self.area

class Pothole (models.Model):
    address     = models.CharField(max_length=255)
    report_date = models.DateField()
    def __str__ (self):
        return self.address
