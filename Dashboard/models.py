from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]
    COURSE_CHOICES = [
        ('Computer Science','Computer Science'),
        ('Information Technology','Information Technology'),
        ('Software Engineering','Software Engineering'),
        ('Web Development','Web Development'),
        ('Data Science','Data Science'),
    ]
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30, choices=COURSE_CHOICES)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name