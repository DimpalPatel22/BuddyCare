from django.shortcuts import render,redirect
from django.contrib import messages
from .models import VolunteerGroupRequest

# Create your views here.
#Volunteer Home Page
def volunteer_home(request):
    return render(request, 'volunteerapp/volunteer.html')

# Volunteer Join Page
def joingroup_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        group = request.POST.get('group')
        
         # Save request in DB
        VolunteerGroupRequest.objects.create(
            name=name,
            contact=contact,
            group=group
        )
        
        return render(request, 'volunteerapp/groupform.html', {
            'submitted': True,
            'name': name,
            'group': group
        })
    
    return render(request, 'volunteerapp/groupform.html',{'submitted': False})
