from django.core.validators import BaseValidator
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


def at_least_8(string):
    if len(string) < 8:
        raise ValidationError('Это значение слишком короткое!')


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Значение "%(value)s" имеет длину %(show_value)d ! А дольжна быть длиннее %(limit_value)d символов!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)
