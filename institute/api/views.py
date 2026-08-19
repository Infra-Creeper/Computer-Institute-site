from datetime import date

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_POST

from home.models import Admission, Contact, Notice


def _notice_context(notice):
	return {
		"title": notice.title,
		"date": notice.published_at,
		"content": notice.message,
		"excerpt": notice.message,
		"slug": notice.slug,
		"is_recent": notice.published_at.date() == date.today(),
	}


def _render_notice(request, notice):
	notice_context = _notice_context(notice)
	return render_to_string(
		"partials/_notice_item.html",
		{"notice": notice_context},
		request=request,
	)


@require_GET
def latest_notices(request):
	notices = Notice.objects.all()[:3]
	if not notices:
		return HttpResponse('<p class="text-sm">No notices available.</p>')
	return HttpResponse("".join(_render_notice(request, notice) for notice in notices))


@require_GET
def notice_list(request):
	paginator = Paginator(Notice.objects.all(), 10)
	page = paginator.get_page(request.GET.get("page", 1))
	if not page.object_list:
		return HttpResponse('<p class="py-8">No notices available.</p>')
	return HttpResponse("".join(_render_notice(request, notice) for notice in page.object_list))


def _response(message, *, success=False, response_id="form-response"):
	css_class = "text-green-700" if success else "text-red-700"
	return HttpResponse(
		f'<div id="{response_id}" class="{css_class}" role="alert">{message}</div>'
	)


@require_POST
def submit_contact(request):
	contact = Contact(
		name=request.POST.get("name", "").strip(),
		email_or_phone=request.POST.get("email", "").strip(),
		message=request.POST.get("message", "").strip(),
	)
	try:
		contact.full_clean()
	except ValidationError:
		return _response("Please complete all contact fields.", response_id="contact-response")

	contact.save()
	return _response("Thanks. Your message has been sent.", success=True, response_id="contact-response")


@require_POST
def submit_admission(request):
	gender_value = request.POST.get("gender", "")
	category_value = request.POST.get("category", "")
	gender = {"male": "M", "female": "F", "other": "O"}.get(
		gender_value.lower(), gender_value
	)
	category = {
		"general": "GEN",
		"obc": "OBC",
		"sc": "SC",
		"st": "ST",
		"ews": "EWS",
		"other": "OTHER",
		"irdp": "OTHER",
		"bpl": "OTHER",
	}.get(category_value.lower(), category_value)
	application = Admission(
		course_name=request.POST.get("course_name", "").strip(),
		name=request.POST.get("name", "").strip(),
		guardian=request.POST.get("so-do", "").strip(),
		address=request.POST.get("address", "").strip(),
		gender=gender,
		contact_number=request.POST.get("contact_no", "").strip(),
		nationality=request.POST.get("nationality", "").strip(),
		category=category,
		highest_qualification=request.POST.get("highest_qualification", "").strip(),
	)
	try:
		application.dob = date.fromisoformat(request.POST.get("dob", ""))
		application.full_clean()
	except (ValueError, ValidationError):
		return _response("Please check the application fields and try again.")

	application.save()
	return _response(
		f"Application received. Your reference is <strong>{application.ref_id}</strong>.",
		success=True,
	)
