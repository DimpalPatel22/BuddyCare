from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings #for Email
from django.core.mail import send_mail
from urllib.parse import quote_plus
from django.http import HttpResponse
from .models import RescueRequest
from volunteerapp.models import Volunteer

# Create your views here.
def rescue_form_view(request):
    """
    Handles rescue form for both guests and logged-in users
    without using ModelForm.
    """
    submission_message = None
    map_link = None

    if request.method == "POST":
        animal_type = request.POST.get('animal_type')
        condition = request.POST.get('condition')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        notes = request.POST.get('notes')
        image = request.FILES.get('image')

        # Simple validation
        if not animal_type or not condition or not location or not image:
            messages.error(request, "Please fill all required fields.")
        else:
            # Save to database
            rescue_request = RescueRequest(
                animal_type=animal_type,
                condition=condition,
                location=location,
                contact=contact,
                notes=notes,
                image=image
            )

            if request.user.is_authenticated:
                rescue_request.user = request.user

            rescue_request.save()

        # Create Google Maps link
            map_link = f"https://www.google.com/maps/search/?api=1&query={location.replace(' ','+')}"
            submission_message = "Rescue form submitted! Our volunteers will contact you shortly."

         # Full absolute image URL (so volunteer can click it)
            try:
                image_url = request.build_absolute_uri(rescue_request.image.url)
            except Exception:
                image_url = None
            
            # Get specific volunteers (IDs 1,2,3)
            volunteer_ids = [1, 2, 3]
            volunteer_qs = Volunteer.objects.filter(id__in=volunteer_ids)
            volunteer_emails = list(volunteer_qs.values_list('email', flat=True))
        
        # Email subject & body
            subject = f"🚨 New Rescue Request: {animal_type} ({condition})"
            message = (
                f"A new rescue has been reported!\n\n"
                f"Animal: {animal_type}\n"
                f"Condition: {condition}\n"
                f"Location: {location}\n"
                f"Google Maps: {map_link}\n"
                f"Contact: {contact if contact else 'Not provided'}\n"
                f"Notes: {notes if notes else 'None'}\n"
                f"Image: {image_url}\n\n"
                f"Please take action immediately!"
            )

            # Send email (to multiple volunteers)
            if volunteer_emails:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    volunteer_emails,
                    fail_silently=True,
                )
            # Clear POST so the form resets
            return render(request, 'rescueapp/rescue_form.html', {
                'submission_message': submission_message,
                'map_link': map_link
            })
    return render(request, 'rescueapp/rescue_form.html', {
        'submission_message': submission_message,
        'map_link': map_link
    })

def rescue_page_view(request):
     return render(request, 'rescueapp/rescue_page.html')

@login_required
def rescue_list_view(request):
    # Allow access if user is admin (staff) or volunteer
    if request.user.is_staff or getattr(request.user, 'is_volunteer', False):
        rescue_requests = RescueRequest.objects.all()
        return render(request, 'rescueapp/rescue_list.html', {'rescue_requests': rescue_requests})
    else:
        messages.warning(request, "You must be an admin or volunteer to see the rescue list.")
        return redirect('rescue_page')