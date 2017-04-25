from django.shortcuts import render, redirect
from lincoln.models import Pothole, Complaint
from lincoln.forms import ComplaintForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/submission')
    else:
        form = ComplaintForm()
        potholes = Pothole.objects.exclude(longitude__isnull=True)
        context = {'form' : form, 'potholes':potholes}
        return render(request, 'lincoln/index.html', context)

def thanks(request):
    return render(request, 'lincoln/thanks.html')

def snitches(request):
    complaints = Complaint.objects.all()
    return render(request, 'lincoln/snitches.html', {'complaints':complaints})
