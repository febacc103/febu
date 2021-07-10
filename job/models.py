# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.models import AbstractUser
#
#
# class MyUser(AbstractUser):
#     phone_number = models.IntegerField(max_length=12)
#
#     options = (
#         ("Employer", "Employer"),
#         ("Job seeker", "Job seeker"),
#
#     )
#     role = models.CharField(max_length=12, choices=options, default="Employer")
#
#
# class UserProfileModel(models.Model):
#     user = models.OneToOneField(MyUser,
#                                 on_delete=models.CASCADE, primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     options = (
#         ("male", "male"),
#         ("female", "female"),
#         ("other", "other")
#     )
#     gender = models.CharField(max_length=12, choices=options, default="male")
#     email = models.CharField(max_length=100)
#     education_qualification=models.CharField(max_length=120)
#     skills=models.CharField(max_length=250)
#     experience=models.CharField(max_length=250)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#
#
# class EmployerProfileModel(models.Model):
#     Employer = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
#     company_name=models.CharField(max_length=100)
#     company_location=models.CharField(max_length=100)
#
#
# class JobRegisterModel(models.Model):
#     job_title=models.CharField(max_length=100)
#     employer=models.ForeignKey(EmployerProfileModel,on_delete=models.CASCADE)
#     job_detail=models.CharField(max_length=300)
#     options = (
#         ("Active", "Active"),
#         ("Closed", "Closed"),
#
#     )
#     status= models.CharField(max_length=20, choices=options, default="Active")
#     created_date=models.DateTimeField(auto_now=True)
#     last_date=models.DateTimeField()
#
#
#
#
# class ApplicationFormModel(models.Model):
#     resume = models.FileField(upload_to="")
#     job=models.ForeignKey(JobRegisterModel,on_delete=models.CASCADE)
#
#
#
