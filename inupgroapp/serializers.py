from rest_framework import serializers
from .models import host_UserData,UserProfile,Student,Teacher,SchoolPage,findjob
from .models import SchoolDetails, CollegeDetails, InstitutionDetails,ourpartners,Career

# class UserProfileAndTeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['firstname']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '_all_'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class SchoolDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolDetails
        fields = ['school_name', 'subject', 'experience']
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class OurPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourpartners
        fields='__all__'
class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDetails
        fields = '__all__'

class InstitutionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionDetails
        fields = '__all__'
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname']

# class TeacherPortfolioItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TeacherPortfolioItem
#         fields = ['user_profile', 'image', 'achievements_and_certificates', 'description', 'abouts']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SchoolPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolPage
        fields = '__all__'
class FindjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = findjob
        fields='__all__'