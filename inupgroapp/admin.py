from django.contrib import admin
from inupgroapp.models import findjob, UserProfile,Student,Teacher,SchoolPage,SchoolDetails,CollegeDetails,InstitutionDetails,ourpartners,Career
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(SchoolPage)
admin.site.register(ourpartners)
admin.site.register(SchoolDetails)
admin.site.register(CollegeDetails)
admin.site.register(InstitutionDetails)
admin.site.register(findjob)
# admin.site.register(TeacherPortfolioItem)

