from django.test import TestCase
from .models import *
# Create your tests here.

class ProjectsTestCase(TestCase):
    def setUp(self, project_name='GitSearch', project_photo='lol.jpg', description='some description', github_repo='git repo', url='lol.com', owner='Mercurial'):
        return Projects.objects.create(project_name=project_name, project_photo=project_photo, description=description, github_repo=github_repo, url=url, owner=owner)

    def projectSave(self):
        initialization = self.setUp()
        self.assertTrue(save > 0)

