from django.db import models
# Create your models here.
class host_UserData(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,unique=True,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    token=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.first_name


# User details
class UserProfile(models.Model):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('schoolpage', 'School Page'),
    ]
    
    EDUCATION_CHOICES = [
        ('school', 'School'),
        ('college', 'College'),
        ('institute', 'Institute'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    education_type = models.CharField(max_length=20, choices=EDUCATION_CHOICES, blank=True, null=True)

    def _str_(self):
        return self.username

class Student(UserProfile):
    college_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

class Teacher(UserProfile):
    school_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

class SchoolPage(UserProfile):
    founder_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
class ourpartners(models.Model):
    PartnersNmae = models.CharField( max_length=100)
class SchoolDetails(models.Model):
    Schoolname = models.CharField( max_length=30)
    SchoolHeading = models.TextField()
    SchoolDescription = models.TextField()
class CollegeDetails(models.Model):
    Collegename = models.CharField( max_length=30)
    CollegeHeading = models.TextField()
    CollegeDescription = models.TextField()
class InstitutionDetails(models.Model):
    Institutionname = models.CharField( max_length=30)
    InstitutionHeading = models.TextField()
    InstitutionDescription = models.TextField()
class Career(models.Model):
    postname= models.CharField(max_length=50)
    fieldname=models.CharField(max_length=50)
    officelocation = models.CharField(max_length=50)
    minimumqualification =models.CharField(max_length=50)
    experiencelavel = models.CharField(max_length=50)
    vacancylocation = models.CharField(max_length=30)
    jobdescription = models.TextField(max_length=100)
    technicalrequirement = models.TextField(max_length=200)

class findjob(models.Model):
    postname= models.CharField(max_length=50)
    fieldname=models.CharField(max_length=50)
    officelocation = models.CharField(max_length=50)
    minimumqualification =models.CharField(max_length=50)
    experiencelavel = models.CharField(max_length=50)
    vacancylocation = models.CharField(max_length=30)
    jobdescription = models.TextField(max_length=100)
    technicalrequirement = models.TextField(max_length=200)
    type_choices = (
        ('school', 'School'),
        ('college', 'College'),
        ('institute', 'Institute'),
    )
    type = models.CharField(max_length=20, choices=type_choices, default='school')
    club_type_choices = (
        ('jobs', 'Jobs'),
        ('clubs', 'Clubs'),
    )
    club_type = models.CharField(max_length=20, choices=club_type_choices, default='jobs')
