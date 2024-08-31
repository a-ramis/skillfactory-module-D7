from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse


# модель авторов, содержащая метод обновления рейтинга
class Author(models.Model):
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        posts_rating = self.posts.aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comments_rating = self.user.comments.aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        posts_comments_rating = self.posts.aggregate(pcr=Coalesce(Sum('comment__rating'), 0))['pcr']

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()

# модель категорий
class Category(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField('Post', through='PostCategory')


article = 'AR'
news = 'NE'
genres = [
    (article, 'Статья'),
    (news, 'Новость')
]

# модель постов, содержащая методы лайка, дизлайка и просмотра превью поста
class Post(models.Model):
    genre = models.CharField(max_length=2, choices=genres)
    creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

# модель, реализующая связь "многие ко многим" постов и категорий
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

# модель комментариев, содержащая методы лайка и дизлайка
class Comment(models.Model):
    text = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
