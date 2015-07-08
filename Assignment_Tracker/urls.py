from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Assignment_Tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^tracker/', include('tracker.urls', namespace="tracker")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'Assignment_Tracker.views.login', name='login'),
	url(r'^accounts/auth/$', 'Assignment_Tracker.views.auth_view', name='auth'),
	url(r'^accounts/logout/$', 'Assignment_Tracker.views.logout', name='logout'),
	url(r'^accounts/loggedin/$', 'Assignment_Tracker.views.loggedin', name='loggedin'),
	url(r'^accounts/invalid/$', 'Assignment_Tracker.views.invalid_login', name='invalid'),
	url(r'^accounts/register/$', 'Assignment_Tracker.views.register_user', name='register'),
	url(r'^accounts/register_success/$', 'Assignment_Tracker.views.register_success', name='register_sucess'),
)
