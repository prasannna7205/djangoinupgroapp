from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from inupgroapp.models import host_UserData,UserProfile,Student,SchoolPage
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import serializers
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PropertySerializer
import jwt
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
import json
import re
from rest_framework import viewsets
from django.contrib.auth import get_user
from django.forms.models import model_to_dict
User = get_user_model()
@method_decorator(csrf_exempt, name='dispatch')
class HostSignupView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        first_name=jsonData.get('first_name')
        last_name=jsonData.get('last_name')
        email = jsonData.get('email')
        phone = jsonData.get('phone')
        password = jsonData.get('password')
        
         # Email verification
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({'success': False, 'message': 'Invalid email format.'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'email is already taken.'})
        # Phone verification
        # if not re.match(r"^[0-9]{10}$", phone):
        #     return JsonResponse({'success': False, 'message': 'Invalid phone number format.'})  
        # user_data = host_UserData(first_name=first_name,last_name=last_name, email=email, phone=phone, password=make_password(password))
        # user_data.save() 

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name 
        user.save()

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'password':make_password(password),
        }
        login(request, user)
        payload = {'user_id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return JsonResponse({'success': True, 'message': 'User created successfully.', 'data': data, 'token': str(token)})

@method_decorator(csrf_exempt, name='dispatch')
class HostLogView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        email = jsonData.get('email')
        password = jsonData.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # user_data = host_UserData.objects.get(email=email)
            # data = {
            #     'user_id': user.id,    
            #     'first_name': user_data.first_name,
            #     'last_name': user_data.last_name,
            #     'email': user_data.email,
            #     'password': user_data.password,
            # }
            payload = {'user_id': user.id}
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
            return JsonResponse({'success': True,'token': str(token)})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'})

@method_decorator(csrf_exempt, name='dispatch')
class HostForgotPasswordView(View):
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'change.html', {'email': email})
        else:
            messages.error(request, 'This email address does not exist.')
            return redirect('forgot_password')
