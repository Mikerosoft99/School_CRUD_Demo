"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from day2.views import about, delete_student, home, signin, signout, signup, students, create_student, update_student
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('students/',students, name='students'),
    path('',signin, name='signin'),
    path('signup/',signup, name='signup'),
    path('signout/',signout, name='signout'),
    path('create_student/',create_student, name='create_student'),
    path("delete_student/<int:id>",delete_student,name='delete_student'),
    path('update_student/<int:id>/',update_student, name='update_student'),
    path('about/',about, name='about'),
]