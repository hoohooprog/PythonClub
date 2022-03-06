from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resource',views.view_resource,name='resource')
]