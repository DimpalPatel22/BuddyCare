from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            messages.success(request, "Account created successfully! 🎉")
            return redirect('home')  # go to homepage
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


# Login View
def login_view(request):
    next_url = request.GET.get('next')  # Get the 'next' parameter if it exists

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login Successfully! Welcome Back")
            
            # Redirect to next_url if exists, else to home
            redirect_to = request.POST.get('next') or next_url or 'home'
            return redirect(redirect_to)
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form, 'next': next_url})

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out")
    return redirect('home')