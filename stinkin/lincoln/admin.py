from django.contrib import admin
from lincoln.models import Contact, Location, Violation, Ticket, Construction, Pothole

# Register your models here.

admin.site.register(Contact)
admin.site.register(Location)
admin.site.register(Violation)
admin.site.register(Ticket)
admin.site.register(Construction)
admin.site.register(Pothole)
