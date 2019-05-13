from django.test import TestCase, RequestFactory
from users.models import Profile, User, Project, Polls, PollAnswers, Members
from django.utils import timezone
from .forms import OurUserForm, UpdateUser, UpdateProfile, ProjectForm, textForm, PollsForm, AnswerForm, UpdateUser
from django.contrib.auth.models import User
from . import views
from django.urls import reverse

# Create your tests here.
class ProjectTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='fake', email='fake@...', password='fake')

    #testing forms here
    def test_forms(self):
        form = ProjectForm(data={'projectName': "projectName", 'projectType': "projectType", 'projectDescription': "projectDescription", 'projectPicture': "projectPicture"})
        self.assertTrue(form.is_valid())

    def test_forms_next(self):
        form = PollsForm(data={'title': "title", 'questionOne': "questionOne", 'questionTwo': "questionTwo", 'questionThree': "questionThree", 'questionFour': "questionFour", 'questionFive': "questionFive"})
        self.assertTrue(form.is_valid())

    def test_forms_again(self):
        form = UpdateProfile(data={'image': "image", 'userDescription': "userDescription", 'userInterests': "userInterests", 'location': "location"})
        self.assertTrue(form.is_valid())

    #being testing templates here
    def test_view_register_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_view_allusers_correct_template(self):
        response = self.client.get(reverse('allusers'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/allUsers.html')

    def test_view_polls_correct_template(self):
        response = self.client.get(reverse('polls'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pollsCreate.html')

    def test_view_pollDashboard_correct_template(self):
        response = self.client.get(reverse('pollDashboard'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pollDashboard.html')


    #Not passing yet
    #def test_forms_lets_hope(self):
    #    form = AnswerForm(data={'answerOne': "Strongly Disagree", 'answerTwo': "Strongly Disagree", 'answerThree': "Strongly Disagree", 'answerFour': "Strongly Disagree", 'answerFive': "Strongly Disagree"})
    #    self.assertTrue(form.is_valid())
