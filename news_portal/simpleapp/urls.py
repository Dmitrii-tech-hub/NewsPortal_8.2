from django.urls import path
from .views import (
    NewsListView,
    NewsDetailView,
    NewsCreateView,
    ArticleCreateView,
    NewsUpdateView,
    ArticleUpdateView,
    SearchView,
    profile_view
)

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('news/search/', SearchView.as_view(), name='news_search'),
    path('accounts/profile/', profile_view, name='account_profile'),
]
