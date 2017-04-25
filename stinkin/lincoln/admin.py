from django.contrib import admin
from lincoln.models import Construction, Pothole, Complaint

# Register your models here.

admin.site.register(Construction)
admin.site.register(Pothole)
admin.site.register(Complaint)
