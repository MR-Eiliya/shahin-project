from django.urls import path
from mainapp.views import *
from django.conf import settings

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('contact',contact_view,name='contact'),
    path('about',about_view,name='about'),
    path('newsletter', newsletter_view, name='newsletter')


]
