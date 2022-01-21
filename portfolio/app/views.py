from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

from .forms import ContactForm

from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    testmony = Testmonials.get_all_approved()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'Hi Ben, you have a new message from {form.cleaned_data["Email"]}: {form.cleaned_data["subject"]}'
            user_email = form.cleaned_data["Email"]
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            
            msg = EmailMessage(from_email= settings.CONTACT_EMAIL, to=[user_email],)
            msg.template_id = "d-790beb02e5c648e0887a1c0f572a79a6"
            msg.send(fail_silently=True)
            return redirect('/')
    form = ContactForm()
    return render(request, 'index.html',{"testmony":testmony,'form': form})
def testmony(request):
    if request.method == 'POST':
        name = request.POST['name']
        testmony = request.POST['testmony']
        position = request.POST['position']
        image = request.FILES['image']
        image = cloudinary.uploader.upload(image)
        image_url = image['url']
        image = Testmonials(name=name, testmony=testmony, image=image_url, position=position)
        image.saving()
        return render(request, 'index.html', {'success': 'Thank you!'})
    else:
        return render(request, 'index.html', {'danger': 'Sorry something went wrong'})

