# Generated by Django 5.0.4 on 2024-05-08 00:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_title', models.CharField(max_length=55)),
                ('c_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c_description', models.TextField()),
                ('c_instructor', models.CharField(max_length=50)),
                ('c_enrolledBy', models.ManyToManyField(related_name='enrolled_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
