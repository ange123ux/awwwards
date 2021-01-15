from django.test import TestCase
from .models import countries,Project
from django.contrib.auth.models import User

# Create your tests here.
class countriesTestClass(TestCase):
    def setUp(self):
        self.Rwanda = countries(countries='Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.Rwanda,countries))

    def tearDown(self):
        countries.objects.all().delete()

    def test_save_method(self):
        self.Rwanda.save_country()
        country = countries.objects.all()
        self.assertTrue(len(country)>0)

    def test_delete_method(self):
        self.Rwanda.delete_country('Rwanda')
        country = countries.objects.all()
        self.assertTrue(len(country)==0)
class ProjectTestClass(TestCase):
    def setUp(self):
        self.triangle = countries(Project='triangle')

    def test_instance(self):
        self.assertTrue(isinstance(self.triangle,Project))

    def tearDown(self):
        Project.objects.all().delete()

    def test_save_method(self):
        self.Project.save_project()
        project= Project.objects.all()
        self.assertTrue(len(project)>0)

    def test_delete_method(self):
        self.triangle.delete_project('Rwanda')
        project = Project.objects.all()
        self.assertTrue(len(project)==0)
