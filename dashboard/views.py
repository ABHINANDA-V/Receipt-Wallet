from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard_page(request):
    return render(request,'dashboard.html')
