from django.shortcuts import render

# Create your views here.
def home(request):
    # Users's home page showing previous calculations and ability to create a new one
    return render(request, \
                  'dashboard/home.html')