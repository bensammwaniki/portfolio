from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import *
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api


# Create your views here.
def home(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')
