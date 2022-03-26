from django.test import TestCase
from .models import Resource, Meeting, Meeting_minutes, Event
# https://docs.djangoproject.com/en/4.0/topics/testing/overview/
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
# https://python-course.eu/oop/inheritance.php
# https://docs.python.org/3/library/unittest.html#organizing-tests

# in case can't create db to test because user is not authorized,
# copy code from link with username into pgadmin shell
# https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni


# Create your tests here.
# ModelTest subclasses(inherits) TestCase
# Class ModelTest(TestCase):
    
    # unittest looks for functions with name start with test
    
    # this first test tests that __str__() function returns the type
    # name as specified for object
    # def test_string(self):
        # type = ModelAttr(attrname = "arg")
        # self.assertEqual(str(type), type.attrname)
    
    # second test checks that meta class has correct name for table
    # def test_table(self):
        # self.assertEqual(str(ProductType._meta.db_table),'producttype')




"""
    testing Meeting model
"""
class MeetingTest(TestCase):
    # set up one time sample data
    def setup(self):
        meetingTest = Meeting(meeting_title='test meet', meeting_date ='3/26/2022',
            meeting_time = '2:19PM', meeting_location='Seattle',meeting_agenda='planning fall quarter')
        return meetingTest

    def test_str(self):
        meetingTest = self.setup()
        # str(meetingObj) = nameRepresentation of meetingObj
        self.assertEqual(str(meetingTest), meetingTest.meeting_title)
        
    def test_table(self):
        demo_meet = self.setup()

        self.assertEqual(Meeting._meta.db_table,'meeting')
"""
    testing Meeting_minutes model 
"""
class Meeting_minutesTest(TestCase):
    # set up one time sample data
    def setup(self):
        # ? how to test FK and many-many fields ?
        meeting_minutesTest = Meeting_minutes()
        return meeting_minutesTest
    def test_table(self):
        self.assertEqual(Meeting_minutes._meta.db_table,'meeting_minutes')

    def test_tables(self):
        self.assertEqual(Meeting_minutes._meta.verbose_name_plural,'meeting_minutes')

"""
    testing Resource model
"""
class ResourceTest(TestCase):

    def setup(self):
        resourceTest = Resource('testResource','test','abc.org',
            '3/26/2022',4,'this is test data')
        return resourceTest

    def test_table(self):
        self.assertEqual(Resource._meta.db_table,'resource')
        self.assertEqual(Resource._meta.verbose_name_plural,'resources')

    def test_repr(self):
        resourceTest = self.setup()
        self.assertEqual(str(resourceTest),resourceTest.resource_name)

"""
    testing Event model
"""
class EventTest(TestCase):
    def setup(self):
        eventTest = Event('test_event','seattle','3/26/2022',
            '3:34PM','this is a test', 10)
        return eventTest

    def test_table(self):
        self.assertEqual(Event._meta.db_table,'event')

    def test_repr(self):
        eventTest = self.setup()
        self.assertEqual(str(eventTest), eventTest.event_title)
