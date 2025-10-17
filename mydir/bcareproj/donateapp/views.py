from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Donation

def donate_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "If you want to donate our humble Mitra, please login first 🐾")
        login_url = f"{reverse('login')}?next={request.path}"
        return redirect(login_url)
    
    if request.method == 'POST':
        donation_type = request.POST.get('donation_type')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        amount = request.POST.get('amount')

        # Save online donation
        if donation_type == 'online' and name and amount:
            return render(request, "donateapp/payment.html", {
                "name": name,
                "amount": amount
            })
        elif donation_type == 'offline':
            return redirect(f"/donate/offline/?name={name}&contact={contact}")
    
    return render(request, 'donateapp/donate.html')

def payment_view(request):
    """Show payment options page (in case accessed directly)."""
    name = request.GET.get("name", "")
    amount = request.GET.get("amount", "")
    return render(request, "donateapp/payment.html", {"name": name, "amount": amount})
    
def offline_donate(request):
    if not request.user.is_authenticated:
        messages.info(request, "If you want to donate our humble Mitra, please login first 🐾")
        return redirect('login')

    # Pre-fill from GET params
    name = request.GET.get('name', '')
    contact = request.GET.get('contact', '')

    if request.method == 'POST':
        item = request.POST.get('item')
        notes = request.POST.get('notes')
        expiry_confirm = bool(request.POST.get('expiry_confirm'))

        Donation.objects.create(
            user=request.user,
            name=name,
            contact=contact,
            donation_type='offline',
            item=item,
            notes=notes,
            expiry_confirm=expiry_confirm
        )
        messages.success(request, "Thank you for your offline donation! Please visit our center 🐾")
        return redirect('donation_success')

    return render(request, 'donateapp/offline_donate.html', {'name': name, 'contact': contact})

def donation_success(request):
    return render(request, 'donateapp/donate_success.html')


def process_payment(request):
    """Handle payment & OTP logic."""
    if request.method == "POST":
        otp = request.POST.get("otp", None)

        if otp:  # OTP submitted → save donation
            name = request.POST.get("name")
            amount = request.POST.get("amount")
            method = request.POST.get("method")

            Donation.objects.create(
                user=request.user,
                name=name,
                contact=request.user.email,
                donation_type='online',
                online_method=method,
                amount=amount
            )
            messages.success(request, f"Your {method} payment of ₹{amount} was successful! 💖")
            return redirect("donation_success")
        else:
            return redirect('donate')
    return redirect("donate")
