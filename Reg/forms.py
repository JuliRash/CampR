from django import forms
from django.forms import ModelForm
from .models import *


#add members
class AddMembers(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['First_Name' , 'Last_Name' , 'Phone' , 'Email' , 'Adress' , 'Marital_Status' , 'Believer' , 'Gender','Branch' , 'Registered']
