import csv
from pathlib import Path

from django.utils.timezone import localdate
from django.shortcuts import get_object_or_404, render

from .models import Notice


about_text = '''
Compuetech is an affordable computer training institute in Dhanubhanga, Goalpara, Assam, India, offering practical computer training courses designed to build job-ready skills. We provide computer courses in Software, Hardware, and Networking courses and other professional computer training programs.

Since 2015, we have helped students and learners develop practical computer skills through high-quality, affordable computer education. Whether you are looking for a computer training institute near you, an ADCA course near you, or computer technician training, Compuetech provides hands-on learning designed to prepare you for real-world opportunities.

With more than 10 years of experience in computer education, our goal is to make quality and affordable computer training accessible to everyone while empowering the digital future of our community.

'''

institute_ctxt = {
        "site_name": "Compuetech",
        "site_tagline": "Empowering digital future.",
        "institute": {
            "email": "compuetech@tuta.io",
            "phone": "+91 700-261-6276",
            "address": "Dhanubhanga, Goalpara, Assam, India",
            "postal_address": "P.O. Dhanubhanga, Dist:Goalpara, PIN: 783130, India",
        },
        "institute_contact": {
            "email": "info@abccomputerinstitute.com",
            "phone": "+91 700-261-6276",
            "whatsapp": "+91 700-261-6276",
        },
        "social_links": {
        },
        "seo": {
            "default_description": "ABC Computer Training Institute provides practical computer training and career-focused digital skills courses.",
            "default_keywords": "computer training, computer courses, IT training, digital skills, career courses",
            
        },
        "about_content":about_text
    }


def home(request):
    return render(request, "home.html", context=institute_ctxt)


def course_list(request):
    course_file = Path(__file__).resolve().parent / "Computer_Institute_Course_Fee_Master.csv"
    with course_file.open(newline="", encoding="cp1252") as csv_file:
        courses = [
            {
                "course_code": row["Course Code"],
                "course_name": row["Course Name"],
                "duration": row["Duration"],
                "eligibility": row["Eligibility"],
                "admission_fees": row["Admission Fees"],
                "monthly_fees": row["Monthly Fees"],
                "exam_fees": row["Exam Fees"],
                "total_fees": row["Total Fees"],
            }
            for row in csv.DictReader(csv_file)
        ]

    context = {**institute_ctxt, "courses": courses}
    return render(request, "courses/list.html", context=context)


def course_detail(request, slug):
    return render(request, "courses/detail.html", {"slug": slug})


def notice_board(request):
    notices = Notice.objects.all()[:10]
    notice_context = [
        {
            "title": notice.title,
            "date": notice.published_at,
            "content": notice.message,
            "excerpt": notice.message,
            "slug": notice.slug,
            "is_recent": notice.published_at.date() == localdate(),
        }
        for notice in notices
    ]
    context = {
        **institute_ctxt,
        "notices": notice_context,
        "next_page": 2,
    }
    return render(request, "notices/board.html", context=context)


def notice_detail(request, slug):
    notice = get_object_or_404(Notice, slug=slug)
    return render(request, "notices/detail.html", {"notice": {
        "title": notice.title,
        "date": notice.published_at,
        "content": notice.message,
    }})


def blog_list(request):
    return render(request, "blog/list.html", context=institute_ctxt)


def blog_detail(request, slug):
    return render(request, "blog/detail.html", {"slug": slug})


def admission_form(request):
    return render(request, "admission/form.html", context=institute_ctxt)


def admission_success(request):
    application = request.session.pop("admission_success", {})
    return render(request, "admission/success.html", {"application": application})


def about(request):
    return render(request, "about.html", context=institute_ctxt)


def contact(request):
    return render(request, "contact.html", context=institute_ctxt)