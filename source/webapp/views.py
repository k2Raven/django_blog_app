from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Article
from webapp.forms import ArticleForm
from django.views import View

from django.views.generic import TemplateView, RedirectView, FormView
from webapp.base_views import FormView as CustomFormView


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('-created_at')
        context = {
            'articles': articles
        }
        return render(request, "index.html", context)


class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        kwargs['article'] = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class MyRedirectView(RedirectView):
    url = 'https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/RedirectView/'


class ArticleCreateView(CustomFormView):
    template_name = "article_create.html"
    form_class = ArticleForm

    def get_redirect_url(self):
        return reverse('article_view', kwargs={'pk': self.article.pk})

    def form_valid(self, form):
        # tags = form.cleaned_data.pop('tags')
        # self.article = Article.objects.create(**form.cleaned_data)
        # self.article.tags.set(tags)
        self.article = form.save()
        return super().form_valid(form)


class ArticleUpdateView(FormView):
    template_name = "article_update.html"
    form_class = ArticleForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.article
        return kwargs

    # def get_initial(self):
    #     initial = {}
    #     for key in 'title', 'content', 'author':
    #         initial[key] = getattr(self.article, key)
    #     initial['tags'] = self.article.tags.all()
    #     return initial

    def form_valid(self, form):
        # tags = form.cleaned_data.pop('tags')
        # for key, value in form.cleaned_data.items():
        #     if value is not None:
        #         setattr(self.article, key, value)
        # self.article.save()
        # self.article.tags.set(tags)
        self.article = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.article.pk})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == "POST":
        article.delete()
        return redirect('index')
