from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..api.finance import eligible_for_graduation
@login_required
def graduation_status(request):
    graduation_status = False
    eligible = eligible_for_graduation(request.user.student_id)
    if eligible:
        graduation_status = True
    
    context = {
        "graduation_status": graduation_status
    }
    return render(request, "pages/graduationStatus.html", context)