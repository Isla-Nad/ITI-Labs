from django.urls import path
from contacts.views import contact_us, about_us

urlpatterns = [
    path('contact', contact_us, name='contacts.contact'),
    path('about', about_us, name='contacts.about'),
]
