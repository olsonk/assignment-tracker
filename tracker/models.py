from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

today = datetime.date.today()
tomorrow = timezone.now() + datetime.timedelta(days=1)

# Create your models here.
class StudentManager(models.Manager):
	def create_student(self, first_name, last_name, classYear, studentID):
		new_student = self.create(	first_name=first_name, last_name=last_name,
									classYear=classYear, studentID=studentID)
		return new_student

class Student(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	def full_name(self): 
		return str(self.first_name) + " " + str(self.last_name)
	classYear = models.CharField(max_length=50)
	studentID = models.PositiveIntegerField()	
	objects = StudentManager()
	
	def __unicode__(self):
		return str(self.first_name) + " " + str(self.last_name)
	
	def numbermissing(self):
		return self.missingwork_set.count()
	numbermissing.short_description = "# of Missing Assignments"
	
	def is_in_current_class(self):
		return self.classYear == "13-14"
	is_in_current_class.boolean = True
	is_in_current_class.short_description = "Current Class?"
	
class AssignmentManager(models.Manager):
	def create_assignment(self, subject, description, due_date):
		new_assignment = self.create(subject=subject, description=description,
									due_date=due_date)
		return new_assignment									

class Assignment(models.Model):
	subject = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	due_date = models.DateField('due date', default=datetime.date.today())
	assigned = datetime.date.today()
	objects = AssignmentManager()
	
	def __unicode__(self):
		return self.description

class MissingWorkManager(models.Manager):
	def create_missingwork(self, student, assignment):
		new_missingwork = self.create(student=student, assignment=assignment)
		return new_missingwork
		
class MissingWork(models.Model):
	student = models.ForeignKey(Student)
	assignment = models.ForeignKey(Assignment)
	day = datetime.date.today()
	objects = MissingWorkManager()
	
	def __unicode__(self):
		return str(self.student) + " / " + str(self.assignment)