from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            # Redirect to a success page or dashboard
            return redirect('dashboard')
        else:
            # Invalid credentials, display error message
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login_user')

    # If request method is GET, render the login form
    return render(request, 'login.html')
