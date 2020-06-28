from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from .models import Movie, Review, Comment, Genre, Emotion
from .forms import MovieForm, ReviewForm, CommentForm, SearchForm
import requests
import random
from django.core.paginator import Paginator


# Create your views here.
def first_page(request):
    if request.user.is_authenticated:
        user = request.user
        emotions = Emotion.objects.all()
        for emotion in emotions:
            a = emotion.emotion.all()
            if user in a:
                return redirect('movies:movie_list')
        return render(request, 'movies/first_page.html')
    return redirect('movies:movie_list')


def movie_list(request):
    movies = Movie.objects.all().order_by('-vote_average')
    if request.user.is_authenticated:
        emotion = request.user.user_emotion.all()
        if not emotion:
            return redirect('movies:first_page')
        genres = emotion[0].genres.all()
        movie_list = []
        start = [0, 1]
        while len(movie_list) <= 15:
            c = random.choice(start)
            if len(genres) <= 1 and c == 1:
                start.pop(c)
                c = random.choice(start)
            genre = genres[c]
            cnt = 0
            for movie in movies:
                if movie.vote_count <= 1000:
                    continue
                if cnt == 15:
                    break
                genres = movie.genre_ids.all()
                if genre in genres:
                    movie_list.append(movie)
                    cnt += 1
            movies1 = movie_list[0:5]
            movies2 = movie_list[5:10]
            movies3 = movie_list[10:15]
    else:
        movies1 = movies[0:5]
        movies2 = movies[5:10]
        movies3 = movies[10:15]
    first_movie = movies1[0]

    movies_2 = Movie.objects.all().order_by('-review_count')
    movies4 = movies_2[0:5]
    movies5 = movies_2[5:10]
    movies6 = movies_2[10:15]
    # search_url = 'https://www.googleapis.com/youtube/v3/search'
    # search_params = {
    #     'part' : 'snippet',
    #     'q': first_movie.original_title + 'trailer',
    #     'key': settings.YOUTUBE_DATA_API_KEY,
    #     'maxResults': 1,
    # }
    # r = requests.get(search_url, params=search_params)
    # video = r.json()['items'][0]['id']['videoId']
    context = {
        'first_movie': first_movie,
        'movies1': movies1,
        'movies2': movies2,
        'movies3': movies3,
        'movies4': movies4,
        'movies5': movies5,
        'movies6': movies6,
        # 'trailer': video,
    }
    return render(request, 'movies/movie_list.html', context)


def recent_movie(request):
    movies = Movie.objects.all().order_by('-release_date')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recent_movie.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    query = movie.title[:3]
    genres = movie.genre_ids.all()
    movies = Movie.objects.all().filter(Q(title__contains=query) | Q(overview__contains=query))
    movie_list = []
    cnt = 0
    for movie_a in movies:
        movie_list.append(movie_a)
        cnt += 1
        if cnt == 4:
            break
    if cnt < 4:
        genre = random.choice(genres)
        all_movie = Movie.objects.all().order_by('release_date')
        for movie1 in all_movie:
            if genre in movie1.genre_ids.all():
                movie_list.append(movie1)
                cnt += 1
                if cnt == 4:
                    break
    if movie in movie_list:
        movie_list.remove(movie)
    # search_url = 'https://www.googleapis.com/youtube/v3/search'
    # search_params = {
    #     'part' : 'snippet',
    #     'q': movie.original_title + 'trailer',
    #     'key': settings.YOUTUBE_DATA_API_KEY,
    #     'maxResults': 1,
    # }
    # r = requests.get(search_url, params=search_params)
    # video = r.json()['items'][0]['id']['videoId']
    context = {
        'movie': movie,
        'reviews': reviews,
        'movie_list': movie_list,
        # 'trailer': video,
    }
    return render(request, 'movies/movie_detail.html', context)


def movie_update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context={
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/form.html', context)


def movie_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:movie_list')


def review_list(request):
    reviews = Review.objects.order_by('-pk')
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'movies/review_list.html', context)


def review_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.movie_id = movie.pk
                form.save()
                movie.review_count += 1
                movie.save()
                return redirect('movies:movie_detail', movie.pk)
        else:
            form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'movies/form.html', context)
    else:
        return redirect('accounts:login')


def review_detail(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        review = get_object_or_404(Review, pk=review_pk)
        comments = review.comment_set.all()
        form = CommentForm()
        context = {
            'movie': movie,
            'review': review,
            'form': form,
            'comments':comments,
        }
        return render(request, 'movies/review_detail.html', context)
    else:
        return redirect('accounts:login')   


def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user != review.user:
        return redirect('movies:review_list')
    if request.method =="POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movies:review_detail', movie_pk, review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'movies/form.html', context)


def review_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user != review.user:
        return redirect('movies:review_list')
    review.delete()
    movie.review_count -= 1
    movie.save()
    return redirect('movies:movie_detail', movie_pk)


def comment_create(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.review_id = review.pk
                form.save()
        return redirect('movies:review_detail', movie_pk, review.pk)
    else:
        return redirect('accounts:login')

@require_POST
def comment_delete(request, movie_pk, review_pk, comment_pk):
    if request.method=="POST":
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:review_detail', movie_pk, review_pk)


def like(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True
    context = {
        'count': movie.like_users.count(),
        'liked': liked,
    }
    return JsonResponse(context)


# 감정 데이터 추출
@login_required
def emotion(request, pk):
    user = request.user
    emotion = get_object_or_404(Emotion, pk=pk)
    emotion.emotion.add(user)
    return redirect('movies:movie_list')


@login_required
def emotion_remove(request):
    user = request.user
    emotions = Emotion.objects.all()
    for emotion in emotions:
        a = emotion.emotion.all()
        if user in a:
            emotion.emotion.remove(user)
    return redirect('movies:first_page')


def search_result(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.all().filter(Q(title__contains=query) | Q(overview__contains=query))
    context = {
        'query': query,
        'movies': movies,
    }
    return render(request, 'movies/search_result.html', context)    



   