from django.forms import ModelForm
from tracker.models import MissingWork

class MissingWorkForm(ModelForm):
	class Meta:
		model = MissingWork
		fields = ['student', 'assignment']