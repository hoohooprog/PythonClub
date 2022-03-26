from django.urls import path

from . import views
# path('user_entered_url_endpoint', views.Method, name='name_of_this_path')

urlpatterns = [
    path('', views.index, name='index'),
    path('resource',views.view_resource,name='resource'),
    path('meetings', views.getMeetings, name='meetings_list'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newResource', views.newResource, name='resourceForm' ),
    path('newMeeting', views.newMeeting, name='meetingForm'),
    path('loginmessage', views.loginmessage, name='loginmessage'),
    path('logoutmessage',views.logoutmessage, name='logoutmessage'),

]