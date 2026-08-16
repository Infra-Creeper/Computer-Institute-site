from django.shortcuts import render
home_context ={
    'site_name':'Compuetech'
}

# Create your views here.
def home(request):
    return render(request,"home.html",context=home_context)

def courses(request):
    return render(request,"courses/list.html")