# Generated by Django 3.0.7 on 2020-06-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0003_auto_20200607_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_name',
            field=models.IntegerField(choices=[(0, 'Dr.Sharma'), (1, 'Dr.Vinay')]),
        ),
    ]
