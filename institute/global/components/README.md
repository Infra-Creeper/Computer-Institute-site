# Computer Training Institute — HTMX + Django Component Library

## Overview

This component library provides **33 modular, reusable HTML partials** for building an SEO-optimized website for a computer training institute using **HTMX**, **Django**, and **Tailwind CSS**.

Each component is a standalone `.html` file designed to be included via Django's `{% include %}` template tag or rendered dynamically via HTMX endpoints.

---

## Directory Structure

```
components/
├── header/                  # Navigation & breadcrumbs
│   ├── navbar.html
│   ├── breadcrumb.html
│   └── mega-menu.html
├── hero/                    # Hero section & statistics
│   ├── hero.html
│   └── hero-stats.html
├── courses/                 # Course catalog & filtering
│   ├── course-card.html
│   ├── course-grid.html
│   ├── course-filter.html
│   ├── course-detail-hero.html
│   ├── search-bar.html
│   └── filter-sidebar.html
├── testimonials/            # Reviews & ratings
│   ├── testimonial-card.html
│   ├── testimonial-carousel.html
│   └── review-section.html
├── instructors/             # Instructor profiles
│   ├── instructor-card.html
│   └── instructor-grid.html
├── faq/                     # Frequently asked questions
│   ├── faq-item.html
│   └── faq-section.html
├── forms/                   # Contact, newsletter, CTAs
│   ├── contact-form.html
│   ├── contact-info-card.html
│   ├── newsletter-signup.html
│   ├── cta-button.html
│   └── cta-section.html
├── pricing/                 # Pricing plans
│   ├── pricing-card.html
│   └── pricing-table.html
├── footer/                  # Site footer
│   ├── footer.html
│   └── footer-link-group.html
└── utils/                   # Reusable utility components
    ├── badge.html
    ├── stat-counter.html
    ├── modal.html
    ├── loading-spinner.html
    ├── error-message.html
    └── success-message.html
```

---

## Component Summary

| # | Component | File | Lines | Purpose |
|---|-----------|------|-------|---------|
| 1 | Navbar | `header/navbar.html` | 156 | Sticky navigation with logo, links, CTA, mobile toggle |
| 2 | Breadcrumb | `header/breadcrumb.html` | 80 | SEO breadcrumb with schema.org JSON-LD |
| 3 | Mega Menu | `header/mega-menu.html` | 65 | Expandable category dropdown |
| 4 | Hero | `hero/hero.html` | 82 | Full-width hero with headline and CTAs |
| 5 | Hero Stats | `hero/hero-stats.html` | 89 | Statistics banner with counters |
| 6 | Course Card | `courses/course-card.html` | 163 | Individual course card with schema.org |
| 7 | Course Grid | `courses/course-grid.html` | 88 | Responsive grid with infinite scroll |
| 8 | Course Filter | `courses/course-filter.html` | 160 | Sidebar filter with live HTMX updates |
| 9 | Course Detail Hero | `courses/course-detail-hero.html` | 247 | Full course detail with enrollment card |
| 10 | Search Bar | `courses/search-bar.html` | 86 | HTMX-powered autocomplete search |
| 11 | Filter Sidebar | `courses/filter-sidebar.html` | 142 | Collapsible filter panel |
| 12 | Testimonial Card | `testimonials/testimonial-card.html` | 82 | Single review card with schema.org |
| 13 | Testimonial Carousel | `testimonials/testimonial-carousel.html` | 164 | Paginated testimonial slider |
| 14 | Review Section | `testimonials/review-section.html` | 94 | Rating summary with distribution bars |
| 15 | Instructor Card | `instructors/instructor-card.html` | 148 | Profile card with social links |
| 16 | Instructor Grid | `instructors/instructor-grid.html` | 40 | Responsive instructor grid |
| 17 | FAQ Item | `faq/faq-item.html` | 97 | Expandable FAQ accordion item |
| 18 | FAQ Section | `faq/faq-section.html` | 82 | Full FAQ with JSON-LD structured data |
| 19 | Contact Form | `forms/contact-form.html` | 163 | Lead capture form with validation |
| 20 | Contact Info Card | `forms/contact-info-card.html` | 127 | Address, phone, email, hours |
| 21 | Newsletter Signup | `forms/newsletter-signup.html` | 83 | Email subscription component |
| 22 | CTA Button | `forms/cta-button.html` | 74 | Reusable CTA button variants |
| 23 | CTA Section | `forms/cta-section.html` | 61 | Full-width CTA banner |
| 24 | Pricing Card | `pricing/pricing-card.html` | 83 | Individual pricing tier |
| 25 | Pricing Table | `pricing/pricing-table.html` | 94 | Multi-plan comparison table |
| 26 | Footer | `footer/footer.html` | 160 | Multi-column footer with social links |
| 27 | Footer Link Group | `footer/footer-link-group.html` | 36 | Organized footer link section |
| 28 | Badge | `utils/badge.html` | 44 | Reusable tag/category badge |
| 29 | Stat Counter | `utils/stat-counter.html` | 88 | Animated number counter |
| 30 | Modal | `utils/modal.html` | 114 | Reusable modal dialog |
| 31 | Loading Spinner | `utils/loading-spinner.html` | 56 | HTMX loading indicator |
| 32 | Error Message | `utils/error-message.html` | 67 | Dismissible error alert |
| 33 | Success Message | `utils/success-message.html` | 71 | Success notification |

