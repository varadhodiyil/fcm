
from django.conf.urls import url
from notifications.core import views

urlpatterns = [
    url(r'^register/', views.Register.as_view()),
	url(r'^log/', views.EventLog.as_view()),
	url(r'^notify/', views.Notify.as_view()),
	# url(r'^update_notify/', views.UpdateNotified.as_view()),
]
