from django.contrib import admin
from django.urls import path, include
from .views import funcs, courses_view, graduation_status

from django.conf import settings
from django.conf.urls.static import static
# from .views.views import 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include('authz.urls')),
    path("", funcs.home, name="home"),

    # courses urls 
    path("courses", courses_view.allCourses, name="courses"),
    path("enrolled", courses_view.my_enrolled_courses, name="enrolled"),
    path("course_checkout/<int:c_id>", courses_view.checkout_course, name="course_checkout"),
    path("enroll_course/<int:c_id>", courses_view.enroll_course, name="enroll_course"),
    path("cancel_enroll/<int:c_id>", courses_view.cancel_enrollment, name="cancel_enroll"),
    path("find_course", courses_view.find_courses, name="find_courses"),

    path("graduation_status", graduation_status.graduation_status, name="graduation_status"),    
    

    path("invoices", funcs.invoices, name="invoices"),


    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)