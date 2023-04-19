# Import path for urls
from django.urls import path

# Import all from views
from . import views


urlpatterns = [
    # Create path to index view;
        # Include in main app urls.py
    path('', views.index, name ='index'),
]