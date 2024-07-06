from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Vishal Admin"
admin.site.site_title = "Vishal Admin Portal"
admin.site.index_title = "Welcome to Vishal Researcher Portal"

urlpatterns = [
    path("", views.index, name="home"),  # Root URL for the homepage
    path("about/", views.about, name="about"),  # Separate path for the about page
    path("services/", views.services, name="services"),  # Separate path for the about page
    path("contact/", views.contact, name="contact"),  # Separate path for the about page
]
