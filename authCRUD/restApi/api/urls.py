from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookAPIView, DetailView,raw_SQL


urlpatterns = [
path('', BookAPIView.as_view()),
path('<int:pk>/', DetailView.as_view()),
path('rawSQL',  raw_SQL)

]
