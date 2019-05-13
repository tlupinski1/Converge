from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from . import views
class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('main-home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('main-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
