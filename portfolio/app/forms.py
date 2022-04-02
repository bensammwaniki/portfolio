from django.forms import ModelForm
from .models import GetInTouch

class ContactForm(ModelForm):
    class Meta:
        model = GetInTouch
        fields = '__all__'