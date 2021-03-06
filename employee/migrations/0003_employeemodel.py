# Generated by Django 3.2.8 on 2021-10-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_customuser_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('dob', models.DateField(null=True)),
                ('mobile_no', models.CharField(max_length=13)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
