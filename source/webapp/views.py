from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse


def index_views(request, *args, **kwargs):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, "index.html", context)


def article_view(request, pk, *args, **kwargs):
    # article_id = kwargs.get('pk')
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('Not Found')
    #     raise Http404
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request):
    if request.method == "GET":
        return render(request, "article_create.html")
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        new_article = Article.objects.create(title=title, content=content, author=author)
        # context = {'article': new_article}
        # return render(request, 'article_view.html', context)
        # url = reverse('article_view', kwargs={'pk':new_article.pk})
        # print(url)
        # return HttpResponseRedirect(url)
        return redirect('article_view', pk=new_article.pk)
