from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Tag, Article
from webapp.validate import at_least_8, MinLengthValidator


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=50, required=True, label='Title', validators=(at_least_8,))
#     author = forms.CharField(max_length=50, required=True, label='Author', validators=(MinLengthValidator(6),))
#     content = forms.CharField(max_length=3000, required=True, label='Content',
#                               widget=widgets.Textarea(attrs={"cols": 20, 'rows': 3}))
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, label='Теги')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'tags']
        # exclude = []
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
            # raise ValidationError('Длина зтого поля должна составлять не меенее %(length)d символов!', code='too_short',
            #                       params={'length': 5})
            self.add_error('title', ValidationError('Длина зтого поля должна составлять не меенее %(length)d символов!',
                                                    code='too_short', params={'length': 5}))
        return title

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['title'] == cleaned_data.get('content', ''):
            raise ValidationError('Текст статьи не должен дублировать ее название!')
        return cleaned_data


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')