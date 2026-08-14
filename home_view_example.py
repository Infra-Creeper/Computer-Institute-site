"""
views.py — Django view that provides context data for the homepage.

This file demonstrates how to assemble all context variables required
by the homepage template (home.html). Adapt querysets and data sources
to match your actual Django models.
"""

from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    Homepage view assembling all context variables for home.html.

    Each key below maps to the context variables expected by the
    individual component files referenced in the template.
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ── Institute Info (used by navbar, footer, og tags) ──────────
        context["institute"] = {
            "name": "CodeCraft Academy",
            "logo_url": "/static/images/logo.png",
            "description": (
                "Industry-leading computer training institute offering "
                "hands-on courses in programming, web development, data science, "
                "and cloud computing."
            ),
            "og_image_url": "/static/images/og-home.jpg",
            "address": {
                "street": "123 Tech Park Avenue, Suite 200",
                "city": "San Francisco",
                "state": "CA",
                "zip": "94105",
                "country": "US",
            },
            "phone": "+1 (555) 987-6543",
            "email": "info@codecraftacademy.com",
            "social": {
                "facebook": "https://facebook.com/codecraftacademy",
                "twitter": "https://twitter.com/codecraftacademy",
                "linkedin": "https://linkedin.com/company/codecraftacademy",
                "youtube": "https://youtube.com/@codecraftacademy",
            },
        }

        # ── Navigation Links (used by navbar.html) ────────────────────
        context["nav_links"] = [
            {"label": "Courses", "url_name": "courses:list"},
            {"label": "Instructors", "url_name": "instructors:list"},
            {"label": "Pricing", "url_name": "pricing"},
            {"label": "About", "url_name": "about"},
            {"label": "Contact", "url_name": "contact"},
        ]

        # ── Auth State (used by navbar.html) ──────────────────────────
        context["is_authenticated"] = self.request.user.is_authenticated
        context["user"] = self.request.user

        # ── Hero Data (used by hero.html) ─────────────────────────────
        context["hero_data"] = {
            "headline": "Build Your Tech Career with Expert-Led Training",
            "subheadline": (
                "Master Python, Web Development, Data Science, and more "
                "with hands-on projects and industry-certified instructors."
            ),
            "cta_primary_label": "Start Learning Today",
            "cta_primary_url_name": "auth:register",
            "cta_secondary_label": "Browse Courses",
            "cta_secondary_url_name": "courses:list",
            "image_url": "/static/images/hero-bg.jpg",
            "image_alt": "Students collaborating in a modern coding lab",
        }

        # ── Statistics (used by hero-stats.html) ──────────────────────
        context["stats"] = [
            {"label": "Students Trained", "value": 5247, "suffix": "+"},
            {"label": "Courses Available", "value": 124, "suffix": "+"},
            {"label": "Success Rate", "value": 95, "suffix": "%"},
            {"label": "Expert Instructors", "value": 52, "suffix": "+"},
        ]

        # ── Featured Courses (used by course-grid.html) ───────────────
        # Replace with actual queryset: Course.objects.filter(featured=True)[:6]
        context["featured_courses"] = []  # Populate from your model
        context["has_more_courses"] = True
        context["next_page_url"] = "/courses/?page=2&featured=true"

        # ── Testimonials (used by testimonial-carousel.html) ──────────
        context["testimonials"] = []  # Populate: Testimonial.objects.filter(featured=True)[:6]

        # ── Featured Instructors (used by instructor-grid.html) ───────
        context["featured_instructors"] = []  # Populate: Instructor.objects.filter(featured=True)[:6]

        # ── Pricing Plans (used by pricing-card.html) ─────────────────
        context["pricing_plans"] = [
            {
                "name": "Starter",
                "price": 49,
                "currency": "USD",
                "period": "month",
                "is_recommended": False,
                "url_name": "auth:register",
                "cta_label": "Get Started",
                "features": [
                    "Access to 20+ beginner courses",
                    "Community forum support",
                    "Basic certificates",
                    "Email support",
                ],
            },
            {
                "name": "Professional",
                "price": 99,
                "currency": "USD",
                "period": "month",
                "is_recommended": True,
                "url_name": "auth:register",
                "cta_label": "Start Free Trial",
                "features": [
                    "Access to all 120+ courses",
                    "Live instructor sessions",
                    "Industry-recognized certificates",
                    "Priority support",
                    "Career guidance sessions",
                    "Project reviews by mentors",
                ],
            },
            {
                "name": "Enterprise",
                "price": 249,
                "currency": "USD",
                "period": "month",
                "is_recommended": False,
                "url_name": "auth:register",
                "cta_label": "Contact Sales",
                "features": [
                    "Everything in Professional",
                    "Dedicated account manager",
                    "Custom learning paths",
                    "Team analytics dashboard",
                    "Bulk enrollment discounts",
                    "On-site training options",
                    "SLA guarantee",
                ],
            },
        ]

        # ── FAQ Categories (used by faq-section.html) ─────────────────
        context["faq_categories"] = [
            {
                "name": "General",
                "faqs": [
                    {
                        "id": 1,
                        "question": "What courses do you offer?",
                        "answer": (
                            "We offer 120+ courses across Python, Web Development "
                            "(HTML, CSS, JavaScript, React, Django), Data Science, "
                            "Machine Learning, Cloud Computing (AWS, Azure), "
                            "Cybersecurity, and DevOps."
                        ),
                    },
                    {
                        "id": 2,
                        "question": "Do I need prior programming experience?",
                        "answer": (
                            "Not at all! Our beginner courses start from the fundamentals. "
                            "Each course clearly indicates its level (beginner, intermediate, "
                            "or advanced) so you can choose the right starting point."
                        ),
                    },
                    {
                        "id": 3,
                        "question": "How long does each course take?",
                        "answer": (
                            "Course durations range from 2 weeks (focused workshops) "
                            "to 12 weeks (comprehensive programs). Most courses are "
                            "6-8 weeks, with flexible scheduling to fit your availability."
                        ),
                    },
                ],
            },
            {
                "name": "Enrollment & Pricing",
                "faqs": [
                    {
                        "id": 4,
                        "question": "Can I try a course before committing?",
                        "answer": (
                            "Yes! We offer a 7-day free trial on our Professional plan, "
                            "and all courses include a free introductory lesson so you "
                            "can preview the content before enrolling."
                        ),
                    },
                    {
                        "id": 5,
                        "question": "Do you offer refunds?",
                        "answer": (
                            "We offer a 14-day money-back guarantee on all paid courses. "
                            "If you're not satisfied, contact our support team within "
                            "14 days of purchase for a full refund."
                        ),
                    },
                    {
                        "id": 6,
                        "question": "Is there a student discount?",
                        "answer": (
                            "Yes! Students with a valid .edu email address receive "
                            "a 30% discount on all plans. Contact us to verify "
                            "your student status."
                        ),
                    },
                ],
            },
            {
                "name": "Certification & Career",
                "faqs": [
                    {
                        "id": 7,
                        "question": "Are your certificates recognized by employers?",
                        "answer": (
                            "Our certificates are industry-recognized and valued by "
                            "employers worldwide. We partner with leading tech companies "
                            "to ensure our curriculum meets industry standards."
                        ),
                    },
                    {
                        "id": 8,
                        "question": "Do you provide job placement assistance?",
                        "answer": (
                            "Professional and Enterprise plan members receive career "
                            "guidance sessions, resume reviews, and access to our "
                            "employer network for job placement support."
                        ),
                    },
                ],
            },
        ]

        # ── CTA Data (used by cta-section.html) ───────────────────────
        context["cta_data"] = {
            "headline": "Ready to Transform Your Career?",
            "description": (
                "Join 5,000+ students who have launched successful tech careers "
                "with our expert-led training programs. Start learning today."
            ),
            "primary_label": "Enroll Now",
            "primary_url_name": "auth:register",
            "secondary_label": "Talk to an Advisor",
            "secondary_url_name": "contact",
            "background": "dark",
        }

        # ── Footer Data (used by footer.html) ─────────────────────────
        context["footer_data"] = {
            "institute_name": "CodeCraft Academy",
            "year": 2026,
            "contact": {
                "address": "123 Tech Park Avenue, Suite 200, San Francisco, CA 94105",
                "phone": "+1 (555) 987-6543",
                "email": "info@codecraftacademy.com",
            },
            "links": [
                {
                    "title": "Courses",
                    "items": [
                        {"label": "All Courses", "url_name": "courses:list"},
                        {"label": "Web Development", "url_name": "courses:by_category", "url_kwargs": {"slug": "web-development"}},
                        {"label": "Data Science", "url_name": "courses:by_category", "url_kwargs": {"slug": "data-science"}},
                        {"label": "Python", "url_name": "courses:by_category", "url_kwargs": {"slug": "python"}},
                        {"label": "DevOps", "url_name": "courses:by_category", "url_kwargs": {"slug": "devops"}},
                    ],
                },
                {
                    "title": "Company",
                    "items": [
                        {"label": "About Us", "url_name": "about"},
                        {"label": "Our Team", "url_name": "instructors:list"},
                        {"label": "Careers", "url_name": "careers"},
                        {"label": "Blog", "url_name": "blog:list"},
                        {"label": "Contact", "url_name": "contact"},
                    ],
                },
                {
                    "title": "Support",
                    "items": [
                        {"label": "Help Center", "url_name": "help"},
                        {"label": "Community Forum", "url_name": "forum"},
                        {"label": "FAQ", "url_name": "faq"},
                        {"label": "Student Resources", "url_name": "resources"},
                    ],
                },
            ],
            "social": context["institute"]["social"],
        }

        # ── Reviews (used by review-section.html if embedded) ─────────
        context["reviews"] = {
            "average_rating": 4.8,
            "total_count": 1247,
            "distribution": {
                5: 892,
                4: 251,
                3: 68,
                2: 24,
                1: 12,
            },
        }

        return context
