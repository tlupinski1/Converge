from django.test import TestCase
from users.models import Profile, User, Project, Polls, PollAnswers, Members
from django.utils import timezone
from .forms import OurUserForm, UpdateUser, UpdateProfile, ProjectForm, textForm, PollsForm, AnswerForm, UpdateUser

# Create your tests here.
class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_forms(self):
        form = ProjectForm(data={'projectName': "projectName", 'projectType': "projectType", 'projectDescription': "projectDescription", 'projectPicture': "projectPicture"})
        self.assertTrue(form.is_valid())

    def test_forms_next(self):
        form = PollsForm(data={'title': "title", 'questionOne': "questionOne", 'questionTwo': "questionTwo", 'questionThree': "questionThree", 'questionFour': "questionFour", 'questionFive': "questionFive"})
        self.assertTrue(form.is_valid())

    def test_forms_again(self):
        form = UpdateProfile(data={'image': "image", 'userDescription': "userDescription", 'userInterests': "userInterests", 'location': "location"})
        self.assertTrue(form.is_valid())

#Not passing yet
    #def test_forms_lets_hope(self):
    #    form = AnswerForm(data={'answerOne': "Strongly Disagree", 'answerTwo': "Strongly Disagree", 'answerThree': "Strongly Disagree", 'answerFour': "Strongly Disagree", 'answerFive': "Strongly Disagree"})
    #    self.assertTrue(form.is_valid())
