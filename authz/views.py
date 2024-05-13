from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from students.api.library import register_student_to_library_account
from students.api.finance import register_student_to_finance_module

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    return render(request, 'pages/login.html')



def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        try:
            # Check if email or username already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already in use.')
            # Check if passwords match
            elif password != password2:
                messages.error(request, 'Passwords do not match.')
            else:
                # Create new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                if user:
                    eitherLibraryAccountCreatedOrNot = register_student_to_library_account(user.student_id)
                    eitherFinanceAccountCreatedOrNot = register_student_to_finance_module(user.student_id)
                    if eitherLibraryAccountCreatedOrNot and eitherFinanceAccountCreatedOrNot:
                        messages.info(request, "Student Registered to Library & Finance Module")
                    else:
                        messages.warning(request, "Student is not Registered to Library & Finance Module")
                messages.success(request, 'Registration successful. You can now login.')
                return redirect('loginUser')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    return render(request, 'pages/signup.html')



def user_logout(request):
    logout(request)
    messages.warning(request,"You're Logged Out")
    return redirect('/')

@login_required
def update_profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        try:
            # Check if email or username already exists
            if User.objects.exclude(pk=request.user.pk).filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
            elif User.objects.exclude(pk=request.user.pk).filter(username=username).exists():
                messages.error(request, 'Username is already in use.')
            else:
                # Update user profile
                user = request.user
                user.email = email
                user.username = username
                user.first_name = fname
                user.last_name = lname
                user.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    return render(request, 'pages/updateProfile.html')





def login_failled(request):
    messages.error(request,"Please login first")
    return redirect("loginUser")


@login_required
def profile(request):
    return render(request, "pages/profile.html")