@method_decorator(csrf_exempt, name='dispatch')
class HostChangePasswordView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'})

        if not email:
            return JsonResponse({'error': 'Email is required.'})
        elif not password:
            return JsonResponse({'error': 'Password is required.'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No user with the given email exists.'})

        user.set_password(password)
        user.save()
        return JsonResponse({'success': 'Your password has been changed successfully.'})

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, Teacher, SchoolPage

class UserRegistrationView(View):
    template_name = 'school_info.html'
    model_mapping = {
        ('student', 'school'): Student,
        ('teacher', 'school'): Teacher,
        ('schoolpage', 'institute'): SchoolPage,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        education_type = request.POST.get('education_type')

        EducationModel = self.model_mapping.get((category, education_type))

        if EducationModel:
            try:
                instance = EducationModel(
                    firstname=firstname,
                    lastname=lastname,
                    username=username,
                    email=email,
                    phone=phone,
                    dob=dob,
                    category=category,
                    education_type=education_type,
                )

                if category == 'student':
                    instance.college_name = request.POST.get('class')
                    instance.school_name = request.POST.get('school')
                elif category == 'teacher':
                    instance.school_name = request.POST.get('school')
                    instance.subject = request.POST.get('subject')
                    instance.experience = request.POST.get('experience')
                elif category == 'schoolpage':
                    instance.founder_name = request.POST.get('founderYear')
                    instance.school_name = request.POST.get('schoolName')

                instance.save()

                return HttpResponse('Data saved successfully')
            except Exception as e:
                return HttpResponse(f'Error: {e}')

        return render(request, self.template_name)




class  schoolEducationCountView(View):
    def get(self, request, *args, **kwargs):
        school_count = UserProfile.objects.filter(education_type='school').count()
        response_data = {
            'school_education_count': school_count
        }
        return JsonResponse(response_data)
class collegeEducationCountView(View):
    def get(self, request, *args, **kwargs):
        college_count = UserProfile.objects.filter(education_type='college').count()
        response_data_count = UserProfile.objects.filter(education_type='institute').count()
        teacher_count = UserProfile.objects.filter(category='teacher').count()
        response_data = {
            'school_education_count': college_count,
            'institute_count':response_data_count,
            'teacher_count':teacher_count
        }
        return JsonResponse(response_data)

from rest_framework import generics
from .models import SchoolDetails, CollegeDetails, InstitutionDetails,ourpartners,Teacher,UserProfile
from .serializers import SchoolDetailsSerializer, CollegeDetailsSerializer, InstitutionDetailsSerializer,OurPartnersSerializer,TeacherSerializer

class SchoolDetailsList(generics.ListAPIView):
    queryset = SchoolDetails.objects.all()
    serializer_class = SchoolDetailsSerializer

class CollegeDetailsList(generics.ListAPIView):
    queryset = CollegeDetails.objects.all()
    serializer_class = CollegeDetailsSerializer

class InstitutionDetailsList(generics.ListAPIView):
    queryset = InstitutionDetails.objects.all()
    serializer_class = InstitutionDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Institution details retrieved successfully',
            'data': serializer.data
        }
        return Response(data, status=200)

 
  
# class UserProfileAndTeacherList(APIView):
#     def get(self, request, *args, **kwargs):
#         teachers = Teacher.objects.all()
#         teacher_serializer = TeacherSerializer(teachers, many=True)
#         combined_data = {
#             'teachers': teacher_serializer.data,
#         }
#         return Response(combined_data) 
      
class UserProfileAndTeacherList(APIView):
        def get(self, request, *args, **kwargs):
            teachers = Teacher.objects.all()
            teacher_data_list = []
            for teacher in teachers:
                try:
                    user_profile = UserProfile.objects.get(teacher=teacher)
                    teacher_data = {
                        'first_name': user_profile.firstname,
                        'last_name': user_profile.lastname,
                        'school_name': teacher.school_name,
                        'subject': teacher.subject,
                        'experience': teacher.experience,
                    }
                    teacher_data_list.append(teacher_data)
                except UserProfile.DoesNotExist:
                 pass
            return Response({'teachers': teacher_data_list})
        # UserProfileAndTeacherList
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
# from .serializers import  TeacherPortfolioItemSerializer,UserProfileSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# class UserProfileAndTeacherList(generics.ListAPIView):
#     queryset = TeacherPortfolioItem.objects.all()
#     serializer_class = TeacherPortfolioItemSerializer
# from inupgroapp.models import TeacherPortfolioItem


# UserProfileAndTeacherList
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import UserProfile, TeacherPortfolioItem
# from .serializers import  TeacherPortfolioItemSerializer,UserProfileSerializer

# class UserProfileAndTeacherList(generics.ListAPIView):
#     def get(self, request, *args, **kwargs):
#             user_profiles = UserProfile.objects.all()
#             teacher_portfolio_items = TeacherPortfolioItem.objects.all()
            
#             user_profile_data = UserProfileSerializer(user_profiles, many=True).data
#             teacher_portfolio_data = TeacherPortfolioItemSerializer(teacher_portfolio_items, many=True).data
#             alldata=[]
#             for i in user_profile_data:
#                 alldata.append(i)
#             for j in teacher_portfolio_data:
#                 alldata.append(j)
#             response_data = {
#                 "alldata":alldata
#             }
#             return Response(response_data)

# class UserProfileAndTeacherList(APIView):
#     def get(self, request, *args, **kwargs):
#         combined_data = []

#         teacher_portfolio_items = TeacherPortfolioItem.objects.select_related('user_profile')
        
#         for portfolio_item in teacher_portfolio_items:
#             data = {
#                 'first_name': portfolio_item.user_profile.firstname,
#                 'last_name': portfolio_item.user_profile.lastname,
#                 'image': portfolio_item.image.url,
#                 'achievements_and_certificates': portfolio_item.achievements_and_certificates,
#                 'description': portfolio_item.description,
#                 'abouts': portfolio_item.abouts,
#             }
#             combined_data.append(data)
        
#         serializer = UserProfileAndTeacherList(combined_data, many=True)
#         return Response(serializer.data)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Student, Teacher, SchoolPage,findjob
from .serializers import UserProfileSerializer, StudentSerializer, TeacherSerializer,SchoolDetailsSerializer,FindjobSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserProfileSerializer  # Import your serializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserProfileSerializer,FindjobSerializer

class RegisterUserView(APIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = serializer.validated_data['category']
            education_type = serializer.validated_data['education_type']
            
            if education_type == 'school':
                if category == 'student':
                    category_code = '1.1'
                    education_type_code = '1'
                elif category == 'teacher':
                    category_code = '1.2'
                    education_type_code = '1'
                elif category == 'schoolpage':
                    category_code = '1.3'
                    education_type_code = '1'
            elif education_type == 'college':
                if category == 'student':
                    category_code = '2.1'
                    education_type_code = '2'
                elif category == 'teacher':
                    category_code = '2.2'
                    education_type_code = '2'
                elif category == 'schoolpage':
                    category_code = '2.3'
                    education_type_code = '2'
            elif education_type == 'institute':
                if category == 'student':
                    category_code = '3.1'
                    education_type_code = '3'
                elif category == 'teacher':
                    category_code = '3.2'
                    education_type_code = '3'
                elif category == 'schoolpage':
                    category_code = '3'
                    education_type_code = '3.3'
            
            serializer.save(category=category_code, education_type=education_type_code)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Career(generics.ListAPIView):
    queryset=findjob.objects.all()
    serializer_class = FindjobSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Career Strategiest retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)
    
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import findjob
from .serializers import FindjobSerializer

class FindJobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FindjobSerializer
    def get_queryset(self):
        type_filter = self.request.query_params.get('type', None)
        if type_filter:
            return findjob.objects.filter(type=type_filter)
        return findjob.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
class ClubTypeFilterView(View):
    def get(self, request, *args, **kwargs):
        club_type_filter = request.GET.get('club_type_filter', None)

        if club_type_filter:
            queryset = findjob.objects.filter(club_type=club_type_filter)
        else:
            queryset = findjob.objects.all()

        serializer = FindjobSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=405)
class ExperienceLevelFilterView(View):
    def get(self, request, *args, **kwargs):
        experience_range = request.GET.get('experience_range', None)
        queryset = findjob.objects.all()

        if experience_range:
            min_experience, max_experience = map(int, experience_range.split('-'))
            queryset = queryset.filter(experiencelavel__gte=min_experience, experiencelavel__lt=max_experience)

        serializer = FindjobSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=405) 
