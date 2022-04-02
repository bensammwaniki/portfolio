from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    # path("bookings", views.save_send_mail, name='bookings'),
    path("testmonials", views.testmony, name='testmonials')
]
