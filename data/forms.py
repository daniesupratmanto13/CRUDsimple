from django.forms import ModelForm
from .models import BookModel


class BookForm(ModelForm):

    class Meta:
        model = BookModel
        fields = (
            'author',
            'title',
            'genre',
        )
