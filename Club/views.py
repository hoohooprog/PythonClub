# https://docs.djangoproject.com/en/4.0/ref/request-response/
# https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/
# https://docs.djangoproject.com/en/4.0/topics/http/views/

# Add a view that returns all the resources (A5)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Club.models import Resource, Meeting


# Create your views here.
# A3 -> Create a view called "index." It doesn't need to do anything at this point 
#       but return the html path.
def index(request):

    return render(request,'index.html')

# A5 -> A view that returns all the resources
def view_resource(request):
    resource_list = Resource.objects.all()
    
    return render(request, 'resources.html',{'resource_list':resource_list})




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
    