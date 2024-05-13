from authz.models import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.shortcuts import redirect, get_object_or_404
from ..api.invoices import new_invoice, delete_invoice
from django.db.models import Q

def allCourses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "pages/courses.html", context)

@login_required
def checkout_course(request, c_id):
    course = Course.objects.get(c_id=c_id)
    enrollment = False
    if Enrollment.objects.filter(e_course=course, e_user=request.user).exists():
        enrollment = True
    context = {
        "course": course,
        "enrollment": enrollment
    }
    return render(request, "pages/courseCheckout.html", context)


def find_courses(request):
    if request.method=='POST':
        
        query = request.POST.get('course')
        if query:
            
            courses = Course.objects.filter(Q(c_title__icontains=query))
        else:
            courses = None

        return render(request, 'pages/courses.html', {'courses': courses})


@login_required
def enroll_course(request, c_id):
    try:
        course = Course.objects.get(pk=c_id)
    except Course.DoesNotExist:
        messages.error(request, 'Course not found')
        return redirect('courses')
    enrollmentExist = Enrollment.objects.filter(e_course=course, e_user=request.user).exists()
    if enrollmentExist:
        messages.error(request, f'You are already enrolled in this course - Invoice: {enrollmentExist.e_reference}')
        return redirect('course_checkout', c_id=c_id)

    data = new_invoice(float(course.c_price), 'TUITION_FEES', request.user.student_id)
    if data['invoice_created']:
        course.c_enrolledBy.add(request.user)
        reference = data['invoice_reference']
        enrollment = Enrollment.objects.create(
            e_reference=reference,
            e_course=course,
            e_user=request.user
        )
        messages.success(request, f'Successfully enrolled in the course - Invoice: {reference}')
    else:
        messages.error(request, "Failed to create invoice for course")
    return redirect('course_checkout', c_id=c_id)

@login_required
def my_enrolled_courses(request):
    # Get all courses enrolled by the current user
    enrolled_courses = Course.objects.filter(c_enrolledBy=request.user)

    context = {
        'courses': enrolled_courses
    }
    print(context)
    return render(request, "pages/courses.html", context)

@login_required
def cancel_enrollment(request, c_id):
    course = get_object_or_404(Course, pk=c_id)
    enrollment = Enrollment.objects.filter(e_user=request.user, e_course=course).first()
    if enrollment:
        data = delete_invoice(enrollment.e_reference)
        print(data)
        if data['status'] == 200:
            
            enrollment.delete()
            course.c_enrolledBy.remove(request.user)
            messages.success(request, 'Successfully canceled enrollment.')
        else:
            messages.warning(request,"Failed to cancel invoice")
    else:
        messages.error(request, 'You are not enrolled in this course.')
    
    return redirect('course_checkout', c_id=c_id) 
