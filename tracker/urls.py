from django.conf.urls import patterns, url
from tracker import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.StudentView.as_view(), name='student'),
	url(r'^assign/$', views.DailyView.as_view(), name='daily_view'),
	url(r'^assign/add$', views.add, name='add'),
	url(r'^add_student/$', views.AddStudent.as_view(), name='add_student'),
	url(r'^add_missing_work/$', views.add_missingwork, name='add_missing_work'),
	url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
)