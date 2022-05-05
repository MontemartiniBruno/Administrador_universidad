from django.db import models

# Create your models here.

class Degree(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return (self.name)

class Student(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    genders = [
        ('F','Female'),
        ('M', 'Male'),
    ]
    gender = models.CharField(max_length=1, choices=genders, default='M')
    degree = models.ForeignKey(Degree, null=False, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def full_name(self):
        txt = "{0} {1}"
        return txt.format(self.last_name, self.first_name)
    
    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tuition(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)