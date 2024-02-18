# Generated by Django 3.1.5 on 2024-02-16 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0002_hostelallotment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_num', models.CharField(max_length=20)),
                ('reason', models.TextField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
            ],
        ),
    ]
