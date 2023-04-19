# Import path for urls
from django.urls import path

# Import all from views
from . import views

# Create a Namespace
app_name = 'polls'

urlpatterns = [
    # Create path to index view;
        # Include in main app urls.py
    path('', views.index, name ='index'),
    # Using parameter pass question id as int in path
    path('<int:question_id>', views.detail, name = 'detail'),
    path('<int:question_id>/results', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name ='vote')
]