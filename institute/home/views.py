from django.shortcuts import render

home_context = {
    'site_name': 'Compuetech'
}


def home(request):
    return render(request, "home.html", context=home_context)


def course_list(request):
    return render(request, "courses/list.html")


def course_detail(request, slug):
    return render(request, "courses/detail.html", {"slug": slug})


def notice_board(request):
    return render(request, "notices/board.html")


def notice_detail(request, slug):
    return render(request, "notices/detail.html", {"slug": slug})


def blog_list(request):
    return render(request, "blog/list.html")


def blog_detail(request, slug):
    return render(request, "blog/detail.html", {"slug": slug})


def admission_form(request):
    return render(request, "admission/form.html")


def admission_success(request):
    return render(request, "admission/success.html")


def about(request):
    return render(request, "about.html", context=home_context)


def contact(request):
    return render(request, "contact.html", context=home_context)