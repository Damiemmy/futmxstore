# from django.db import models



# class StudentProfile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')
#     matric_number=models.CharField(max_length=50)
#     department=models.CharField(max_length=100)
#     faculty=models.CharField(max_length=100)
#     level=models.IntegerField(max_length=3)
#     UGT=models.CharField(max_length=10)

#     def __str__(self):
#         return self.user.username
