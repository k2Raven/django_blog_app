from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Comment, Article


class ArticleCommentCreateView(CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment/update.html'
    form_class = CommentForm
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.article.pk })


