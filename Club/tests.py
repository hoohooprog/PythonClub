from django.test import TestCase
from .models import Resource, Meeting, Meeting_minutes, Event
# https://docs.djangoproject.com/en/4.0/topics/testing/overview/
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
# https://python-course.eu/oop/inheritance.php
# https://docs.python.org/3/library/unittest.html#organizing-tests

# Create your tests here.
# ModelTest subclasses(inherits) TestCase
#Class ModelTest(TestCase):
    
    # unittest looks for functions with name start with test
    
    # this first test tests that __str__() function returns the type
    # name as specified for object
    #def test_string(self):
        #type = ModelAttr(attrname = "arg")
        #self.assertEqual(str(type), type.attrname)
    
    # second test checks that meta class has correct name for table
    #def test_table(self):
        #self.assertEqual(str(ProductType._meta.db_table),'producttype')
