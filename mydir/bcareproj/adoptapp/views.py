from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import AdoptionRequest

# Create your views here.

def adopt_page(request):
    return render(request, 'adoptapp/adopt_page.html')
def adopt_form(request):
    pet_name = request.GET.get('pet', '') 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason') 
        AdoptionRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            pet_name=pet_name,
            reason=reason
        )
        return redirect('adopt_success')
    return render(request, 'adoptapp/adopt_form.html', {'pet_name': pet_name})

def adopt_success(request):
    return render(request, 'adoptapp/adopt_success.html')
