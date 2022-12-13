from django.urls import path
from webapp.views import IndexViews, ArticleCreateView, ArticleView, MyRedirectView, ArticleUpdateView, \
    ArticleDeleteView, ArticleCommentCreateView, CommentUpdateView, CommentDeleteView
from django.views.generic import RedirectView

app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index')),
    path('articles/', IndexViews.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/comment/add/', ArticleCommentCreateView.as_view(), name='article_comment_add'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('redirect_view/', MyRedirectView.as_view())
]