from cProfile import label

from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, CharFilter
from .models import Post, Category, Author
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    title = CharFilter(
        lookup_expr='icontains',
        label='Название'
    )

    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='все авторы',
    )

    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='все категории',
    )

    added_after = DateTimeFilter(
        field_name='created_at',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )
