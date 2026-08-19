from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
	path("notices/latest/", views.latest_notices, name="api-latest-notices"),
	path("notices/", views.notice_list, name="api-notice-list"),
	path("admission/submit/", views.submit_admission, name="api-submit-admission"),
	path("contact/submit/", views.submit_contact, name="api-submit-contact"),
]