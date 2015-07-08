from django.contrib import admin
from tracker.models import Student, Assignment, MissingWork

class MissingWorkInline(admin.StackedInline):
	model = MissingWork
	extra = 2
	
class StudentAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['first_name']}),
		(None, 					{'fields': ['last_name']}),
		("Student ID",			{'fields': ['studentID']}),
		("Class Year (ex. 13-14)",{'fields': ['classYear']}),
	]
	inlines = [MissingWorkInline]
	list_display = ('full_name', 'is_in_current_class', 'numbermissing')
	list_filter = ['classYear']
	search_fields = ['full_name']
	
class AssignmentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Subject',				{'fields': ['subject']}),
		('Description',			{'fields': ['description']}),
		('Due', 				{'fields': ['due_date']})
	]
	inlines = [MissingWorkInline]
	list_display = ('description', 'subject', 'due_date')
	list_filter = ['due_date']
	search_fields = ['description']

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(MissingWork)