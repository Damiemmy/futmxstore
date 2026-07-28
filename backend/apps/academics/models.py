# from django.db import models

# # Create your models here.
# class Faculty(models.Model):
#     name=models.CharField(max_length=100)
#     slug=models.SlugField(max_length=100)
#     description=models.TextField()

# class Department(models.Model):
#     name=models.CharField(max_length=100)
#     slug=models.SlugField(max_length=100)

#     def __str__(self):
#         return self.name

# class Level(models.Model):
#     level=models.IntegerField(max_length=300)

#     def __str__(self):
#         return self.name

# class Semester(models.Model):
#     semester=models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# #should on_delete=models.CASCADE ON ALL FIELD OR SET_NULL
# class Course(models.Model):
#     department=models.ForeignKey(Department,on_delete=models.CASCADE)
#     code=models.CharField(max_length=20)
#     title=models.CharField(max_length=100)
#     description=models.TextField(max_length=1200)
#     level=models.ForeignKey(Level,on_delete=models.CASCADE,related_name='past_questions')
#     semester=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='past_questions')
#     lecture=models.CharField(max_length=100)
    
# #should on_delete=models.CASCADE ON ALL FIELD OR SET_NULL
# class Material(models.Model):
#     MATERIAL_TYPE=(
#         ("lecture_note","Lecture Note"),
#         ("handout","Handout" ),
#         ("lab_manual","Lab Manual"),
#         ("slides","Slides"),
#         ("tutorial","Tutorial"),

#     )

#     course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     title=models.CharField(max_length=100)
#     description=models.TextField(max_length=1200)
#     material_type=models.CharField(max_length=20,choices=MATERIAL_TYPE, default="Lecture_note")


# #should on_delete=models.CASCADE ON ALL FIELD OR SET_NULL
# class PastQuestion(models.Model):
#     course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='past_questions')
#     year=models.CharField(max_length=4)
#     semester=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='past_questions')
#     pdf=models.FileField(upload_to='/pastquestions')
#     uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='past_questions')
#     create_at=models.DatetimeField(auto_add_now=True)



