from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   # path — означает путь.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='posts'),
   path('search/', PostsList.as_view(), name='search'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/update/', PostUpdate.as_view(), name='articles_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
]