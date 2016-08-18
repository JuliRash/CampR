from django.shortcuts import render
from django.contrib.auth.models import User , Group
from rest_framework import viewsets
# from .serializers import UserSerializers ,GroupSerializers
from django.http import HttpResponseRedirect
from .forms import *
import operator
from .models import Member as q

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
# 	queryset = User.objects.all().order_by('-date_joined')
# 	serializer_class = UserSerializers

# class GroupViewSet(viewsets.ModelViewSet):
# 	queryset = Group.objects.all()
# 	serializer_class = GroupSerializers
def index(request):
	return render(request , 'content/index.html' , {})

#adding a member view
def AddMember(request):
	if request.method == 'GET':
		form = AddMembers()
	else:
		form = AddMembers(request.POST)
		if form.is_valid():
			First_Name = form.cleaned_data['First_Name']
			Last_Name = form.cleaned_data['Last_Name']
			Phone   = form.cleaned_data['Phone']
			Adress = form.cleaned_data['Adress']
			Email = form.cleaned_data['Email']
			Marital_status = form.cleaned_data['Marital_Status']
			Gender = form.cleaned_data['Gender']
			Believer = form.cleaned_data['Believer']
			Registered = form.cleaned_data['Registered']
			Branch = form.cleaned_data['Branch']
			Add = form.save()
			return HttpResponseRedirect('/website/index/')
	return render(request , 'content/add.html' ,{'form':form})


