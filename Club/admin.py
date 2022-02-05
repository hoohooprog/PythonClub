from django.contrib import admin
from .models import Meeting, Meeting_minutes, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Meeting_minutes)
admin.site.register(Resource)
admin.site.register(Event)
