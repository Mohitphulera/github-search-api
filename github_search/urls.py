from django.urls import path
from . import views

urlpatterns = [
    path('api/search/', views.GitHubSearchView.as_view(), name='search_github'),
    path('api/clear-cache/', views.ClearCacheView.as_view(), name='clear_cache'),
]
