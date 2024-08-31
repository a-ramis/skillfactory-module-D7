from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post


# Создаем свой набор фильтров для модели Post.
class PostFilter(FilterSet):
    creation = DateFilter(field_name='creation', widget=DateInput(attrs={'type':'date'}),
                          lookup_expr='date__gte'
                          )
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'name': ['icontains'],
            'author': ['exact'],
            'genre': ['exact'],
        }
