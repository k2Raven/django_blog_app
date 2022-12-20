from django.contrib import admin
from webapp.models import Article, Tag


class ArticleTagInlines(admin.TabularInline):
    model = Article.tags.through


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    # fields = ['id', 'title', 'author', 'content', 'created_at', 'updated_at']
    exclude = ['tags']
    readonly_fields = ['created_at', 'updated_at']
    # filter_horizontal = ['tags']
    inlines = (ArticleTagInlines,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