---

## Key Features

### SEO Optimization
- **Schema.org structured data**: Course, Organization, LocalBusiness, Person, Review, AggregateRating, FAQPage, BreadcrumbList, Question/Answer
- **Semantic HTML5**: `<nav>`, `<header>`, `<footer>`, `<section>`, `<article>`, `<aside>`, `<address>`
- **Proper heading hierarchy**: h1 → h2 → h3 without skipped levels
- **Alt text** on all images
- **JSON-LD microdata** in breadcrumb, FAQ, and course components

### HTMX Integration
- Live search with debounce (`keyup changed delay:500ms`)
- Infinite scroll pagination (`revealed` trigger)
- Form submission without page reload (`hx-post`)
- Live filtering (`change` trigger on filter inputs)
- Accordion/expand (`click` trigger on FAQ items)
- Loading indicators via `hx-indicator`

### Tailwind CSS
- Custom color palette: steel-blue, jet-black, sandy-brown, almond-cream, deep-space-blue
- Mobile-first responsive design (sm, md, lg, xl breakpoints)
- Dark mode support with `dark:` prefix
- No inline styles — all styling via Tailwind utility classes

### Accessibility
- ARIA labels on all interactive elements
- `aria-expanded`, `aria-controls`, `aria-current` for dynamic content
- Skip navigation link in navbar
- Proper `<label>` associations for all form inputs
- `role="alert"` and `role="status"` for notifications
- Keyboard navigable (tab order, focus indicators)
- WCAG AA color contrast compliance

---

## Usage Example

### In a Django Template

```html
{% extends "base.html" %}
{% block content %}

  {% include "components/header/navbar.html" %}
  {% include "components/header/breadcrumb.html" %}

  <main id="main-content">
    {% include "components/hero/hero.html" %}
    {% include "components/hero/hero-stats.html" %}

    <section>
      {% include "components/courses/search-bar.html" %}
      <div class="flex gap-8">
        <aside class="w-64 hidden lg:block">
          {% include "components/courses/course-filter.html" %}
        </aside>
        {% include "components/courses/course-grid.html" %}
      </div>
    </section>

    {% include "components/testimonials/testimonial-carousel.html" %}
    {% include "components/instructors/instructor-grid.html" %}
    {% include "components/faq/faq-section.html" %}
    {% include "components/forms/newsletter-signup.html" %}
    {% include "components/forms/cta-section.html" %}
  </main>

  {% include "components/footer/footer.html" %}

{% endblock %}
```

