from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article
from webapp.forms import ArticleForm


def index_views(request, *args, **kwargs):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, "index.html", context)


def article_view(request, pk, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "article_create.html", {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content']
            )
            return redirect('article_view', pk=new_article.pk)
        else:
            return render(request, "article_create.html", {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            'title': article.title,
            'author': article.author,
            'content': article.content,
        })
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.author = form.cleaned_data.get('author')
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == "POST":
        article.delete()
        return redirect('index')
