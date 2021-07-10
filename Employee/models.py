from django.db import models


# Create your models here.


class EmployeeRegModel(models.Model):
    company_name = models.CharField(max_length=120, unique=True)
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=500)
    experience = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    job_post_on = models.DateField(auto_now=True)
    close = models.DateField()

    def __str__(self):
        return self.company_name



class JobseekerApplicationFormModel(models.Model):
   first_name = models.CharField(max_length=120)
   last_name= models.CharField(max_length=120)
   phone_number = models.IntegerField(max_length=12)
   email= models.EmailField(max_length=100)
   location = models.CharField(max_length=100)
   options = (("select a job category", "select a job category"),
              ("Accounting", "Accounting"),
              ("Business support", "Bsiness support"),
              ("Communications", "Communications"),
              ("Corporate Developement", "Corporate Developement"),
              ("Cybersecurity", "Cybersecurity"),
              ("Digital", "Digital"),
              ("Engineering", "Engineering"),
              ("Finance", "Finance"),
              ("Information Technology", "Information Technology"),
              ("Internship", "Internship"),
              ("Legal", "Legal"),
              ("Manufacturing", "Manufacturing"),
              ("Others", "Others")
              )
   category= models.CharField(max_length=120, choices=options, default="select a job category")
   options=(("Select one","Select one"),
            ("Professional","Professional"),
            ("Entry Level","Entry Level"),
            ("Management","Management"),
            ("Student","Student")
            )
   career_level= models.CharField(max_length=120, choices=options, default="select a job category")
   Field_of_study= models.CharField(max_length=120)
   overall_result=models.FloatField(max_length=5)
   resume=models.FileField()
   job_post_on = models.DateField(auto_now=True)
   def __str__(self):
        return self.first_name
