from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index-meetups'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