### HTMX Endpoint Example (Django View)

```python
from django.shortcuts import render
from django.views.decorators.http import require_GET

@require_GET
def course_search(request):
    q = request.GET.get('q', '')
    courses = Course.objects.filter(title__icontains=q)[:5]
    results = []
    for course in courses:
        results.append({
            'id': course.id,
            'title': course.title,
            'price': course.price,
        })
    return render(request, 'components/courses/search-results.html', {
        'results': results,
    })
```

---

## Django URL Configuration Reference

Components reference these Django URL names (configure in your `urls.py`):

| URL Name | Description | Used By |
|----------|-------------|---------|
| `home` | Homepage | navbar |
| `auth:login` | Login page | navbar |
| `auth:register` | Registration page | navbar, CTA |
| `dashboard` | User dashboard | navbar |
| `courses:list` | Course listing | navbar, grid |
| `courses:detail` | Course detail page | course-card, detail-hero |
| `courses:enroll` | Enrollment action | course-card, detail-hero |
| `courses:by_category` | Category filter | course-card, detail-hero |
| `courses:filter` | Filter endpoint | course-filter, filter-sidebar |
| `courses:search` | Search endpoint | search-bar |
| `courses:card` | Single card endpoint | course-grid |
| `categories:list` | Category listing | mega-menu |
| `instructors:detail` | Instructor profile | course-card, instructor-card |
| `testimonials:page` | Paginated testimonials | testimonial-carousel |
| `faq:detail` | FAQ answer endpoint | faq-item |
| `contact:submit` | Contact form endpoint | contact-form |
| `newsletter:subscribe` | Newsletter endpoint | newsletter-signup |
| `enrollment:create` | Enrollment creation | course-detail-hero |
| `courses:wishlist_toggle` | Wishlist toggle | course-detail-hero |
| `privacy` | Privacy policy | footer |
| `terms` | Terms of service | footer |
| `sitemap` | Sitemap page | footer |

---

## Tailwind Configuration

Add the following to your `tailwind.config.js`:

```javascript
module.exports = {
  content: ["./templates/**/*.{html,py}"],
  theme: {
    extend: {
      colors: {
        "steel-blue": {
          50: "#eef3f6", 100: "#dde8ee", 200: "#bcd0dc",
          300: "#9ab9cb", 400: "#78a2ba", 500: "#578aa8",
          600: "#456f87", 700: "#345365", 800: "#233743",
          900: "#111c22", 950: "#0c1318"
        },
        "jet-black": {
          50: "#eef2f6", 100: "#dde5ee", 200: "#bbcbdd",
          300: "#99b1cc", 400: "#7797bb", 500: "#557daa",
          600: "#446488", 700: "#334b66", 800: "#223244",
          900: "#111922", 950: "#0c1118"
        },
        "sandy-brown": {
          50: "#fdf2e7", 100: "#fbe4d0", 200: "#f8c9a0",
          300: "#f4ae71", 400: "#f19341", 500: "#ed7812",
          600: "#be600e", 700: "#8e480b", 800: "#5f3007",
          900: "#2f1804", 950: "#211102"
        },
        "almond-cream": {
          50: "#faf3eb", 100: "#f5e7d6", 200: "#eaceae",
          300: "#e0b685", 400: "#d59d5d", 500: "#cb8534",
          600: "#a26a2a", 700: "#7a501f", 800: "#513515",
          900: "#291b0a", 950: "#1c1307"
        },
        "deep-space-blue": {
          50: "#eaf3fa", 100: "#d5e6f6", 200: "#accdec",
          300: "#82b4e3", 400: "#599bd9", 500: "#2f82d0",
          600: "#2668a6", 700: "#1c4e7d", 800: "#133453",
          900: "#091a2a", 950: "#07121d"
        }
      }
    }
  },
  plugins: [require('@tailwindcss/line-clamp')]
}
```

---

## License

Free to use for personal and commercial projects.
