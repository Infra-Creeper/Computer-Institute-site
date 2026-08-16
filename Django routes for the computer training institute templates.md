# Django routes for the computer training institute templates

The templates require **11 public page routes** and **9 HTMX/API routes**. The route definitions are provided in `training-institute-urls.py`. Replace `training` with your actual Django app name and replace the view names with your own view functions or class-based views.

## Public page routes

| Method | URL | Suggested name | Template | Purpose |
|---|---|---|---|---|
| GET | `/` | `home` | `home.html` | Homepage with hero, featured courses, notices, and latest blog posts. |
| GET | `/courses/` | `course-list` | `courses/list.html` | Full course catalog and initial course results. |
| GET | `/courses/<slug:slug>/` | `course-detail` | `courses/detail.html` | Individual course, syllabus, fee, and apply link. |
| GET | `/notices/` | `notice-board` | `notices/board.html` | Notice board and initial notice page. |
| GET | `/notices/<slug:slug>/` | `notice-detail` | `notices/detail.html` | Notice detail; return the partial for HTMX requests. |
| GET | `/blog/` | `blog-list` | `blog/list.html` | Blog index, category filters, and pagination. |
| GET | `/blog/<slug:slug>/` | `blog-detail` | `blog/detail.html` | Individual blog post and related posts. |
| GET | `/admission/` | `admission-form` | `admission/form.html` | Admission form; supports `?course=<course-slug>`. |
| GET | `/admission/success/` | `admission-success` | `admission/success.html` | Optional full-page application confirmation. |
| GET | `/about/` | `about` | `about.html` | About page. |
| GET | `/contact/` | `contact` | `contact.html` | Contact page and contact form. |

## HTMX/API routes

| Method | URL | Suggested name | Expected response |
|---|---|---|---|
| GET | `/api/courses/featured/` | `api-featured-courses` | Repeated `partials/_course_card.html` fragments. |
| GET | `/api/courses/` | `api-course-search` | Course cards for `#course-grid`; read `search` and `category`. |
| GET | `/api/notices/latest/` | `api-latest-notices` | Latest three `partials/_notice_item.html` fragments. |
| GET | `/api/notices/` | `api-notice-list` | Notice fragments for `#notice-list`; read `page`. |
| GET | `/api/blog/latest/` | `api-latest-blog-posts` | Latest three blog card fragments. |
| GET | `/api/blog/related/<slug:slug>/` | `api-related-blog-posts` | Related blog card fragments. |
| GET | `/api/blog/` | `api-blog-search` | Filtered blog cards; read `category` and `page`. |
| POST | `/api/admission/submit/` | `api-submit-admission` | Validate/process multipart admission form; return success or validation fragment. |
| POST | `/api/contact/submit/` | `api-submit-contact` | Validate/process contact form; return a fragment with `id="contact-response"`. |

## Suggested `urls.py`

```python
from django.urls import path
from . import views

app_name = "training"

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.course_list, name="course-list"),
    path("courses/<slug:slug>/", views.course_detail, name="course-detail"),
    path("notices/", views.notice_board, name="notice-board"),
    path("notices/<slug:slug>/", views.notice_detail, name="notice-detail"),
    path("blog/", views.blog_list, name="blog-list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog-detail"),
    path("admission/", views.admission_form, name="admission-form"),
    path("admission/success/", views.admission_success, name="admission-success"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("api/courses/featured/", views.featured_courses, name="api-featured-courses"),
    path("api/courses/", views.course_search, name="api-course-search"),
    path("api/notices/latest/", views.latest_notices, name="api-latest-notices"),
    path("api/notices/", views.notice_list, name="api-notice-list"),
    path("api/blog/latest/", views.latest_blog_posts, name="api-latest-blog-posts"),
    path("api/blog/related/<slug:slug>/", views.related_blog_posts, name="api-related-blog-posts"),
    path("api/blog/", views.blog_search, name="api-blog-search"),
    path("api/admission/submit/", views.submit_admission, name="api-submit-admission"),
    path("api/contact/submit/", views.submit_contact, name="api-submit-contact"),
]
```

Include the app URLs in the project-level `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path("", include("training.urls", namespace="training")),
]
```

For `/notices/<slug:slug>/`, return only `notices/detail.html` when the request contains `HX-Request: true`, because the template is loaded into `#modal`. For ordinary browser requests, return a full-page wrapper or redirect to the notice board.

For `/api/admission/submit/`, the template currently targets `#form-response` with `hx-swap="outerHTML"`; return a replacement element with that same ID for success or validation errors. The form includes `{% csrf_token %}` and uploads files, so the view should accept `POST` and `request.FILES`.

Static files, media files, `sitemap.xml`, and `robots.txt` are outside the requested frontend template scope and should be configured at the project level.
