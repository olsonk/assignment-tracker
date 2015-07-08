from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.core.context_processors import csrf
import datetime

from tracker.models import Student, Assignment, MissingWork
from tracker.forms import MissingWorkForm

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'tracker/index.html'
	context_object_name = 'all_students'
	
	def get_queryset(self):
		return Student.objects.all()
		
class DashboardView(generic.ListView):
	model = Assignment
	template_name = 'tracker/dashboard.html'
	context_object_name = 'todays_assignments'
	
	def get_queryset(self):
		todays_assignments = []
		for assignment in Assignment.objects.all():
			if assignment.due_date == datetime.date.today():
				todays_assignments.append(assignment)
		return todays_assignments
		
class StudentView(generic.DetailView):
	model = Student
	template_name = "tracker/student.html"

class DailyView(generic.ListView):
	model = Assignment
	template_name = "tracker/assign.html"
	
class AddStudent(generic.ListView):
	model = Student
	template_name = "tracker/add_student.html"
	
def add_missingwork(request):
	form = MissingWorkForm(request.POST)
	if form.is_valid():
		model_instance = form.save(commit=False)
		model_instance.timestamp = timezone.now()
		model_instance.save()
		return redirect('tracker:index')
	else:
		form = MissingWorkForm()
	return render(request, 'tracker/add_missing_work.html', {'form': form})
	
def add(request):
	if 'subject' in request.POST:
		new = Assignment.objects.create_assignment(	request.POST['subject'], 
													request.POST['description'],
													request.POST['due_date'],
													)
	elif 'first_name' in request.POST:
		new = Student.objects.create_student(	request.POST['first_name'],
												request.POST['last_name'],
												request.POST['classYear'], 
												request.POST['studentID'],
											)
	elif 'student' in request.POST:
		new = MissingWork.objects.create_missingwork(	request.POST['student'],
														request.POST['assignment'],
													)
	new.save()
	return HttpResponseRedirect(reverse('tracker:index'))