from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('header/', TemplateView.as_view(template_name="Header.html"))
]
