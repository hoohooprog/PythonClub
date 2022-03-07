from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resource',views.view_resource,name='resource'),
    path('meetings', views.getMeetings, name='meetings_list'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]