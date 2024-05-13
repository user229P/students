
from django.shortcuts import render, redirect
from django.contrib import messages
from ..api.invoices import fetch_all_invoices
from django.contrib.auth.decorators import login_required


def home(request):
    
    return render(request, "pages/home.html")


def loginUser(request):
    return render(request, "pages/login.html")

def signupUser(request):
    return render(request, "pages/signup.html")


@login_required
def invoices(request):
    data = fetch_all_invoices(request.user.student_id)
    context = {
        "invoices": data
    }
    return render(request, "pages/invoices.html", context)






