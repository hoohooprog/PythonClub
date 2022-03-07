from socket import fromshare
from django import forms
from .models import Resource, Meeting

# Create a form to add a resource and a form to add a meeting (A8)
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
