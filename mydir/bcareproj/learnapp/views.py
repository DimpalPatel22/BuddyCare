from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import UserTips

# Create your views here.
def learn_home(request):
    approved_tips = UserTips.objects.filter(status='approved').order_by('-submitted_at')
    return render(request, 'learnapp/learn.html',{'tips': approved_tips})

def emergency(request):
    return render(request, 'learnapp/emergency.html')

def food(request):
    return render(request, 'learnapp/food.html')

def owner(request):
    return render(request, 'learnapp/newowner.html')

def health(request):
    return render(request, 'learnapp/health.html')

def dangerous(request):
    return render(request, 'learnapp/dangerous.html')

@login_required
def tipform(request):
    """
    Handle user tip submission (only for logged-in users).
    """
    if request.method == "POST":
        username = request.POST.get("username") or request.user.username
        email = request.POST.get("email", "").strip()
        tip_type = request.POST.get("tip_type")
        other_text = request.POST.get("other_text", "").strip()
        tip_text = request.POST.get("tip_text", "").strip()

        # If user chose "Other", replace tip_type with their custom text
        if tip_type == "other" and other_text:
            tip_type = other_text

        if tip_text:  # only save if tip is not empty
            UserTips.objects.create(
                user=request.user,
                username=username,
                email=email,
                tip_type=tip_type,
                other_text=other_text,
                tip_text=tip_text,
            )

            # After saving, show success box
            return render(request, "learnapp/tipform.html", {
                "submitted": True,
                "username": username,
                "tip_type": tip_type,
            })
    return render(request, 'learnapp/tipform.html')