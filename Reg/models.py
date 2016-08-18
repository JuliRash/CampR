from django.db import models
from django.utils import timezone

# Create your models here.

#members
class Member(models.Model):
	First_Name = models.CharField(max_length=250)
	Last_Name = models.CharField(max_length=250)
	Adress = models.CharField(max_length=300)
	Phone = models.CharField(max_length=11)
	Email = models.EmailField()
	Single = 'S'
	Married = 'M'
	Engaged = 'E'
	Marital_choice = (
		               (Single,'Single'),
		               (Married , 'Married'),
		               (Engaged , 'Engaged'),
		            )
	Marital_Status = models.CharField(max_length=1 , choices=Marital_choice)
	Male = 'M'
	Female = 'F'
	Gender_choices = (
       (Male , 'Male') , 
       (Female , 'Female' ) , 
		)
	Gender = models.CharField(max_length=1 , choices=Gender_choices)
	Believer = models.BooleanField()
	Registered = models.BooleanField()
	Branch = models.CharField(max_length=300)
	Date_registered = models.DateTimeField(default=timezone.now)

