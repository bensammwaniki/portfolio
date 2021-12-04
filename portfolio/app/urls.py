from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("about", views.about),
    path("contacts", views.contact),
    path("project", views.project),
]