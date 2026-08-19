from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.courses, name="course-details"),
    path("courses/list", views.course_list, name="course-list"),
    path("notices/", views.notice_board, name="notice-board"),
    path("notices/<slug:slug>/", views.notice_detail, name="notice-detail"),
    path("blog/", views.blog_list, name="blog-list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog-detail"),
    path("admission/", views.admission_form, name="admission-form"),
    path("admission/success/", views.admission_success, name="admission-success"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
