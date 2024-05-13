from django.db import models

# Create your models here.
import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models


# Generate a unique student ID
def generate_student_id():
    unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return unique_id

class User(AbstractUser):
    student_id = models.CharField(max_length=6, unique=True, editable=False)
    def save(self, *args, **kwargs):
        if not self.student_id:
            # Generate student ID if not provided
            self.student_id = generate_student_id().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_title = models.CharField(max_length=55)
    c_price = models.DecimalField(max_digits=10, decimal_places=2)
    c_enrolledBy = models.ManyToManyField(User, related_name='enrolled_courses')
    c_description = models.TextField()
    c_instructor = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return self.c_title

class Enrollment(models.Model):
    e_reference = models.CharField(max_length=100, blank=False, null=False)
    e_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    e_user = models.ForeignKey(User, on_delete=models.CASCADE)
    e_time = models.DateField(auto_now_add=True)
    e_note = models.CharField(max_length=200, default="", blank=True, null=True)


    def __str__(self):
        return f"Enrollment: {self.e_reference} - Student: {self.e_user.username}"