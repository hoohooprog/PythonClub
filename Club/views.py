# https://docs.djangoproject.com/en/4.0/ref/request-response/
# https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/
# https://docs.djangoproject.com/en/4.0/topics/http/views/

# Add a view that returns all the resources (A5)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Club.models import Resource, Meeting
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required



# Create your views here.
# A3 -> Create a view called "index." It doesn't need to do anything at this point 
#       but return the html path.
def index(request):

    return render(request,'index.html')

# A5 -> A view that returns all the resources
def view_resource(request):
    resource_list = Resource.objects.all()
    
    return render(request, 'resources.html',{'resource_list':resource_list})



# function that responses to meetings.html via path in urls.py
# grabs all Meeting entities and puts them into a list called 'Meetings_list'
# renders data from Meetings_list in Meetings.html, somewhere along the way turns
# request into response
def getMeetings(request):
    Meetings_list= Meeting.objects.all()
    return render(request, 'Meetings.html', {'Meetings_list': Meetings_list})



def meetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    title = meeting.meeting_title
    date = meeting.meeting_date
    location = meeting.meeting_location
    agenda = meeting.meeting_agenda
    context = {
        'title' : title,
        'date' : date,
        'location' : location,
        'agenda' : agenda,
    }
    
    return render(request, 'meetingdetails.html', context)

@login_required
# Create a form to add a resource and a form to add a meeting (A8)
def newResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'newResource.html',{'form':form})

@login_required
def newMeeting(request):
    form = Meeting
    if request.method == 'POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'newMeeting.html',{'form':form})

def loginmessage(request):
    return render(request, 'loginmessage.html')

def logoutmessage(request):
    return render(request, 'logoutmessage.html')