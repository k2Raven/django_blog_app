from django.db import models
from django.urls import reverse

from webapp.validate import at_least_8, MinLengthValidator
from django.core.validators import MaxLengthValidator


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown",
                              validators=(MinLengthValidator(6),))
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент",
                               validators=(at_least_8,))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', blank=True)

    def get_absolute_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.pk})

    def get_comments_count(self):
        return self.comments.count()

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=50, default='Unknown', verbose_name='Автор')
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='comments',
                                verbose_name="Статья")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'
