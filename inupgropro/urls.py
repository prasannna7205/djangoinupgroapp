"""inupgropro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from inupgroapp.views import ExperienceLevelFilterView, ClubTypeFilterView, Career,RegisterUserView,UserRegistrationView,HostSignupView, HostLogView, HostForgotPasswordView,HostChangePasswordView,schoolEducationCountView,collegeEducationCountView,SchoolDetailsList, CollegeDetailsList, InstitutionDetailsList,UserProfileAndTeacherList,UserProfileAndTeacherList
# from inupgroapp.views import register_user
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inupgroapp.views import FindJobViewSet
router = DefaultRouter()
router.register(r'jobs', FindJobViewSet,basename='job')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('host_signup/', HostSignupView.as_view(), name='host_signup'),
    path('host_login/', HostLogView.as_view(), name='host_login'),
    path('host_forgot_password/', HostForgotPasswordView.as_view(), name='host_forgot_password'),
    path('host_change_password/', HostChangePasswordView.as_view(), name='host_change_password'),
    path('User_Registration_View/', UserRegistrationView.as_view(), name='User_Registration_View'),
    # path('school-education-count/', schoolEducationCountView.as_view(), name='school-education-count'),
    path('college_education-count/', collegeEducationCountView.as_view(), name='college-education-count'),
    # path('institute-education-count/', instituteEducationCountView.as_view(), name='institute-education-count'),
    # path('teacher-education-count/', teacherEducationCountView.as_view(), name='teacher-education-count'),
    path('api-schools/', SchoolDetailsList.as_view(), name='school-list'),
    path('api-colleges/', CollegeDetailsList.as_view(), name='college-list'),
    path('api-institutions/', InstitutionDetailsList.as_view(), name='institution-list'),
    # path('api-OurPartnersList/',OurPartnersList.as_view(), name='api-OurPartnersList'),
    path('api/userprofiles_and_teachers/', UserProfileAndTeacherList.as_view(), name='userprofile-teacher-list'),
    path('api/UserProfileAndTeacherList/', UserProfileAndTeacherList.as_view(), name='UserProfileAndTeacherList'),
    # path('forgotpassword/', HostForgotPasswordView.as_view()),
    # path('changepassword/', HostChangePasswordView.as_view()),
    # path('register/', register_user, name='register_user'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('api/CareerStrategiest/',Career.as_view(), name='CareerStrategiest'),
    path('api/', include(router.urls)),
    path('api_filtered/', ClubTypeFilterView.as_view(), name='club-type-filter'),
    path('api_filtered_by_experience/', ExperienceLevelFilterView.as_view(), name='experience-level-filter')
    
]
