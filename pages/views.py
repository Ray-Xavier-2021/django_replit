from django.shortcuts import render

# Create your views here.
# Landing Page view
def index(request):
    return render(request, 'pages/index.html')