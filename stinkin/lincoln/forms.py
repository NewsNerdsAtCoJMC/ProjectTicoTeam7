from django.forms import ModelForm
from lincoln.models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
