from django.conf.urls import patterns, include, url

urlpatterns = patterns('calendarapp.views',
	(r"^month/(\d{4})/(\d+)/$", "month"),
	(r"^settings/$", "settings"),
	(r"^(\d+)/$", "main"),
	(r"", "main"),
)
