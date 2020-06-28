from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)


class Cast(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    popularity = models.FloatField()
    overview = models.TextField()
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    cast = models.ManyToManyField(Cast, related_name='movie_cast', db_constraint=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    movie_rating = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_rank', blank=True)
    review_count = models.IntegerField(default=0)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Emotion(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='emotion_genre')
    emotion = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_emotion', blank=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)