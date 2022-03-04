from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    """class defining a Meeting model, referencing Model class object """

	#  fields for meeting title, meeting date, meeting time, location, Agenda
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=255)
    meeting_agenda = models.TextField()
	
	# Django will automatically assign an id autonumbered field as a primary key,
	# using BigAutoField
	
	


	# Metadata
    class Meta:
        """anything that's not a field, such as ordering options (ordering), 
	   database table name (db_table), or human-readable singular and plural names 
	   (verbose_name and verbose_name_plural).
		"""
        db_table = "meeting"
        verbose_name_plural = "meetings"

	# Methods
	# get_absolute_url(), which returns a URL for displaying individual model 
	# records on the website
    def get_absolute_url(self):
		
        """Returns the url to access a particular instance of Meeting.
		   ie url of id, /myapplication/mymodelname/2; helpful for testing on admin"""

        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):

        """String for representing the Meeting object (in Admin site)"""

        return self.meeting_title
	

class Meeting_minutes(models.Model):
	"""class defining a Meeting Minutes model, referencing Model class object"""

	# fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text
	meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
	attendance = models.ManyToManyField(User)
	minutes = models.TextField()

	# Metadata
	class Meta:
		"""anything that's not a field, such as ordering options (ordering), 
	   database table name (db_table), or human-readable singular and plural names 
	   (verbose_name and verbose_name_plural).
		"""
		db_table = "meeting_minutes"
		verbose_name_plural = "meeting_minutes"

	# Methods
	# get_absolute_url(), which returns a URL for displaying individual model 
	# records on the website
	def get_absolute_url(self):
		
		"""Returns the url to access a particular instance of Meeting.
		   ie url of id, /myapplication/mymodelname/2"""

		return reverse('meeting-mins-view', args=[str(self.id)])

	def __str__(self):

		"""String for representing the Meeting_minutes object (in Admin site)"""

		return self.meeting_id



class Resource(models.Model):
    """class defining a Resource model, referencing Model class object"""

    # fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    URL = models.URLField(null=True, blank=True)
    date_entered = models.DateField()
    user_entered = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()
	
    # Metadata
    class Meta:
        """anything that's not a field, such as ordering options (ordering), 
        database table name (db_table), or human-readable singular and plural names 
	   (verbose_name and verbose_name_plural).
        """
        db_table = "resource"
        verbose_name_plural = "resources"

	# Methods
	# get_absolute_url(), which returns a URL for displaying individual model 
	# records on the website
    def get_absolute_url(self):
	    
        """Returns the url to access a particular instance of Meeting.
            ie url of id, /myapplication/mymodelname/2"""

        return reverse('resource-info-view', args=[str(self.id)])

    def __str__(self):

        """String for representing the Resource object (in Admin site)"""

        return self.resource_name


class Event(models.Model):
    """class defining a Meeting model, referencing Model class object"""

    # fields for event title, location, date, time, description and the user id of the member that posted it

    event_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    user_entered = models.ForeignKey(User, on_delete=models.DO_NOTHING)


	# Metadata
    class Meta:
        """anything that's not a field, such as ordering options (ordering), 
	   database table name (db_table), or human-readable singular and plural names 
	   (verbose_name and verbose_name_plural).
		"""
        db_table = 'event'
        verbose_name_plural = 'events'

	# Methods
	# get_absolute_url(), which returns a URL for displaying individual model 
	# records on the website
    def get_absolute_url(self):
		
        """Returns the url to access a particular instance of Meeting.
		   ie url of id, /myapplication/mymodelname/2"""

        return reverse('event-info-view', args=[str(self.id)])

    def __str__(self):

        """String for representing the Event object (in Admin site)"""

        return self.event_title

# references (diagrams, docs, tutorials etc) for the knowledge used in this file?