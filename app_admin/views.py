from django.shortcuts import render

# Create your views here.


from django.contrib import admin
from .models import Users

admin.site.register(Users)
