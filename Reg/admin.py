from django.contrib import admin
from . models import *

class MemberView(admin.ModelAdmin):
	model = Member
	list_display = ['First_Name'  , 'Last_Name', 'Phone' , 'Email' , 'Adress' , 'Marital_Status' , 'Believer' , 'Gender' , 'Branch' , 'Date_registered']
	search_fields = ['First_Name' , 'Email']
	list_filter =  ['First_Name' , 'Last_Name' , 'Phone' , 'Email' , 'Adress' , 'Marital_Status' , 'Believer' , 'Gender' , 'Branch']
# Register your models here.
admin.site.register(Member , MemberView)