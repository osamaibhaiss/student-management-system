from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    schedule = models.ForeignKey('CourseSchedule', on_delete=models.CASCADE)
    prerequisites = models.ManyToManyField('self', related_name='prerequisite_courses', blank=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=10)
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_courses = models.ManyToManyField(Course, related_name='students')
    
    def has_completed_prerequisites(self, course):
        if not course.prerequisites.exists():
            return True
        for prereq in course.prerequisites.all():
            if self.registered_courses.filter(code=prereq.code).exists():
                continue
            return False
        return True



class StudentsRegs(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    
