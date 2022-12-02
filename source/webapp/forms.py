from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple,
        }
        error_messages = {
            'content': {
                'required': 'Поле должно быть заполнено'
            }
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            self.add_error('title', ValidationError('Длина зтого поля должна составлять не меенее %(length)d символов!',
                                                    code='too_short', params={'length': 5}))
        return title

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['title'] == cleaned_data.get('content', ''):
            raise ValidationError('Текст статьи не должен дублировать ее название!')
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')