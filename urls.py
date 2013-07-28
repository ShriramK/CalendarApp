from django.conf.urls import patterns, include, url

urlpatterns = patterns('calendarapp.views',
	(r"^day/(\d{4})/(\d+)/(\d+)/$", "day"),
	(r"^month/(\d{4})/(\d+)/$", "month"),
	(r"^month/(\d{4})/(\d+)/(prev|next)/$", "month"),
	(r"^month$", "month"),
	(r"^settings/$", "settings"),
	(r"^(\d+)/$", "main"),
	(r"", "main"),
)
