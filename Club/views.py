# https://docs.djangoproject.com/en/4.0/ref/request-response/
# https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/
# https://docs.djangoproject.com/en/4.0/topics/http/views/

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A3 -> Create a view called "index." It doesn't need to do anything at this point 
#       but return the html path.
def index(request):

    return render(request,'index.html')



