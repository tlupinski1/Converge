"""converge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from main import views as main_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('polls/', user_views.polls_create,name='polls'),
    path('register/', user_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('admin/', admin.site.urls),
    path('profiles/', user_views.profiles, name='profiles'),
    path('allUsers/',user_views.allUsers,name='allusers'),
    path('pollDashboard/',user_views.pollsDashboard,name='pollDashboard'),
    path('createProject/',user_views.projectCreation,name="projectCreation"),
    path('publicDashboard/',user_views.dashboard,name="dash"),
    path('',main_views.home,name="main-home"),
    path('myProjects/', user_views.myProjects, name='myProjects'),
    path('projectPage/',user_views.projectPage,name="projPage"),
    path('takePoll/',user_views.takePoll,name="takepoll"),
    path('pollPage/',user_views.pollPage,name="pollpage"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
