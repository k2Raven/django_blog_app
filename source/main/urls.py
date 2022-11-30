"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views import IndexViews, ArticleCreateView, ArticleView, MyRedirectView, ArticleUpdateView, \
    article_delete_view
from django.views.generic import RedirectView

urlpatterns = [
    path('silk/', include('silk.urls', namespace='silk')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='index')),
    path('articles/', IndexViews.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', article_delete_view, name='article_delete'),
    path('redirect_view/', MyRedirectView.as_view())
]
